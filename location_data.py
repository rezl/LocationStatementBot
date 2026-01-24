"""
Location database for natural language detection.
Contains countries, states/provinces, abbreviations, and major cities worldwide.
Optimized for memory efficiency on fly.io free tier.
"""

# =============================================================================
# COUNTRIES
# =============================================================================

COUNTRIES = {
    # Major English-speaking
    "usa", "united states", "america", "us",
    "uk", "united kingdom", "britain", "england", "scotland", "wales", "northern ireland",
    "canada", "australia", "new zealand", "ireland",

    # Europe
    "france", "germany", "italy", "spain", "portugal", "netherlands", "belgium",
    "switzerland", "austria", "poland", "czech republic", "czechia", "slovakia",
    "hungary", "romania", "bulgaria", "greece", "turkey", "sweden", "norway",
    "finland", "denmark", "iceland", "estonia", "latvia", "lithuania",
    "ukraine", "russia", "belarus", "moldova", "croatia", "slovenia", "serbia",
    "bosnia", "montenegro", "albania", "north macedonia", "kosovo", "luxembourg",
    "malta", "cyprus", "monaco", "liechtenstein", "andorra", "san marino",

    # Asia
    "china", "japan", "south korea", "korea", "north korea", "taiwan",
    "india", "pakistan", "bangladesh", "sri lanka", "nepal", "bhutan",
    "thailand", "vietnam", "philippines", "indonesia", "malaysia", "singapore",
    "myanmar", "cambodia", "laos", "brunei", "east timor", "mongolia",
    "kazakhstan", "uzbekistan", "turkmenistan", "tajikistan", "kyrgyzstan",
    "afghanistan", "iran", "iraq", "syria", "lebanon", "jordan", "israel",
    "palestine", "saudi arabia", "yemen", "oman", "uae", "united arab emirates",
    "qatar", "bahrain", "kuwait",

    # Americas
    "mexico", "brazil", "argentina", "chile", "peru", "colombia", "venezuela",
    "ecuador", "bolivia", "paraguay", "uruguay", "guyana", "suriname",
    "panama", "costa rica", "nicaragua", "honduras", "el salvador", "guatemala",
    "belize", "cuba", "jamaica", "haiti", "dominican republic", "puerto rico",
    "trinidad", "bahamas", "barbados",

    # Africa
    "egypt", "morocco", "algeria", "tunisia", "libya", "sudan", "south sudan",
    "ethiopia", "kenya", "tanzania", "uganda", "rwanda", "nigeria", "ghana",
    "south africa", "zimbabwe", "zambia", "botswana", "namibia", "mozambique",
    "angola", "democratic republic of congo", "drc", "congo", "cameroon",
    "ivory coast", "senegal", "mali", "niger", "mauritius", "madagascar",

    # Oceania
    "fiji", "papua new guinea", "samoa", "tonga", "vanuatu", "solomon islands",
    "new caledonia", "french polynesia", "guam", "hawaii",
}

# =============================================================================
# US STATES + ABBREVIATIONS
# =============================================================================

US_STATES = {
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",
    "maine", "maryland", "massachusetts", "michigan", "minnesota",
    "mississippi", "missouri", "montana", "nebraska", "nevada",
    "new hampshire", "new jersey", "new mexico", "new york", "north carolina",
    "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania",
    "rhode island", "south carolina", "south dakota", "tennessee", "texas",
    "utah", "vermont", "virginia", "washington", "west virginia",
    "wisconsin", "wyoming", "district of columbia", "washington dc", "dc",
    "puerto rico", "guam", "us virgin islands",
}

US_STATE_ABBREVS = {
    "al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id",
    "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms",
    "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok",
    "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv",
    "wi", "wy", "dc", "pr", "gu", "vi",
}

# =============================================================================
# CANADIAN PROVINCES + ABBREVIATIONS
# =============================================================================

CANADIAN_PROVINCES = {
    "ontario", "quebec", "british columbia", "alberta", "manitoba",
    "saskatchewan", "nova scotia", "new brunswick", "newfoundland",
    "newfoundland and labrador", "prince edward island", "pei",
    "northwest territories", "yukon", "nunavut",
}

CANADIAN_ABBREVS = {
    "on", "qc", "bc", "ab", "mb", "sk", "ns", "nb", "nl", "pe", "nt", "yt", "nu",
}

# =============================================================================
# UK REGIONS
# =============================================================================

