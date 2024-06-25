import traceback
from threading import Thread

import config
import os
import praw

from discord_client import DiscordClient
from google_sheets_recorder import GoogleSheetsRecorder
from janitor import Janitor
from reddit_actions_handler import RedditActionsHandler
from settings import *
import time

if __name__ == "__main__":
    # get config from env vars if set, otherwise from config file
    client_id = os.environ.get("CLIENT_ID", config.CLIENT_ID)
    client_secret = os.environ.get("CLIENT_SECRET", config.CLIENT_SECRET)
    bot_username = os.environ.get("BOT_USERNAME", config.BOT_USERNAME)
    bot_password = os.environ.get("BOT_PASSWORD", config.BOT_PASSWORD)
    discord_token = os.environ.get("DISCORD_TOKEN", config.DISCORD_TOKEN)
    discord_error_guild_name = os.environ.get("DISCORD_ERROR_GUILD", config.DISCORD_ERROR_GUILD)
    discord_error_channel_name = os.environ.get("DISCORD_ERROR_CHANNEL", config.DISCORD_ERROR_CHANNEL)
    subreddits_config = os.environ.get("SUBREDDITS", config.SUBREDDITS)
    subreddit_names = [subreddit.strip() for subreddit in subreddits_config.split(",")]
    print("CONFIG: subreddit_names=" + str(subreddit_names) + ", client_id=" + client_id)

    discord_client = DiscordClient(discord_error_guild_name, discord_error_channel_name)
    discord_client.add_commands()
    Thread(target=discord_client.run, args=(discord_token,)).start()

    while not discord_client.is_ready:
        time.sleep(1)

    while True:
        try:
            reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent="flyio:com.statementbot.location-bot:v3.1",
                redirect_uri="http://localhost:8080",  # unused for script applications
                username=bot_username,
                password=bot_password
            )

            google_sheets_recorder = GoogleSheetsRecorder(discord_client)
            reddit_handler = RedditActionsHandler(reddit, discord_client)

            subreddits = list()
            settings_map = dict()
            for subreddit_name in subreddit_names:
                settings = SettingsFactory.get_settings(subreddit_name)
                print(f"Creating Subreddit: {subreddit_name} with {type(settings).__name__} settings")
                subreddit = reddit.subreddit(subreddit_name)
                subreddits.append(subreddit)
                settings_map[subreddit.display_name.lower()] = settings
                google_sheets_recorder.add_sheet_for_sub(subreddit_name,
                                                         settings.google_sheet_id, settings.google_sheet_name)

            janitor = Janitor(discord_client, bot_username, reddit, reddit_handler,
                              google_sheets_recorder, settings_map)
            while True:
                for subreddit in subreddits:
                    try:
                        print("____________________")
                        print(f"Checking Subreddit: {subreddit}")
                        janitor.handle_posts(subreddit)
                    except Exception as e:
                        message = f"Exception when handling all posts: {e}\n```{traceback.format_exc()}```"
                        discord_client.send_error_msg(message)
                        print(message)
                time.sleep(Settings.post_check_frequency_mins * 60)
        except Exception as e:
            message = f"Exception in main processing: {e}\n```{traceback.format_exc()}```"
            discord_client.send_error_msg(message)
            print(message)
            time.sleep(Settings.post_check_frequency_mins * 60)

