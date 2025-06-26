from pydantic import BaseModel
from enum import Enum


class Currency(BaseModel):
    currency_code: str
    name: str
    symbol: str
    country_code: str
    country_name: str


class CurrencyCode(str, Enum):
    ONE_INCH = "1inch"
    AAVE = "aave"
    ADA = "ada"
    AED = "aed"
    AFN = "afn"
    AGIX = "agix"
    AKT = "akt"
    ALGO = "algo"
    ALL = "all"
    AMD = "amd"
    AMP = "amp"
    ANG = "ang"
    AOA = "aoa"
    APE = "ape"
    APT = "apt"
    AR = "ar"
    ARB = "arb"
    ARS = "ars"
    ATOM = "atom"
    ATS = "ats"
    AUD = "aud"
    AVAX = "avax"
    AWG = "awg"
    AXS = "axs"
    AZM = "azm"
    AZN = "azn"
    BAKE = "bake"
    BAM = "bam"
    BAT = "bat"
    BBD = "bbd"
    BCH = "bch"
    BDT = "bdt"
    BEF = "bef"
    BGN = "bgn"
    BHD = "bhd"
    BIF = "bif"
    BMD = "bmd"
    BNB = "bnb"
    BND = "bnd"
    BOB = "bob"
    BRL = "brl"
    BSD = "bsd"
    BSV = "bsv"
    BSW = "bsw"
    BTC = "btc"
    BTG = "btg"
    BTN = "btn"
    BTT = "btt"
    BUSD = "busd"
    BWP = "bwp"
    BYN = "byn"
    BYR = "byr"
    BZD = "bzd"
    CAD = "cad"
    CAKE = "cake"
    CDF = "cdf"
    CELO = "celo"
    CFX = "cfx"
    CHF = "chf"
    CHZ = "chz"
    CLP = "clp"
    CNH = "cnh"
    CNY = "cny"
    COMP = "comp"
    COP = "cop"
    CRC = "crc"
    CRO = "cro"
    CRV = "crv"
    CSPR = "cspr"
    CUC = "cuc"
    CUP = "cup"
    CVE = "cve"
    CVX = "cvx"
    CYP = "cyp"
    CZK = "czk"
    DAI = "dai"
    DASH = "dash"
    DCR = "dcr"
    DEM = "dem"
    DFI = "dfi"
    DJF = "djf"
    DKK = "dkk"
    DOGE = "doge"
    DOP = "dop"
    DOT = "dot"
    DYDX = "dydx"
    DZD = "dzd"
    EEK = "eek"
    EGLD = "egld"
    EGP = "egp"
    ENJ = "enj"
    EOS = "eos"
    ERN = "ern"
    ESP = "esp"
    ETB = "etb"
    ETC = "etc"
    ETH = "eth"
    EUR = "eur"
    FEI = "fei"
    FIL = "fil"
    FIM = "fim"
    FJD = "fjd"
    FKP = "fkp"
    FLOW = "flow"
    FLR = "flr"
    FRAX = "frax"
    FRF = "frf"
    FTT = "ftt"
    GALA = "gala"
    GBP = "gbp"
    GEL = "gel"
    GGP = "ggp"
    GHC = "ghc"
    GHS = "ghs"
    GIP = "gip"
    GMD = "gmd"
    GMX = "gmx"
    GNF = "gnf"
    GNO = "gno"
    GRD = "grd"
    GRT = "grt"
    GT = "gt"
    GTQ = "gtq"
    GUSD = "gusd"
    GYD = "gyd"
    HBAR = "hbar"
    HKD = "hkd"
    HNL = "hnl"
    HNT = "hnt"
    HOT = "hot"
    HRK = "hrk"
    HT = "ht"
    HTG = "htg"
    HUF = "huf"
    ICP = "icp"
    IDR = "idr"
    IEP = "iep"
    ILS = "ils"
    IMP = "imp"
    IMX = "imx"
    INJ = "inj"
    INR = "inr"
    IQD = "iqd"
    IRR = "irr"
    ISK = "isk"
    ITL = "itl"
    JEP = "jep"
    JMD = "jmd"
    JOD = "jod"
    JPY = "jpy"
    KAS = "kas"
    KAVA = "kava"
    KCS = "kcs"
    KDA = "kda"
    KES = "kes"
    KGS = "kgs"
    KHR = "khr"
    KLAY = "klay"
    KMF = "kmf"
    KNC = "knc"
    KPW = "kpw"
    KRW = "krw"
    KSM = "ksm"
    KWD = "kwd"
    KYD = "kyd"
    KZT = "kzt"
    LAK = "lak"
    LBP = "lbp"
    LDO = "ldo"
    LEO = "leo"
    LINK = "link"
    LKR = "lkr"
    LRC = "lrc"
    LRD = "lrd"
    LSL = "lsl"
    LTC = "ltc"
    LTL = "ltl"
    LUF = "luf"
    LUNA = "luna"
    LUNC = "lunc"
    LVL = "lvl"
    LYD = "lyd"
    MAD = "mad"
    MANA = "mana"
    MBX = "mbx"
    MDL = "mdl"
    MGA = "mga"
    MGF = "mgf"
    MINA = "mina"
    MKD = "mkd"
    MKR = "mkr"
    MMK = "mmk"
    MNT = "mnt"
    MOP = "mop"
    MRO = "mro"
    MRU = "mru"
    MTL = "mtl"
    MUR = "mur"
    MVR = "mvr"
    MWK = "mwk"
    MXN = "mxn"
    MXV = "mxv"
    MYR = "myr"
    MZM = "mzm"
    MZN = "mzn"
    NAD = "nad"
    NEAR = "near"
    NEO = "neo"
    NEXO = "nexo"
    NFT = "nft"
    NGN = "ngn"
    NIO = "nio"
    NLG = "nlg"
    NOK = "nok"
    NPR = "npr"
    NZD = "nzd"
    OKB = "okb"
    OMR = "omr"
    ONE = "one"
    OP = "op"
    ORDI = "ordi"
    PAB = "pab"
    PAXG = "paxg"
    PEN = "pen"
    PEPE = "pepe"
    PGK = "pgk"
    PHP = "php"
    PKR = "pkr"
    PLN = "pln"
    PTE = "pte"
    PYG = "pyg"
    QAR = "qar"
    QNT = "qnt"
    QTUM = "qtum"
    ROL = "rol"
    RON = "ron"
    RPL = "rpl"
    RSD = "rsd"
    RUB = "rub"
    RUNE = "rune"
    RVN = "rvn"
    RWF = "rwf"
    SAND = "sand"
    SAR = "sar"
    SBD = "sbd"
    SCR = "scr"
    SDD = "sdd"
    SDG = "sdg"
    SEK = "sek"
    SGD = "sgd"
    SHIB = "shib"
    SHP = "shp"
    SIT = "sit"
    SKK = "skk"
    SLE = "sle"
    SLL = "sll"
    SNX = "snx"
    SOL = "sol"
    SOS = "sos"
    SPL = "spl"
    SRD = "srd"
    SRG = "srg"
    STD = "std"
    STN = "stn"
    STX = "stx"
    SUI = "sui"
    SVC = "svc"
    SYP = "syp"
    SZL = "szl"
    THB = "thb"
    THETA = "theta"
    TJS = "tjs"
    TMM = "tmm"
    TMT = "tmt"
    TND = "tnd"
    TON = "ton"
    TOP = "top"
    TRL = "trl"
    TRX = "trx"
    TRY_ = "try"  # 'try' is a reserved word, hence the underscore suffix
    TTD = "ttd"
    TUSD = "tusd"
    TVD = "tvd"
    TWD = "twd"
    TWT = "twt"
    TZS = "tzs"
    UAH = "uah"
    UGX = "ugx"
    UNI = "uni"
    USD = "usd"
    USDC = "usdc"
    USDD = "usdd"
    USDP = "usdp"
    USDT = "usdt"
    UYU = "uyu"
    UZS = "uzs"
    VAL = "val"
    VEB = "veb"
    VED = "ved"
    VEF = "vef"
    VES = "ves"
    VET = "vet"
    VND = "vnd"
    VUV = "vuv"
    WAVES = "waves"
    WEMIX = "wemix"
    WOO = "woo"
    WST = "wst"
    XAF = "xaf"
    XAG = "xag"
    XAU = "xau"
    XAUT = "xaut"
    XBT = "xbt"
    XCD = "xcd"
    XCG = "xcg"
    XCH = "xch"
    XDC = "xdc"
    XDR = "xdr"
    XEC = "xec"
    XEM = "xem"
    XLM = "xlm"
    XMR = "xmr"
    XOF = "xof"
    XPD = "xpd"
    XPF = "xpf"
    XPT = "xpt"
    XRP = "xrp"
    XTZ = "xtz"
    YER = "yer"
    ZAR = "zar"
    ZEC = "zec"
    ZIL = "zil"
    ZMK = "zmk"
    ZMW = "zmw"
    ZWD = "zwd"
    ZWG = "zwg"
    ZWL = "zwl"

    def __str__(self):
        return "{}({})".format(self.full_name, self.symbol)

    @property
    def symbol(self):
        return self.value.upper()

    @property
    def full_name(self):
        currency_codes = {
            "1inch": "1inch",
            "aave": "Aave",
            "ada": "Cardano",
            "aed": "Emirati Dirham",
            "afn": "Afghan Afghani",
            "agix": "SingularityNET",
            "akt": "Akash Network",
            "algo": "Algorand",
            "all": "Albanian Lek",
            "amd": "Armenian Dram",
            "amp": "Amp",
            "ang": "Dutch Guilder",
            "aoa": "Angolan Kwanza",
            "ape": "ApeCoin",
            "apt": "Aptos",
            "ar": "Arweave",
            "arb": "Arbitrum",
            "ars": "Argentine Peso",
            "atom": "Cosmos",
            "ats": "Austrian Schilling",
            "aud": "Australian Dollar",
            "avax": "Avalanche",
            "awg": "Aruban or Dutch Guilder",
            "axs": "Axie Infinity",
            "azm": "Azerbaijani Manat",
            "azn": "Azerbaijan Manat",
            "bake": "BakeryToken",
            "bam": "Bosnian Convertible Mark",
            "bat": "Basic Attention Token",
            "bbd": "Barbadian or Bajan Dollar",
            "bch": "Bitcoin Cash",
            "bdt": "Bangladeshi Taka",
            "bef": "Belgian Franc",
            "bgn": "Bulgarian Lev",
            "bhd": "Bahraini Dinar",
            "bif": "Burundian Franc",
            "bmd": "Bermudian Dollar",
            "bnb": "Binance Coin",
            "bnd": "Bruneian Dollar",
            "bob": "Bolivian Bolíviano",
            "brl": "Brazilian Real",
            "bsd": "Bahamian Dollar",
            "bsv": "Bitcoin SV",
            "bsw": "Biswap",
            "btc": "Bitcoin",
            "btg": "Bitcoin Gold",
            "btn": "Bhutanese Ngultrum",
            "btt": "BitTorrent",
            "busd": "Binance USD",
            "bwp": "Botswana Pula",
            "byn": "Belarusian Ruble",
            "byr": "Belarusian Ruble",
            "bzd": "Belizean Dollar",
            "cad": "Canadian Dollar",
            "cake": "PancakeSwap",
            "cdf": "Congolese Franc",
            "celo": "Celo",
            "cfx": "Conflux",
            "chf": "Swiss Franc",
            "chz": "Chiliz",
            "clp": "Chilean Peso",
            "cnh": "Chinese Yuan Renminbi Offshore",
            "cny": "Chinese Yuan Renminbi",
            "comp": "Compound",
            "cop": "Colombian Peso",
            "crc": "Costa Rican Colon",
            "cro": "Crypto.com Chain",
            "crv": "Curve DAO Token",
            "cspr": "Casper",
            "cuc": "Cuban Convertible Peso",
            "cup": "Cuban Peso",
            "cve": "Cape Verdean Escudo",
            "cvx": "Convex Finance",
            "cyp": "Cypriot Pound",
            "czk": "Czech Koruna",
            "dai": "DAI",
            "dash": "Digital Cash",
            "dcr": "Decred",
            "dem": "German Deutsche Mark",
            "dfi": "DfiStarter",
            "djf": "Djiboutian Franc",
            "dkk": "Danish Krone",
            "doge": "Dogecoin",
            "dop": "Dominican Peso",
            "dot": "Polkadot",
            "dydx": "dYdX",
            "dzd": "Algerian Dinar",
            "eek": "Estonian Kroon",
            "egld": "Elrond",
            "egp": "Egyptian Pound",
            "enj": "Enjin Coin",
            "eos": "EOS",
            "ern": "Eritrean Nakfa",
            "esp": "Spanish Peseta",
            "etb": "Ethiopian Birr",
            "etc": "Ethereum Classic",
            "eth": "Ethereum",
            "eur": "Euro",
            "fei": "Fei USD",
            "fil": "Filecoin",
            "fim": "Finnish Markka",
            "fjd": "Fijian Dollar",
            "fkp": "Falkland Island Pound",
            "flow": "Flow",
            "flr": "FLARE",
            "frax": "Frax",
            "frf": "French Franc",
            "ftt": "FarmaTrust",
            "gala": "Gala",
            "gbp": "British Pound",
            "gel": "Georgian Lari",
            "ggp": "Guernsey Pound",
            "ghc": "Ghanaian Cedi",
            "ghs": "Ghanaian Cedi",
            "gip": "Gibraltar Pound",
            "gmd": "Gambian Dalasi",
            "gmx": "Goldmaxcoin",
            "gnf": "Guinean Franc",
            "gno": "Gnosis",
            "grd": "Greek Drachma",
            "grt": "The Graph",
            "gt": "GateToken",
            "gtq": "Guatemalan Quetzal",
            "gusd": "Gemini US Dollar",
            "gyd": "Guyanese Dollar",
            "hbar": "Hedera",
            "hkd": "Hong Kong Dollar",
            "hnl": "Honduran Lempira",
            "hnt": "Helium",
            "hot": "Hydro Protocol",
            "hrk": "Croatian Kuna",
            "ht": "Huobi Token",
            "htg": "Haitian Gourde",
            "huf": "Hungarian Forint",
            "icp": "Internet Computer",
            "idr": "Indonesian Rupiah",
            "iep": "Irish Pound",
            "ils": "Israeli Shekel",
            "imp": "Isle of Man Pound",
            "imx": "Immutable X",
            "inj": "Injective",
            "inr": "Indian Rupee",
            "iqd": "Iraqi Dinar",
            "irr": "Iranian Rial",
            "isk": "Icelandic Krona",
            "itl": "Italian Lira",
            "jep": "Jersey Pound",
            "jmd": "Jamaican Dollar",
            "jod": "Jordanian Dinar",
            "jpy": "Japanese Yen",
            "kas": "",
            "kava": "Kava",
            "kcs": "Kucoin",
            "kda": "Kadena",
            "kes": "Kenyan Shilling",
            "kgs": "Kyrgyzstani Som",
            "khr": "Cambodian Riel",
            "klay": "Klaytn",
            "kmf": "Comorian Franc",
            "knc": "Kyber Network Crystals",
            "kpw": "North Korean Won",
            "krw": "South Korean Won",
            "ksm": "Kusama",
            "kwd": "Kuwaiti Dinar",
            "kyd": "Caymanian Dollar",
            "kzt": "Kazakhstani Tenge",
            "lak": "Lao Kip",
            "lbp": "Lebanese Pound",
            "ldo": "Lido DAO Token",
            "leo": "LEOcoin",
            "link": "Chainlink",
            "lkr": "Sri Lankan Rupee",
            "lrc": "Loopring",
            "lrd": "Liberian Dollar",
            "lsl": "Basotho Loti",
            "ltc": "Litecoin",
            "ltl": "Lithuanian Litas",
            "luf": "Luxembourg Franc",
            "luna": "Terra",
            "lunc": "",
            "lvl": "Latvian Lat",
            "lyd": "Libyan Dinar",
            "mad": "Moroccan Dirham",
            "mana": "Mana Coin Decentraland",
            "mbx": "MobieCoin",
            "mdl": "Moldovan Leu",
            "mga": "Malagasy Ariary",
            "mgf": "Malagasy Franc",
            "mina": "Mina",
            "mkd": "Macedonian Denar",
            "mkr": "Maker",
            "mmk": "Burmese Kyat",
            "mnt": "Mongolian Tughrik",
            "mop": "Macau Pataca",
            "mro": "Mauritanian Ouguiya",
            "mru": "Mauritanian Ouguiya",
            "mtl": "Maltese Lira",
            "mur": "Mauritian Rupee",
            "mvr": "Maldivian Rufiyaa",
            "mwk": "Malawian Kwacha",
            "mxn": "Mexican Peso",
            "mxv": "",
            "myr": "Malaysian Ringgit",
            "mzm": "Mozambican Metical",
            "mzn": "Mozambican Metical",
            "nad": "Namibian Dollar",
            "near": "NEAR Protocol",
            "neo": "NEO",
            "nexo": "NEXO",
            "nft": "NFT",
            "ngn": "Nigerian Naira",
            "nio": "Nicaraguan Cordoba",
            "nlg": "Dutch Guilder",
            "nok": "Norwegian Krone",
            "npr": "Nepalese Rupee",
            "nzd": "New Zealand Dollar",
            "okb": "Okex",
            "omr": "Omani Rial",
            "one": "Menlo One",
            "op": "Optimism",
            "ordi": "",
            "pab": "Panamanian Balboa",
            "paxg": "PAX Gold",
            "pen": "Peruvian Sol",
            "pepe": "",
            "pgk": "Papua New Guinean Kina",
            "php": "Philippine Peso",
            "pkr": "Pakistani Rupee",
            "pln": "Polish Zloty",
            "pte": "Portuguese Escudo",
            "pyg": "Paraguayan Guarani",
            "qar": "Qatari Riyal",
            "qnt": "Quant",
            "qtum": "QTUM",
            "rol": "Romanian Leu",
            "ron": "Romanian Leu",
            "rpl": "Rocket Pool",
            "rsd": "Serbian Dinar",
            "rub": "Russian Ruble",
            "rune": "THORChain (ERC20)",
            "rvn": "Ravencoin",
            "rwf": "Rwandan Franc",
            "sand": "The Sandbox",
            "sar": "Saudi Arabian Riyal",
            "sbd": "Solomon Islander Dollar",
            "scr": "Seychellois Rupee",
            "sdd": "Sudanese Dinar",
            "sdg": "Sudanese Pound",
            "sek": "Swedish Krona",
            "sgd": "Singapore Dollar",
            "shib": "Shiba Inu",
            "shp": "Saint Helenian Pound",
            "sit": "Slovenian Tolar",
            "skk": "Slovak Koruna",
            "sle": "Sierra Leonean Leone",
            "sll": "Sierra Leonean Leone",
            "snx": "Synthetix Network",
            "sol": "Solana",
            "sos": "Somali Shilling",
            "spl": "Seborgan Luigino",
            "srd": "Surinamese Dollar",
            "srg": "Surinamese Guilder",
            "std": "Sao Tomean Dobra",
            "stn": "Sao Tomean Dobra",
            "stx": "Stacks",
            "sui": "Sui",
            "svc": "Salvadoran Colon",
            "syp": "Syrian Pound",
            "szl": "Swazi Lilangeni",
            "thb": "Thai Baht",
            "theta": "Theta",
            "tjs": "Tajikistani Somoni",
            "tmm": "Turkmenistani Manat",
            "tmt": "Turkmenistani Manat",
            "tnd": "Tunisian Dinar",
            "ton": "Tokamak Network",
            "top": "Tongan Pa'anga",
            "trl": "",
            "trx": "TRON",
            "try": "Turkish Lira",
            "ttd": "Trinidadian Dollar",
            "tusd": "True USD",
            "tvd": "Tuvaluan Dollar",
            "twd": "Taiwan New Dollar",
            "twt": "Trust Wallet Token",
            "tzs": "Tanzanian Shilling",
            "uah": "Ukrainian Hryvnia",
            "ugx": "Ugandan Shilling",
            "uni": "Uniswap",
            "usd": "US Dollar",
            "usdc": "USDC",
            "usdd": "",
            "usdp": "USDP Stablecoin",
            "usdt": "Tether",
            "uyu": "Uruguayan Peso",
            "uzs": "Uzbekistani Som",
            "val": "Vatican City Lira",
            "veb": "Venezuelan Bolívar",
            "ved": "",
            "vef": "Venezuelan Bolívar",
            "ves": "Venezuelan Bolívar",
            "vet": "Vechain",
            "vnd": "Vietnamese Dong",
            "vuv": "Ni-Vanuatu Vatu",
            "waves": "Waves",
            "wemix": "WEMIX",
            "woo": "WOO Network",
            "wst": "Samoan Tala",
            "xaf": "Central African CFA Franc BEAC",
            "xag": "Silver Ounce",
            "xau": "Gold Ounce",
            "xaut": "Tether Gold",
            "xbt": "",
            "xcd": "East Caribbean Dollar",
            "xcg": "Xchange",
            "xch": "Chia",
            "xdc": "XDC Network",
            "xdr": "IMF Special Drawing Rights",
            "xec": "Eternal Coin",
            "xem": "NEM",
            "xlm": "Stellar Lumen",
            "xmr": "Monero",
            "xof": "CFA Franc",
            "xpd": "Palladium Ounce",
            "xpf": "CFP Franc",
            "xpt": "Platinum Ounce",
            "xrp": "Ripple",
            "xtz": "Tezos",
            "yer": "Yemeni Rial",
            "zar": "South African Rand",
            "zec": "ZCash",
            "zil": "Zilliqa",
            "zmk": "Zambian Kwacha",
            "zmw": "Zambian Kwacha",
            "zwd": "Zimbabwean Dollar",
            "zwg": "",
            "zwl": "Zimbabwean Dollar",
        }
        return currency_codes[self.value]