UK_REGIONS = {
    "england", "scotland", "wales", "northern ireland",
    "london", "greater london", "west midlands", "east midlands",
    "yorkshire", "north west", "north east", "south west", "south east",
    "east anglia", "east of england",
}

# =============================================================================
# AUSTRALIAN STATES + ABBREVIATIONS
# =============================================================================

AUSTRALIAN_STATES = {
    "new south wales", "victoria", "queensland", "western australia",
    "south australia", "tasmania", "northern territory",
    "australian capital territory", "act",
}

AUSTRALIAN_ABBREVS = {
    "nsw", "vic", "qld", "wa", "sa", "tas", "nt", "act",
}

# =============================================================================
# OTHER MAJOR SUBDIVISIONS
# =============================================================================

OTHER_SUBDIVISIONS = {
    # Germany
    "bavaria", "baden-wurttemberg", "berlin", "hamburg", "hesse",
    "lower saxony", "north rhine-westphalia", "rhineland-palatinate",
    "saxony", "schleswig-holstein", "thuringia",

    # France
    "ile-de-france", "provence", "brittany", "normandy", "alsace",

    # India
    "maharashtra", "karnataka", "tamil nadu", "delhi", "kerala",
    "west bengal", "gujarat", "rajasthan", "uttar pradesh", "punjab",

    # Brazil
    "sao paulo", "rio de janeiro", "minas gerais", "bahia", "parana",

    # Mexico
    "jalisco", "nuevo leon", "mexico city", "cdmx", "quintana roo",

    # Japan
    "tokyo", "osaka", "kyoto", "hokkaido", "okinawa",
}

# =============================================================================
# MAJOR CITIES (100k+ population) - Organized by region
# =============================================================================

CITIES_NORTH_AMERICA = {
    # US Major Cities
    "new york", "nyc", "manhattan", "brooklyn", "queens", "bronx", "staten island",
    "los angeles", "la", "chicago", "houston", "phoenix", "philadelphia",
    "san antonio", "san diego", "dallas", "san jose", "austin", "jacksonville",
    "fort worth", "columbus", "charlotte", "san francisco", "indianapolis",
    "seattle", "denver", "washington", "boston", "el paso", "detroit",
    "nashville", "portland", "memphis", "oklahoma city", "las vegas",
    "louisville", "baltimore", "milwaukee", "albuquerque", "tucson",
    "fresno", "mesa", "sacramento", "atlanta", "kansas city", "colorado springs",
    "miami", "raleigh", "omaha", "long beach", "virginia beach", "oakland",
    "minneapolis", "tulsa", "arlington", "tampa", "new orleans", "wichita",
    "cleveland", "bakersfield", "aurora", "anaheim", "honolulu", "santa ana",
    "riverside", "corpus christi", "lexington", "stockton", "henderson",
    "saint paul", "st paul", "st louis", "st. louis", "saint louis",
    "cincinnati", "pittsburgh", "greensboro", "anchorage", "plano", "lincoln",
    "orlando", "irvine", "newark", "toledo", "durham", "chula vista",
    "fort wayne", "jersey city", "st. petersburg", "laredo", "scottsdale",
    "gilbert", "lubbock", "madison", "reno", "buffalo", "chandler", "glendale",
    "north las vegas", "garland", "hialeah", "irving", "chesapeake", "fremont",
    "baton rouge", "richmond", "boise", "spokane", "des moines", "tacoma",
    "san bernardino", "modesto", "fontana", "santa clarita", "birmingham",
    "oxnard", "fayetteville", "moreno valley", "rochester", "glendale",
    "huntington beach", "salt lake city", "grand rapids", "amarillo",
    "yonkers", "aurora", "montgomery", "akron", "little rock", "huntsville",
    "augusta", "port st. lucie", "grand prairie", "overland park", "tallahassee",
    "cape coral", "mobile", "knoxville", "shreveport", "worcester",
    "ontario", "tempe", "brownsville", "santa rosa", "vancouver", "eugene",
    "fort lauderdale", "salem", "peoria", "elk grove", "corona", "pembroke pines",
    "garden grove", "springfield", "cary", "fort collins", "hayward",
    "lancaster", "lakewood", "palmdale", "salinas", "hollywood", "pasadena",
    "sunnyvale", "pomona", "escondido", "killeen", "naperville", "joliet",
    "bellevue", "rockford", "savannah", "paterson", "torrance", "bridgeport",
    "mcallen", "mesquite", "syracuse", "midland", "pasadena", "murfreesboro",
    "macon", "alexandria", "frisco", "olathe", "waco", "thornton",

    # US Smaller but notable cities
    "milford", "roswell", "sedona", "area 51", "rachel",

    # Canada
    "toronto", "montreal", "vancouver", "calgary", "edmonton", "ottawa",
    "winnipeg", "quebec city", "hamilton", "kitchener", "london", "victoria",
    "halifax", "oshawa", "windsor", "saskatoon", "regina", "st. john's",
    "barrie", "kelowna", "abbotsford", "sudbury", "kingston", "thunder bay",
    "mississauga", "brampton", "surrey", "burnaby", "richmond", "markham",

    # Mexico
    "mexico city", "guadalajara", "monterrey", "puebla", "tijuana",
    "leon", "juarez", "zapopan", "merida", "cancun", "acapulco",
}

