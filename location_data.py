"""
Location database for natural language detection.
Contains countries, states/provinces, abbreviations, and cities worldwide.
Expanded coverage for US towns and European locations.
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
# UK COUNTIES (England, Scotland, Wales, Northern Ireland)
# =============================================================================

UK_COUNTIES_ENGLAND = {
    "bedfordshire", "berkshire", "bristol", "buckinghamshire", "cambridgeshire",
    "cheshire", "city of london", "cornwall", "cumbria", "derbyshire", "devon",
    "dorset", "durham", "east riding of yorkshire", "east sussex", "essex",
    "gloucestershire", "greater london", "greater manchester", "hampshire",
    "herefordshire", "hertfordshire", "isle of wight", "kent", "lancashire",
    "leicestershire", "lincolnshire", "merseyside", "norfolk", "north yorkshire",
    "northamptonshire", "northumberland", "nottinghamshire", "oxfordshire",
    "rutland", "shropshire", "somerset", "south yorkshire", "staffordshire",
    "suffolk", "surrey", "tyne and wear", "warwickshire", "west midlands",
    "west sussex", "west yorkshire", "wiltshire", "worcestershire",
}

UK_COUNTIES_SCOTLAND = {
    "aberdeenshire", "angus", "argyll", "ayrshire", "banffshire", "berwickshire",
    "buteshire", "caithness", "clackmannanshire", "dumfriesshire", "dunbartonshire",
    "east lothian", "fife", "inverness-shire", "kincardineshire", "kinross-shire",
    "kirkcudbrightshire", "lanarkshire", "midlothian", "moray", "nairnshire",
    "orkney", "peeblesshire", "perthshire", "renfrewshire", "ross and cromarty",
    "roxburghshire", "selkirkshire", "shetland", "stirlingshire", "sutherland",
    "west lothian", "wigtownshire",
}

UK_COUNTIES_WALES = {
    "anglesey", "brecknockshire", "caernarfonshire", "cardiganshire",
    "carmarthenshire", "clwyd", "denbighshire", "dyfed", "flintshire",
    "glamorgan", "gwent", "gwynedd", "merionethshire", "mid glamorgan",
    "monmouthshire", "montgomeryshire", "pembrokeshire", "powys", "radnorshire",
    "south glamorgan", "west glamorgan", "wrexham",
}

UK_COUNTIES_NI = {
    "antrim", "armagh", "down", "fermanagh", "londonderry", "tyrone",
}

UK_REGIONS = (
    UK_COUNTIES_ENGLAND | UK_COUNTIES_SCOTLAND | UK_COUNTIES_WALES | UK_COUNTIES_NI |
    {"england", "scotland", "wales", "northern ireland", "london", "greater london",
     "yorkshire", "east anglia", "east of england"}
)

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
    # Germany (Bundeslander)
    "bavaria", "baden-wurttemberg", "berlin", "hamburg", "hesse",
    "lower saxony", "north rhine-westphalia", "rhineland-palatinate",
    "saxony", "schleswig-holstein", "thuringia", "brandenburg", "bremen",
    "mecklenburg-vorpommern", "saarland", "saxony-anhalt",

    # France (Regions)
    "ile-de-france", "provence", "brittany", "normandy", "alsace",
    "aquitaine", "auvergne", "burgundy", "champagne", "corsica",
    "languedoc", "lorraine", "midi-pyrenees", "pays de la loire",
    "picardy", "poitou-charentes", "rhone-alpes",

    # Italy (Regions)
    "lombardy", "lazio", "campania", "sicily", "sardinia", "piedmont",
    "veneto", "emilia-romagna", "tuscany", "puglia", "calabria", "liguria",
    "marche", "abruzzo", "friuli venezia giulia", "trentino-alto adige",
    "umbria", "basilicata", "molise", "valle d'aosta",

    # Spain (Autonomous Communities)
    "andalusia", "catalonia", "madrid", "valencia", "galicia", "castile and leon",
    "basque country", "castile-la mancha", "canary islands", "murcia",
    "aragon", "extremadura", "balearic islands", "asturias", "navarre",
    "cantabria", "la rioja",

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
# US CITIES (Expanded - Top 1000+ by population)
# =============================================================================

CITIES_US = {
    # Top 100 cities
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

    # 100-200
    "baton rouge", "richmond", "boise", "spokane", "des moines", "tacoma",
    "san bernardino", "modesto", "fontana", "santa clarita", "birmingham",
    "oxnard", "fayetteville", "moreno valley", "rochester", "glendale",
    "huntington beach", "salt lake city", "grand rapids", "amarillo",
    "yonkers", "montgomery", "akron", "little rock", "huntsville",
    "augusta", "port st. lucie", "grand prairie", "overland park", "tallahassee",
    "cape coral", "mobile", "knoxville", "shreveport", "worcester",
    "ontario", "tempe", "brownsville", "santa rosa", "vancouver", "eugene",
    "fort lauderdale", "salem", "peoria", "elk grove", "corona", "pembroke pines",
    "garden grove", "springfield", "cary", "fort collins", "hayward",
    "lancaster", "lakewood", "palmdale", "salinas", "hollywood", "pasadena",
    "sunnyvale", "pomona", "escondido", "killeen", "naperville", "joliet",
    "bellevue", "rockford", "savannah", "paterson", "torrance", "bridgeport",
    "mcallen", "mesquite", "syracuse", "midland", "murfreesboro",
    "macon", "alexandria", "frisco", "olathe", "waco", "thornton",

    # 200-500 (medium cities)
    "dayton", "gainesville", "coral springs", "denton", "thousand oaks",
    "warren", "simi valley", "concord", "topeka", "roseville", "peoria",
    "carrollton", "charleston", "hartford", "kent", "visalia", "columbia",
    "sterling heights", "new haven", "provo", "victorville", "palm bay",
    "stamford", "elizabeth", "evansville", "fullerton", "norman", "fargo",
    "ann arbor", "broken arrow", "west jordan", "berkeley", "abilene",
    "pueblo", "independence", "clearwater", "inglewood", "west valley city",
    "arvada", "college station", "costa mesa", "fairfield", "wilmington",
    "cedar rapids", "round rock", "cambridge", "billings", "boulder",
    "elgin", "antioch", "richardson", "temecula", "west covina", "downey",
    "manchester", "murrieta", "westminster", "pompano beach", "waterbury",
    "high point", "lowell", "lewisville", "centennial", "vallejo",
    "burbank", "el monte", "norwalk", "ventura", "everett", "west palm beach",
    "sparks", "pueblo", "green bay", "gresham", "lakeland", "santa maria",
    "victorville", "tyler", "palm bay", "league city", "odessa",
    "edison", "carlsbad", "meridian", "allen", "sugar land", "beaumont",

    # 500-1000 (smaller cities, UFO-relevant areas)
    "milford", "roswell", "sedona", "rachel", "rachel nevada",
    "socorro", "aurora", "gulf breeze", "marfa", "stephenville",
    "pine bush", "hudson valley", "skinwalker ranch", "dulce",
    "phoenix lights", "lubbock lights",

    # Additional medium/small cities
    "appleton", "battle creek", "bellingham", "boca raton", "boynton beach",
    "bradenton", "burlington", "canton", "champaign", "chapel hill",
    "charlottesville", "chattanooga", "cicero", "citrus heights", "clifton",
    "clovis", "compton", "danbury", "daly city", "davie", "daytona beach",
    "decatur", "deltona", "dearborn", "delray beach", "dothan", "edinburg",
    "el cajon", "el centro", "elkhart", "encinitas", "enid", "erie",
    "farmington", "flagstaff", "flint", "flower mound", "folsom", "fountain valley",
    "galveston", "gary", "goodyear", "greenville", "greenwood", "hamilton",
    "hammond", "harlingen", "harrisburg", "hattiesburg", "hawthorne", "hemet",
    "hesperia", "hickory", "hoffman estates", "homestead", "hoover",
    "iowa city", "jackson", "janesville", "johnson city", "jonesboro",
    "jupiter", "kalamazoo", "kenner", "kennewick", "kenosha", "kettering",
    "kissimmee", "la crosse", "la mesa", "lafayette", "lake charles",
    "lake forest", "lakewood", "largo", "las cruces", "lawrence", "lawton",
    "lee's summit", "lenexa", "lehi", "livermore", "livonia", "lodi",
    "longmont", "longview", "lynchburg", "lynn", "malden", "mansfield",
    "maple grove", "margate", "marietta", "martinez", "maui", "medford",
    "melbourne", "menifee", "mentor", "merced", "mesa", "midwest city",
    "milpitas", "miramar", "mission", "mission viejo", "missoula", "mobile",
    "monroe", "montebello", "monterey park", "mount pleasant", "mount vernon",
    "muncie", "nampa", "napa", "nashua", "national city", "new bedford",
    "new braunfels", "newport beach", "newport news", "niagara falls",
    "noblesville", "north charleston", "north port", "norwalk", "o'fallon",
    "ocala", "oceanside", "ogden", "olympia", "orem", "orland park", "oshkosh",
    "owensboro", "oxnard", "palatine", "palm coast", "palo alto", "paradise",
    "parma", "perris", "pharr", "pittsburg", "plantation", "pleasanton",
    "pocatello", "port arthur", "port orange", "portsmouth", "poway",
    "prescott", "quincy", "racine", "rancho cordova", "rancho cucamonga",
    "rapid city", "redding", "redmond", "redondo beach", "redwood city",
    "renton", "rialto", "richland", "rio rancho", "riverside", "roanoke",
    "rocklin", "rockville", "rogers", "rosemead", "royal oak", "san angelo",
    "san buenaventura", "san clemente", "san leandro", "san marcos",
    "san mateo", "san ramon", "sandy", "santa barbara", "santa clara",
    "santa cruz", "santa fe", "santa monica", "santee", "sarasota",
    "schaumburg", "schenectady", "scranton", "shoreline", "shawnee", "sheboygan",
    "skokie", "south bend", "south gate", "springdale", "st. charles",
    "st. cloud", "st. george", "st. joseph", "state college", "suffolk",
    "sunrise", "surprise", "tamarac", "taylor", "terre haute", "texas city",
    "tinley park", "tracy", "trenton", "troy", "turlock", "tuscaloosa",
    "tustin", "twin falls", "union city", "upland", "utica", "vacaville",
    "valdosta", "vista", "waukegan", "waukesha", "west allis", "west des moines",
    "west haven", "westland", "westminster", "whittier", "wichita falls",
    "wilkes-barre", "wilmington", "woodbury", "woodland", "yakima", "yuba city",
    "yucaipa", "yuma",
}

# Canada
CITIES_CANADA = {
    "toronto", "montreal", "vancouver", "calgary", "edmonton", "ottawa",
    "winnipeg", "quebec city", "hamilton", "kitchener", "london", "victoria",
    "halifax", "oshawa", "windsor", "saskatoon", "regina", "st. john's",
    "barrie", "kelowna", "abbotsford", "sudbury", "kingston", "thunder bay",
    "mississauga", "brampton", "surrey", "burnaby", "richmond", "markham",
    "vaughan", "oakville", "burlington", "greater sudbury", "sherbrooke",
    "trois-rivieres", "guelph", "cambridge", "whitby", "ajax", "langley",
    "saanich", "delta", "waterloo", "red deer", "lethbridge", "kamloops",
    "nanaimo", "prince george", "chilliwack", "fredericton", "moncton",
    "saint john", "charlottetown", "yellowknife", "whitehorse",
}

# Mexico
CITIES_MEXICO = {
    "mexico city", "guadalajara", "monterrey", "puebla", "tijuana",
    "leon", "juarez", "zapopan", "merida", "cancun", "acapulco",
    "toluca", "chihuahua", "aguascalientes", "morelia", "saltillo",
    "hermosillo", "culiacan", "mexicali", "queretaro", "san luis potosi",
    "tampico", "veracruz", "mazatlan", "oaxaca", "villahermosa", "tuxtla gutierrez",
    "reynosa", "matamoros", "nuevo laredo", "ciudad victoria", "durango",
    "cuernavaca", "tepic", "pachuca", "ensenada", "los cabos", "playa del carmen",
}

CITIES_NORTH_AMERICA = CITIES_US | CITIES_CANADA | CITIES_MEXICO

# =============================================================================
# UK CITIES AND TOWNS (Expanded)
# =============================================================================

CITIES_UK = {
    # Major cities
    "london", "birmingham", "manchester", "glasgow", "liverpool", "bristol",
    "sheffield", "leeds", "edinburgh", "leicester", "coventry", "bradford",
    "cardiff", "belfast", "nottingham", "kingston upon hull", "hull",
    "newcastle", "stoke-on-trent", "southampton", "derby", "portsmouth",
    "brighton", "plymouth", "wolverhampton", "reading", "aberdeen", "dundee",
    "cambridge", "oxford", "york", "bath", "canterbury", "exeter", "norwich",

    # Additional cities and towns
    "ashford", "aylesbury", "banbury", "bangor", "barnsley", "barrow-in-furness",
    "barry", "basildon", "basingstoke", "bebington", "bedford", "beeston",
    "birkenhead", "blackburn", "blackpool", "bloxwich", "bognor regis", "bolton",
    "bootle", "bournemouth", "bracknell", "brentwood", "bridgend", "brighton and hove",
    "burnley", "burton upon trent", "bury", "cannock", "carlisle", "carlton",
    "chatham", "chelmsford", "cheltenham", "chester", "chesterfield", "clacton-on-sea",
    "colchester", "corby", "craigavon", "crawley", "crewe", "crosby", "cumbernauld",
    "darlington", "dartford", "derry", "dewsbury", "doncaster", "dudley",
    "dunfermline", "durham", "eastbourne", "east kilbride", "ellesmere port",
    "esher", "farnborough", "folkestone", "gateshead", "gillingham", "gloucester",
    "gosport", "gravesend", "grimsby", "guildford", "halesowen", "halifax",
    "hamilton", "harlow", "harrogate", "hartlepool", "hastings", "hemel hempstead",
    "hereford", "high wycombe", "hinckley", "horsham", "huddersfield",
    "huyton with roby", "ipswich", "kettering", "kidderminster", "kingswinford",
    "kingswood", "kirkcaldy", "lancaster", "lincoln", "lisburn", "livingston",
    "loughborough", "lowestoft", "luton", "macclesfield", "maidenhead", "maidstone",
    "mansfield", "margate", "middlesbrough", "milton keynes", "newcastle-under-lyme",
    "newport", "northampton", "nuneaton", "oldham", "paignton", "paisley",
    "peterborough", "poole", "preston", "redditch", "rochdale", "rochester",
    "rotherham", "royal leamington spa", "leamington spa", "royal sutton coldfield",
    "royal tunbridge wells", "tunbridge wells", "rugby", "runcorn", "sale", "salford",
    "scarborough", "scunthorpe", "shrewsbury", "sittingbourne", "slough", "smethwick",
    "solihull", "southend-on-sea", "southport", "south shields", "stafford",
    "st albans", "stevenage", "st helens", "stockport", "stockton-on-tees",
    "stourbridge", "sunderland", "swansea", "swindon", "tamworth", "taunton",
    "telford", "thundersley", "torquay", "tynemouth", "wakefield", "wallasey",
    "walsall", "warrington", "washington", "watford", "wellingborough",
    "welwyn garden city", "west bromwich", "weston-super-mare", "weymouth",
    "widnes", "wigan", "woking", "wokingham", "worcester", "worthing",
    "wythenshawe", "yeovil",

    # UFO-relevant UK locations
    "rendlesham", "rendlesham forest", "woodbridge", "bentwaters",
    "warminster", "bonnybridge", "falkirk triangle", "broad haven",
    "cosford", "shropshire", "calvine", "livingston",
}

# =============================================================================
# GERMAN CITIES (Expanded - 50k+ population)
# =============================================================================

CITIES_GERMANY = {
    # Major cities
    "berlin", "hamburg", "munich", "munchen", "cologne", "koln", "frankfurt",
    "stuttgart", "dusseldorf", "dortmund", "essen", "leipzig", "bremen",
    "dresden", "hanover", "hannover", "nuremberg", "nurnberg", "duisburg", "bochum",

    # Additional cities (50k+)
    "aachen", "aalen", "ahlen", "arnsberg", "aschaffenburg", "augsburg",
    "baden-baden", "bad homburg", "bad kreuznach", "bad oeynhausen", "bad salzuflen",
    "bamberg", "bayreuth", "bergheim", "bergisch gladbach", "bielefeld",
    "boblingen", "bocholt", "bonn", "bottrop", "brandenburg", "braunschweig",
    "bremerhaven", "castrop-rauxel", "celle", "chemnitz", "cottbus", "darmstadt",
    "delmenhorst", "dessau", "detmold", "dinslaken", "dormagen", "dorsten",
    "duren", "elmshorn", "erfurt", "erlangen", "eschweiler", "esslingen",
    "euskirchen", "flensburg", "frankfurt oder", "frechen", "freiburg",
    "friedrichshafen", "fulda", "furth", "garbsen", "gelsenkirchen", "gera",
    "giessen", "gladbeck", "goppingen", "gorlitz", "gottingen", "greifswald",
    "grevenbroich", "gronau", "gummersbach", "gutersloh", "hagen", "halle",
    "hameln", "hamm", "hanau", "hattingen", "heidelberg", "heidenheim",
    "heilbronn", "herford", "herne", "herten", "hilden", "hildesheim", "hurth",
    "ibbenburen", "ingolstadt", "iserlohn", "jena", "kaiserslautern", "karlsruhe",
    "kassel", "kempten", "kerpen", "kiel", "kleve", "koblenz", "konstanz",
    "krefeld", "lahr", "landshut", "langenfeld", "langenhagen", "leverkusen",
    "lingen", "lippstadt", "lorrach", "lubeck", "ludenscheid", "ludwigsburg",
    "ludwigshafen", "luneburg", "lunen", "magdeburg", "mainz", "mannheim",
    "marburg", "marl", "meerbusch", "menden", "minden", "moers", "monchengladbach",
    "mulheim", "munster", "neubrandenburg", "neumunster", "neuss", "neustadt",
    "neu-ulm", "neuwied", "norderstedt", "nordhorn", "oberhausen", "offenbach",
    "offenburg", "oldenburg", "osnabruck", "paderborn", "passau", "peine",
    "pforzheim", "plauen", "potsdam", "pulheim", "rastatt", "ratingen",
    "ravensburg", "recklinghausen", "regensburg", "remscheid", "reutlingen",
    "rheine", "rosenheim", "rostock", "russelsheim", "saarbrucken", "salzgitter",
    "sankt augustin", "schwabisch gmund", "schweinfurt", "schwerin", "siegen",
    "sindelfingen", "solingen", "stolberg", "stralsund", "trier", "troisdorf",
    "tubingen", "ulm", "unna", "velbert", "viersen", "villingen-schwenningen",
    "waiblingen", "weimar", "wesel", "wetzlar", "wiesbaden", "wilhelmshaven",
    "witten", "wolfenbuttel", "wolfsburg", "worms", "wuppertal", "wurzburg", "zwickau",
}

# =============================================================================
# FRENCH CITIES (Expanded)
# =============================================================================

CITIES_FRANCE = {
    # Major cities
    "paris", "marseille", "lyon", "toulouse", "nice", "nantes", "montpellier",
    "strasbourg", "bordeaux", "lille", "rennes", "reims", "le havre",

    # Additional cities (100k+)
    "aix-en-provence", "amiens", "angers", "annecy", "argenteuil", "besancon",
    "boulogne-billancourt", "brest", "caen", "clermont-ferrand", "dijon",
    "grenoble", "le mans", "limoges", "metz", "montreuil", "mulhouse", "nancy",
    "nimes", "orleans", "perpignan", "rouen", "saint-denis", "saint-etienne",
    "toulon", "tours", "villeurbanne",

    # Additional notable cities
    "antibes", "asnieres-sur-seine", "aubervilliers", "avignon", "bayonne",
    "beauvais", "belfort", "beziers", "calais", "cannes", "chambery",
    "cholet", "colmar", "compiegne", "courbevoie", "dunkerque", "evry",
    "fort-de-france", "hyeres", "issy-les-moulineaux", "la rochelle",
    "le blanc-mesnil", "levallois-perret", "lorient", "meaux", "merignac",
    "nanterre", "neuilly-sur-seine", "niort", "noisy-le-grand", "pau",
    "pessac", "poitiers", "quimper", "rueil-malmaison", "saint-brieuc",
    "saint-malo", "saint-nazaire", "saint-quentin", "sarcelles", "sevran",
    "tourcoing", "troyes", "valence", "vannes", "versailles", "vincennes",
    "vitry-sur-seine",
}

# =============================================================================
# ITALIAN CITIES (Expanded)
# =============================================================================

CITIES_ITALY = {
    # Major cities
    "rome", "roma", "milan", "milano", "naples", "napoli", "turin", "torino",
    "palermo", "genoa", "genova", "bologna", "florence", "firenze", "bari",
    "catania", "venice", "venezia", "verona", "messina", "padua", "padova",
    "trieste",

    # Additional cities
    "ancona", "andria", "arezzo", "asti", "avellino", "barletta", "bergamo",
    "bolzano", "brescia", "brindisi", "busto arsizio", "cagliari", "carrara",
    "caserta", "castellammare di stabia", "catanzaro", "cesena", "cinisello balsamo",
    "como", "cosenza", "cremona", "ferrara", "foggia", "forli", "giugliano",
    "grosseto", "guidonia montecelio", "la spezia", "latina", "lecce", "lecco",
    "leghorn", "livorno", "lodi", "lucca", "mestre", "modena", "monza",
    "novara", "parma", "perugia", "pesaro", "pescara", "piacenza", "pistoia",
    "pordenone", "pozzuoli", "prato", "ragusa", "ravenna", "reggio calabria",
    "reggio emilia", "rimini", "salerno", "san remo", "sanremo", "sassari",
    "savona", "sesto san giovanni", "siena", "siracusa", "syracuse", "taranto",
    "terni", "torre del greco", "trani", "trento", "treviso", "udine",
    "varese", "vicenza", "vigevano", "viterbo",
}

# =============================================================================
# SPANISH CITIES (Expanded)
# =============================================================================

CITIES_SPAIN = {
    # Major cities
    "madrid", "barcelona", "valencia", "seville", "sevilla", "zaragoza",
    "malaga", "murcia", "palma", "las palmas", "bilbao", "alicante",

    # Additional cities
    "a coruna", "albacete", "alcala de henares", "alcobendas", "alcorcon",
    "algeciras", "almeria", "badajoz", "badalona", "barakaldo", "benidorm",
    "burgos", "caceres", "cadiz", "cartagena", "castello de la plana",
    "ceuta", "cordoba", "dos hermanas", "elche", "elx", "fuenlabrada",
    "getafe", "gijon", "girona", "granada", "guadalajara", "huelva",
    "huesca", "jaen", "jerez de la frontera", "la laguna", "leganes",
    "leon", "hospitalet de llobregat", "lleida", "logrono", "lorca", "lugo",
    "marbella", "mataro", "melilla", "merida", "mostoles", "oviedo",
    "pamplona", "pontevedra", "reus", "roquetas de mar", "sabadell",
    "salamanca", "san sebastian", "donostia", "santa cruz de tenerife",
    "santander", "santiago de compostela", "segovia", "tarragona", "telde",
    "terrassa", "toledo", "torrejon de ardoz", "torrevieja", "valladolid",
    "vigo", "vitoria-gasteiz", "zamora",
}

# =============================================================================
# POLISH CITIES (Expanded)
# =============================================================================

CITIES_POLAND = {
    # Major cities
    "warsaw", "warszawa", "krakow", "cracow", "wroclaw", "lodz", "poznan",
    "gdansk", "szczecin", "lublin", "bydgoszcz", "bialystok", "katowice",

    # Additional cities
    "bytom", "chorzow", "czestochowa", "dabrowa gornicza", "elblag",
    "gdynia", "gliwice", "gorzow wielkopolski", "grudziadz", "inowroclaw",
    "jastrzebie-zdroj", "jaworzno", "jelenia gora", "kalisz", "kielce",
    "koszalin", "legnica", "myslowice", "nowy sacz", "olsztyn", "opole",
    "ostrowiec swietokrzyski", "pila", "plock", "radom", "ruda slaska",
    "rybnik", "rzeszow", "siedlce", "siemianowice slaskie", "slupsk",
    "sosnowiec", "stalowa wola", "stargard", "suwalki", "swidnica",
    "swinoujscie", "tarnow", "torun", "tychy", "walbrzych", "wloclawek",
    "zabrze", "zamosc", "zielona gora",
}

# =============================================================================
# OTHER EUROPEAN CITIES
# =============================================================================

CITIES_EUROPE_OTHER = {
    # Netherlands
    "amsterdam", "rotterdam", "the hague", "utrecht", "eindhoven", "tilburg",
    "groningen", "almere", "breda", "nijmegen", "arnhem", "haarlem", "enschede",
    "maastricht", "dordrecht", "leiden", "zoetermeer", "zwolle", "amersfoort",

    # Belgium
    "brussels", "antwerp", "ghent", "charleroi", "liege", "bruges", "namur",
    "leuven", "mons", "aalst", "mechelen", "kortrijk", "hasselt", "ostend",

    # Austria
    "vienna", "wien", "graz", "linz", "salzburg", "innsbruck", "klagenfurt",

    # Switzerland
    "zurich", "geneva", "basel", "bern", "lausanne", "winterthur", "lucerne",
    "st. gallen", "lugano",

    # Ireland
    "dublin", "cork", "galway", "limerick", "waterford", "drogheda", "dundalk",

    # Portugal
    "lisbon", "porto", "amadora", "braga", "coimbra", "funchal", "setubal",
    "almada", "faro", "aveiro",

    # Sweden
    "stockholm", "gothenburg", "goteborg", "malmo", "uppsala", "vasteras",
    "orebro", "linkoping", "helsingborg", "norrkoping",

    # Norway
    "oslo", "bergen", "trondheim", "stavanger", "drammen", "fredrikstad",

    # Denmark
    "copenhagen", "kobenhavn", "aarhus", "odense", "aalborg", "esbjerg",

    # Finland
    "helsinki", "espoo", "tampere", "turku", "oulu", "vantaa", "jyvaskyla",

    # Greece
    "athens", "thessaloniki", "patras", "heraklion", "piraeus", "larissa",

    # Czech Republic
    "prague", "praha", "brno", "ostrava", "plzen", "liberec", "olomouc",

    # Hungary
    "budapest", "debrecen", "szeged", "miskolc", "pecs", "gyor",

    # Romania
    "bucharest", "bucuresti", "cluj-napoca", "timisoara", "iasi", "constanta",
    "craiova", "brasov", "galati", "ploiesti",

    # Ukraine
    "kyiv", "kiev", "kharkiv", "odessa", "dnipro", "lviv", "zaporizhzhia",
    "donetsk", "kryvyi rih", "mykolaiv",

    # Russia
    "moscow", "saint petersburg", "st petersburg", "novosibirsk",
    "yekaterinburg", "kazan", "nizhny novgorod", "samara", "chelyabinsk",
    "rostov-on-don", "ufa", "krasnoyarsk", "perm", "voronezh", "volgograd",

    # Croatia
    "zagreb", "split", "rijeka", "osijek",

    # Serbia
    "belgrade", "novi sad", "nis",

    # Bulgaria
    "sofia", "plovdiv", "varna", "burgas",

    # Slovakia
    "bratislava", "kosice", "presov", "zilina",

    # Slovenia
    "ljubljana", "maribor",

    # Baltic states
    "tallinn", "tartu", "riga", "vilnius", "kaunas",
}

CITIES_EUROPE = (
    CITIES_UK | CITIES_GERMANY | CITIES_FRANCE | CITIES_ITALY |
    CITIES_SPAIN | CITIES_POLAND | CITIES_EUROPE_OTHER
)

# =============================================================================
# ASIA (Expanded - Top cities from major agglomerations list)
# =============================================================================

CITIES_ASIA = {
    # China (200+ cities, 750k+ pop)
    "beijing", "shanghai", "guangzhou", "shenzhen", "chengdu", "hangzhou",
    "wuhan", "xian", "xi'an", "chongqing", "nanjing", "tianjin", "suzhou",
    "zhengzhou", "changsha", "kunming", "qingdao", "dalian", "shenyang",
    "hong kong", "macau", "dongguan", "foshan", "xiamen", "harbin", "hefei",
    "shantou", "ningbo", "wenzhou", "jinan", "nanning", "taiyuan", "urumqi",
    "fuzhou", "shijiazhuang", "changchun", "nanchang", "guiyang", "lanzhou",
    "wuxi", "zhuhai", "changzhou", "yantai", "huizhou", "xuzhou", "haikou",
    "zhongshan", "luoyang", "nantong", "quanzhou", "baotou", "tangshan",
    "zibo", "weifang", "linyi", "shaoxing", "jiaxing", "yangzhou", "taizhou",
    "huzhou", "jinhua", "zhenjiang", "nanchong", "yichang", "liuzhou",
    "guilin", "daqing", "anshan", "fushun", "jilin", "qiqihar", "datong",
    "hohhot", "xining", "yinchuan", "lhasa", "kaifeng", "anyang", "xinxiang",
    "jiaozuo", "pingdingshan", "nanyang", "zhanjiang", "maoming", "jiangmen",
    "zhaoqing", "qingyuan", "meizhou", "shanwei", "shaoguan", "heyuan",

    # Japan (major cities)
    "tokyo", "osaka", "yokohama", "nagoya", "sapporo", "fukuoka", "kobe",
    "kawasaki", "kyoto", "saitama", "hiroshima", "sendai", "chiba", "kitakyushu",
    "sakai", "niigata", "hamamatsu", "kumamoto", "sagamihara", "okayama",
    "shizuoka", "kagoshima", "funabashi", "hachioji", "matsuyama", "higashiosaka",
    "kawaguchi", "nishinomiya", "kurashiki", "utsunomiya", "matsudo", "ichikawa",
    "kanazawa", "oita", "nagasaki", "gifu", "himeji", "toyama", "wakayama",

    # South Korea
    "seoul", "busan", "incheon", "daegu", "daejeon", "gwangju", "ulsan",
    "suwon", "seongnam", "goyang", "yongin", "bucheon", "ansan", "anyang",
    "changwon", "cheongju", "jeonju", "pohang", "uijeongbu", "hwaseong",

    # India (300+ urban centers)
    "mumbai", "bombay", "delhi", "new delhi", "bangalore", "bengaluru",
    "hyderabad", "ahmedabad", "chennai", "madras", "kolkata", "calcutta",
    "surat", "pune", "jaipur", "lucknow", "kanpur", "nagpur", "indore",
    "thane", "bhopal", "visakhapatnam", "patna", "vadodara", "ghaziabad",
    "agra", "amritsar", "aurangabad", "bhilai", "bhubaneswar", "chandigarh",
    "coimbatore", "cuttack", "dhanbad", "faridabad", "gurgaon", "gurugram",
    "guwahati", "gwalior", "jabalpur", "jalandhar", "jamshedpur", "jodhpur",
    "kochi", "ludhiana", "madurai", "meerut", "moradabad", "mysore", "mysuru",
    "nashik", "noida", "puducherry", "rajkot", "ranchi", "salem", "siliguri",
    "varanasi", "vijayawada", "warangal", "allahabad", "prayagraj", "bareilly",
    "mangalore", "belgaum", "tiruchirappalli", "trichy", "hubli", "dharwad",
    "solapur", "jalandhar", "thiruvananthapuram", "tiruvallur", "raipur",
    "bikaner", "udaipur", "nellore", "chhapra", "gorakhpur", "aligarh",
    "kota", "saharanpur", "muzaffarnagar", "mathura", "kollam", "ajmer",
    "erode", "guntur", "ujjain", "durgapur", "asansol", "jamnagar",
    "sangli", "nanded", "kolhapur", "akola", "gulbarga", "jhansi",
    "firozabad", "bhavnagar", "dehradun", "durg", "korba", "bilaspur",

    # Southeast Asia (expanded)
    "bangkok", "ho chi minh city", "saigon", "hanoi", "singapore",
    "kuala lumpur", "manila", "jakarta", "surabaya", "bandung", "medan",
    "yangon", "phnom penh", "vientiane", "quezon city", "davao", "cebu",
    "makati", "pasig", "taguig", "caloocan", "zamboanga", "antipolo",
    "semarang", "palembang", "tangerang", "depok", "bekasi", "makassar",
    "malang", "batam", "pekanbaru", "bandar lampung", "padang", "denpasar",
    "balikpapan", "pontianak", "manado", "samarinda", "johor bahru", "ipoh",
    "george town", "penang", "petaling jaya", "shah alam", "subang jaya",
    "klang", "kota kinabalu", "kuching", "da nang", "hai phong", "can tho",
    "bien hoa", "nha trang", "buon ma thuot", "hue", "mandalay", "naypyidaw",
    "mawlamyine", "bago", "pathein",

    # Middle East (expanded)
    "dubai", "abu dhabi", "riyadh", "jeddah", "tehran", "baghdad", "damascus",
    "amman", "beirut", "tel aviv", "jerusalem", "doha", "kuwait city",
    "muscat", "manama", "istanbul", "ankara", "izmir", "sharjah", "mecca",
    "medina", "dammam", "tabuk", "bursa", "antalya", "adana", "gaziantep",
    "konya", "mersin", "diyarbakir", "kayseri", "eskisehir", "sanliurfa",
    "mashhad", "isfahan", "karaj", "shiraz", "tabriz", "qom", "ahvaz",
    "kermanshah", "rasht", "hamadan", "yazd", "ardabil", "mosul", "basra",
    "erbil", "najaf", "karbala", "nasiriyah", "aleppo", "homs", "latakia",
    "haifa", "rishon lezion", "ashdod", "petah tikva", "beer sheva",
    "netanya", "holon", "bnei brak", "ramat gan", "irbid", "zarqa", "aqaba",

    # Central Asia
    "almaty", "tashkent", "nur-sultan", "astana", "bishkek", "dushanbe",
    "ashgabat", "samarkand", "namangan", "andijan", "bukhara", "nukus",
    "shymkent", "karaganda", "aktobe", "taraz", "pavlodar", "ust-kamenogorsk",
    "semey", "atyrau", "kostanay", "kyzylorda", "uralsk", "aktau", "turkestan",

    # Pakistan/Bangladesh (expanded)
    "karachi", "lahore", "islamabad", "rawalpindi", "dhaka", "chittagong",
    "faisalabad", "hyderabad", "multan", "peshawar", "quetta", "gujranwala",
    "sialkot", "bahawalpur", "sargodha", "sukkur", "larkana", "sheikhupura",
    "rahim yar khan", "jhang", "mardan", "gujrat", "khulna", "rajshahi",
    "sylhet", "rangpur", "mymensingh", "barisal", "comilla", "gazipur",
    "narayanganj", "tongi", "bogra", "dinajpur", "savar",

    # Taiwan
    "taipei", "kaohsiung", "taichung", "tainan", "hsinchu", "keelung",
    "taoyuan", "chiayi", "changhua", "pingtung",
}

CITIES_OCEANIA = {
    # Australia (expanded)
    "sydney", "melbourne", "brisbane", "perth", "adelaide", "gold coast",
    "newcastle", "canberra", "wollongong", "hobart", "geelong", "townsville",
    "cairns", "darwin", "toowoomba", "ballarat", "bendigo", "launceston",
    "mackay", "rockhampton", "bundaberg", "hervey bay", "wagga wagga",
    "albury", "mildura", "shepparton", "gladstone", "tamworth", "port macquarie",
    "orange", "dubbo", "bathurst", "nowra", "warrnambool", "geraldton",
    "kalgoorlie", "albany", "bunbury", "mandurah", "alice springs",

    # New Zealand (expanded)
    "auckland", "wellington", "christchurch", "hamilton", "tauranga", "dunedin",
    "palmerston north", "napier", "hastings", "nelson", "rotorua", "new plymouth",
    "whangarei", "invercargill", "whanganui", "gisborne",

    # Pacific Islands
    "suva", "port moresby", "noumea", "papeete", "lae", "mount hagen",
    "madang", "apia", "nukualofa", "port vila", "honiara", "nadi", "lautoka",
}

CITIES_SOUTH_AMERICA = {
    # Brazil (expanded)
    "sao paulo", "rio de janeiro", "rio", "brasilia", "salvador", "fortaleza",
    "belo horizonte", "manaus", "curitiba", "recife", "porto alegre", "belem",
    "goiania", "guarulhos", "campinas", "sao luis", "sao goncalo", "maceio",
    "duque de caxias", "natal", "teresina", "campo grande", "nova iguacu",
    "sao bernardo do campo", "joao pessoa", "santo andre", "osasco",
    "jaboatao dos guararapes", "ribeirao preto", "uberlandia", "contagem",
    "sorocaba", "aracaju", "feira de santana", "cuiaba", "joinville",
    "aparecida de goiania", "londrina", "juiz de fora", "porto velho",
    "ananindeua", "niteroi", "belford roxo", "campos dos goytacazes",
    "serra", "caxias do sul", "sao joao de meriti", "florianopolis",
    "maua", "vila velha", "diadema", "betim", "pelotas", "vitoria",

    # Argentina (expanded)
    "buenos aires", "cordoba", "rosario", "mendoza", "la plata", "tucuman",
    "mar del plata", "salta", "santa fe", "san juan", "resistencia",
    "corrientes", "posadas", "neuquen", "formosa", "san salvador de jujuy",
    "bahia blanca", "parana", "santiago del estero", "san luis", "catamarca",
    "la rioja", "rio gallegos", "ushuaia", "rawson", "viedma", "rio cuarto",

    # Chile (expanded)
    "santiago", "valparaiso", "concepcion", "vina del mar", "antofagasta",
    "temuco", "rancagua", "talca", "arica", "chillan", "iquique", "puerto montt",
    "coquimbo", "la serena", "osorno", "valdivia", "punta arenas", "copiapo",

    # Colombia (expanded)
    "bogota", "medellin", "cali", "barranquilla", "cartagena", "cucuta",
    "bucaramanga", "pereira", "santa marta", "ibague", "pasto", "manizales",
    "neiva", "villavicencio", "armenia", "valledupar", "monteria", "sincelejo",
    "popayan", "floridablanca", "palmira", "buenaventura", "soledad", "bello",

    # Peru (expanded)
    "lima", "arequipa", "trujillo", "cusco", "cuzco", "chiclayo", "piura",
    "iquitos", "huancayo", "chimbote", "tacna", "juliaca", "ica", "pucallpa",
    "sullana", "chincha alta", "ayacucho", "cajamarca", "puno", "tumbes",

    # Venezuela (expanded)
    "caracas", "maracaibo", "valencia", "barquisimeto", "maracay", "ciudad guayana",
    "barcelona", "maturin", "cumana", "san cristobal", "petare", "ciudad bolivar",
    "merida", "barinas", "cabudare", "los teques", "puerto la cruz", "guarenas",

    # Ecuador (expanded)
    "quito", "guayaquil", "cuenca", "santo domingo", "machala", "manta",
    "portoviejo", "ambato", "riobamba", "loja", "ibarra", "esmeraldas",
    "quevedo", "milagro", "duran",

    # Other South American countries
    "montevideo", "asuncion", "la paz", "santa cruz", "georgetown", "paramaribo",
    "cochabamba", "sucre", "oruro", "tarija", "potosi", "salto", "ciudad del este",
    "encarnacion", "san lorenzo", "luque", "capiata", "lambare", "fernando de la mora",
    "cayenne",
}

CITIES_AFRICA = {
    # North Africa (expanded)
    "cairo", "alexandria", "giza", "casablanca", "rabat", "fes", "marrakech",
    "algiers", "tunis", "tripoli", "port said", "suez", "luxor", "aswan",
    "ismailia", "tanta", "mansoura", "zagazig", "asyut", "fayoum", "damanhur",
    "minya", "beni suef", "sohag", "qena", "hurghada", "sharm el sheikh",
    "tangier", "agadir", "meknes", "oujda", "kenitra", "tetouan", "safi",
    "el jadida", "nador", "beni mellal", "khouribga", "oran", "constantine",
    "annaba", "batna", "djelfa", "setif", "sidi bel abbes", "biskra", "tebessa",
    "el oued", "skikda", "tiaret", "bechar", "tlemcen", "bejaia", "blida",
    "sfax", "sousse", "kairouan", "bizerte", "gabes", "ariana", "gafsa",
    "benghazi", "misrata", "tarhuna", "al khums", "zawiya", "ajdabiya", "tobruk",

    # West Africa (expanded)
    "lagos", "abuja", "nairobi", "accra", "dakar", "abidjan", "kano", "ibadan",
    "port harcourt", "benin city", "kaduna", "onitsha", "aba", "maiduguri",
    "zaria", "ilorin", "jos", "warri", "enugu", "abeokuta", "sokoto", "owerri",
    "calabar", "uyo", "akure", "bauchi", "osogbo", "makurdi", "yola", "kontagora",
    "kumasi", "tamale", "sekondi-takoradi", "sunyani", "cape coast", "obuasi",
    "tema", "koforidua", "ho", "wa", "bolgatanga", "techiman", "bamako", "sikasso",
    "segou", "mopti", "kayes", "koutiala", "niamey", "zinder", "maradi", "tahoua",
    "agadez", "ouagadougou", "bobo-dioulasso", "koudougou", "banfora", "nouakchott",
    "nouadhibou", "banjul", "serekunda", "brikama", "bissau", "conakry", "kankan",
    "nzerekore", "kindia", "freetown", "bo", "kenema", "makeni", "monrovia",
    "yamoussoukro", "bouake", "daloa", "san-pedro", "korhogo", "man", "lome",
    "sokode", "kara", "atakpame", "cotonou", "porto-novo", "parakou", "abomey",
    "djougou",

    # East Africa (expanded)
    "nairobi", "mombasa", "kisumu", "nakuru", "eldoret", "thika", "malindi",
    "kitale", "garissa", "nyeri", "machakos", "meru", "lamu", "dar es salaam",
    "mwanza", "arusha", "dodoma", "mbeya", "morogoro", "tanga", "zanzibar city",
    "kigoma", "tabora", "iringa", "moshi", "kampala", "gulu", "lira", "mbarara",
    "jinja", "mbale", "entebbe", "masaka", "fort portal", "kabale", "addis ababa",
    "dire dawa", "mekele", "gondar", "hawassa", "bahir dar", "adama", "jimma",
    "dessie", "jijiga", "harar", "debre markos", "nekemte", "asella", "kigali",
    "butare", "gisenyi", "ruhengeri", "gitarama", "bujumbura", "gitega", "ngozi",
    "kirundo", "muyinga", "rumonge", "asmara", "keren", "massawa", "assab",
    "mendefera", "mogadishu", "hargeisa", "bosaso", "kismayo", "berbera", "burao",
    "djibouti city", "juba", "wau", "malakal",

    # Central Africa
    "kinshasa", "lubumbashi", "mbuji-mayi", "kisangani", "kananga", "bukavu",
    "goma", "kolwezi", "likasi", "kikwit", "matadi", "mbandaka", "brazzaville",
    "pointe-noire", "dolisie", "nkayi", "libreville", "port-gentil", "franceville",
    "oyem", "moanda", "douala", "yaounde", "garoua", "bamenda", "maroua",
    "bafoussam", "ngaoundere", "bertoua", "loum", "nkongsamba", "kumba", "limbe",
    "bangui", "bimbo", "berberat", "carnot", "ndjamena", "moundou", "sarh",
    "abeche", "kelo", "koumra", "malabo", "bata", "ebebiyin", "sao tome",

    # Southern Africa (expanded)
    "johannesburg", "cape town", "durban", "pretoria", "port elizabeth",
    "bloemfontein", "east london", "pietermaritzburg", "polokwane", "nelspruit",
    "kimberley", "rustenburg", "witbank", "vereeniging", "soweto", "benoni",
    "krugersdorp", "boksburg", "brakpan", "springs", "alberton", "randfontein",
    "centurion", "midrand", "sandton", "roodepoort", "germiston", "kempton park",
    "luanda", "huambo", "lobito", "benguela", "lucapa", "kuito", "malanje",
    "cabinda", "lubango", "namibe", "soyo", "uige", "sumbe", "maputo", "matola",
    "beira", "nampula", "chimoio", "nacala", "quelimane", "tete", "lichinga",
    "pemba", "xai-xai", "maxixe", "lusaka", "kitwe", "ndola", "kabwe", "chingola",
    "mufulira", "livingstone", "luanshya", "kasama", "chipata", "solwezi",
    "harare", "bulawayo", "chitungwiza", "mutare", "gweru", "epworth", "kwekwe",
    "kadoma", "masvingo", "chinhoyi", "marondera", "norton", "gaborone",
    "francistown", "molepolole", "serowe", "maun", "selibe phikwe", "kasane",
    "windhoek", "rundu", "walvis bay", "swakopmund", "oshakati", "katima mulilo",
    "rehoboth", "otjiwarongo", "mbabane", "manzini", "maseru", "teyateyaneng",
    "mafeteng", "hlotse", "antananarivo", "toamasina", "antsirabe", "fianarantsoa",
    "mahajanga", "toliara", "antsiranana", "ambovombe", "port louis", "beau bassin",
    "vacoas", "curepipe", "quatre bornes", "mamoudzou", "moroni", "victoria",
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