CITIES_EUROPE = {
    # UK
    "london", "birmingham", "manchester", "glasgow", "liverpool", "bristol",
    "sheffield", "leeds", "edinburgh", "leicester", "coventry", "bradford",
    "cardiff", "belfast", "nottingham", "kingston upon hull", "hull",
    "newcastle", "stoke-on-trent", "southampton", "derby", "portsmouth",
    "brighton", "plymouth", "wolverhampton", "reading", "aberdeen", "dundee",
    "cambridge", "oxford", "york", "bath", "canterbury", "exeter", "norwich",

    # Germany
    "berlin", "hamburg", "munich", "munchen", "cologne", "koln", "frankfurt",
    "stuttgart", "dusseldorf", "dortmund", "essen", "leipzig", "bremen",
    "dresden", "hanover", "nuremberg", "nurnberg", "duisburg", "bochum",

    # France
    "paris", "marseille", "lyon", "toulouse", "nice", "nantes", "strasbourg",
    "montpellier", "bordeaux", "lille", "rennes", "reims", "le havre",

    # Italy
    "rome", "roma", "milan", "milano", "naples", "napoli", "turin", "torino",
    "palermo", "genoa", "genova", "bologna", "florence", "firenze", "bari",
    "catania", "venice", "venezia", "verona", "messina", "padua", "trieste",

    # Spain
    "madrid", "barcelona", "valencia", "seville", "sevilla", "zaragoza",
    "malaga", "murcia", "palma", "bilbao", "alicante", "cordoba", "valladolid",

    # Netherlands
    "amsterdam", "rotterdam", "the hague", "utrecht", "eindhoven", "tilburg",

    # Belgium
    "brussels", "antwerp", "ghent", "charleroi", "liege", "bruges",

    # Poland
    "warsaw", "krakow", "lodz", "wroclaw", "poznan", "gdansk",

    # Portugal
    "lisbon", "porto", "amadora", "braga", "coimbra", "funchal",

    # Sweden
    "stockholm", "gothenburg", "malmo", "uppsala",

    # Norway
    "oslo", "bergen", "trondheim", "stavanger",

    # Denmark
    "copenhagen", "aarhus", "odense",

    # Finland
    "helsinki", "espoo", "tampere", "turku",

    # Austria
    "vienna", "wien", "graz", "linz", "salzburg", "innsbruck",

    # Switzerland
    "zurich", "geneva", "basel", "bern", "lausanne",

    # Ireland
    "dublin", "cork", "galway", "limerick",

    # Greece
    "athens", "thessaloniki", "patras", "heraklion",

    # Czech Republic
    "prague", "brno", "ostrava",

    # Hungary
    "budapest", "debrecen", "szeged",

    # Romania
    "bucharest", "cluj-napoca", "timisoara", "iasi",

    # Ukraine
    "kyiv", "kiev", "kharkiv", "odessa", "dnipro", "lviv",

    # Russia
    "moscow", "saint petersburg", "st petersburg", "novosibirsk",
    "yekaterinburg", "kazan", "nizhny novgorod", "samara", "chelyabinsk",
}

CITIES_ASIA = {
    # China
    "beijing", "shanghai", "guangzhou", "shenzhen", "chengdu", "hangzhou",
    "wuhan", "xian", "xi'an", "chongqing", "nanjing", "tianjin", "suzhou",
    "zhengzhou", "changsha", "kunming", "qingdao", "dalian", "shenyang",
    "hong kong", "macau",

    # Japan
    "tokyo", "osaka", "yokohama", "nagoya", "sapporo", "fukuoka", "kobe",
    "kawasaki", "kyoto", "saitama", "hiroshima", "sendai", "chiba",

    # South Korea
    "seoul", "busan", "incheon", "daegu", "daejeon", "gwangju", "ulsan",

    # India
    "mumbai", "bombay", "delhi", "new delhi", "bangalore", "bengaluru",
    "hyderabad", "ahmedabad", "chennai", "madras", "kolkata", "calcutta",
    "surat", "pune", "jaipur", "lucknow", "kanpur", "nagpur", "indore",
    "thane", "bhopal", "visakhapatnam", "patna", "vadodara", "ghaziabad",

    # Southeast Asia
    "bangkok", "ho chi minh city", "saigon", "hanoi", "singapore",
    "kuala lumpur", "manila", "jakarta", "surabaya", "bandung", "medan",
    "yangon", "phnom penh", "vientiane",

    # Middle East
    "dubai", "abu dhabi", "riyadh", "jeddah", "tehran", "baghdad", "damascus",
    "amman", "beirut", "tel aviv", "jerusalem", "doha", "kuwait city",
    "muscat", "manama", "istanbul", "ankara", "izmir",

    # Central Asia
    "almaty", "tashkent", "nur-sultan", "astana", "bishkek",

    # Pakistan/Bangladesh
    "karachi", "lahore", "islamabad", "rawalpindi", "dhaka", "chittagong",
}

CITIES_OCEANIA = {
    # Australia
    "sydney", "melbourne", "brisbane", "perth", "adelaide", "gold coast",
    "newcastle", "canberra", "wollongong", "hobart", "geelong", "townsville",
    "cairns", "darwin", "toowoomba", "ballarat", "bendigo",

    # New Zealand
    "auckland", "wellington", "christchurch", "hamilton", "tauranga", "dunedin",

    # Pacific Islands
    "suva", "port moresby", "noumea", "papeete",
}

CITIES_SOUTH_AMERICA = {
    # Brazil
    "sao paulo", "rio de janeiro", "rio", "brasilia", "salvador", "fortaleza",
    "belo horizonte", "manaus", "curitiba", "recife", "porto alegre",

    # Argentina
    "buenos aires", "cordoba", "rosario", "mendoza", "la plata",

    # Chile
    "santiago", "valparaiso", "concepcion",

    # Colombia
    "bogota", "medellin", "cali", "barranquilla", "cartagena",

    # Peru
    "lima", "arequipa", "trujillo", "cusco", "cuzco",

    # Venezuela
    "caracas", "maracaibo", "valencia", "barquisimeto",

    # Ecuador
    "quito", "guayaquil", "cuenca",

    # Others
    "montevideo", "asuncion", "la paz", "santa cruz", "georgetown", "paramaribo",
}

CITIES_AFRICA = {
    # North Africa
    "cairo", "alexandria", "giza", "casablanca", "rabat", "fes", "marrakech",
    "algiers", "tunis", "tripoli",

    # Sub-Saharan Africa
    "lagos", "abuja", "nairobi", "johannesburg", "cape town", "durban",
    "pretoria", "addis ababa", "dar es salaam", "kinshasa", "luanda",
    "accra", "dakar", "abidjan", "kampala", "harare", "lusaka",
    "maputo", "antananarivo", "kigali",
}

# =============================================================================
# COMBINED SETS FOR EFFICIENT LOOKUP
# =============================================================================

# All location indicators (states, provinces, countries)
ALL_REGIONS = (
    COUNTRIES |
    US_STATES |
    CANADIAN_PROVINCES |
    UK_REGIONS |
    AUSTRALIAN_STATES |
    OTHER_SUBDIVISIONS
)

# All abbreviations
ALL_ABBREVIATIONS = (
    US_STATE_ABBREVS |
    CANADIAN_ABBREVS |
    AUSTRALIAN_ABBREVS
)

# All cities
ALL_CITIES = (
    CITIES_NORTH_AMERICA |
    CITIES_EUROPE |
    CITIES_ASIA |
    CITIES_OCEANIA |
    CITIES_SOUTH_AMERICA |
    CITIES_AFRICA
)

# Everything combined for simple lookup
ALL_LOCATIONS = ALL_REGIONS | ALL_ABBREVIATIONS | ALL_CITIES

# =============================================================================
# LOCATION INDICATOR PHRASES
# =============================================================================

LOCATION_INDICATORS = [
    "in", "near", "close to", "from", "at", "over", "above",
    "outside of", "outside", "around", "by", "north of", "south of",
    "east of", "west of", "just outside", "right outside", "not far from",
    "heading to", "heading toward", "coming from", "leaving",
    "between", "approaching",
]
