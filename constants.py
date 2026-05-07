STATE_FIPS = {
    "AL": "01", "AK": "02", "AZ": "04", "AR": "05", "CA": "06",
    "CO": "08", "CT": "09", "DE": "10", "FL": "12", "GA": "13",
    "HI": "15", "ID": "16", "IL": "17", "IN": "18", "IA": "19",
    "KS": "20", "KY": "21", "LA": "22", "ME": "23", "MD": "24",
    "MA": "25", "MI": "26", "MN": "27", "MS": "28", "MO": "29",
    "MT": "30", "NE": "31", "NV": "32", "NH": "33", "NJ": "34",
    "NM": "35", "NY": "36", "NC": "37", "ND": "38", "OH": "39",
    "OK": "40", "OR": "41", "PA": "42", "RI": "44", "SC": "45",
    "SD": "46", "TN": "47", "TX": "48", "UT": "49", "VT": "50",
    "VA": "51", "WA": "53", "WV": "54", "WI": "55", "WY": "56",
    "DC": "11"
}

WEIGHTS = {
    "renter_pct":       0.30,   # is this a renter market?
    "vacancy_rate":     0.25,   # is it actively turning over?
    "housing_units":    0.20,   # is the market big enough?
    "review_count":     0.15,   # how large is the specific property?
}

CENSUS_BASE_URL = "https://api.census.gov/data/2022/acs/acs5"

CENSUS_VARIABLES = "B25003_001E,B25003_002E,B25001_001E,B19013_001E"

WALKSCORE_BASE_URL = "https://api.walkscore.com/score"

SCORE_SENTIMENT = {}

CENSUS_TOTAL_OCCUPIED_UNITS = "B25003_001E"
CENSUS_RENTER_OCCUPIED_UNITS = "B25003_002E"
CENSUS_TOTAL_HOUSING_UNITS = "B25001_001E"
CENSUS_MEDIAN_HOUSEHOLD_INCOME = "B19013_001E"
CENSUS_VARIABLES = f"{CENSUS_TOTAL_OCCUPIED_UNITS},{CENSUS_RENTER_OCCUPIED_UNITS},{CENSUS_TOTAL_HOUSING_UNITS},{CENSUS_MEDIAN_HOUSEHOLD_INCOME}"


FRED_BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

STATE_VACANCY_SERIES = {
    "AL": "ALRVAC", "AK": "AKRVAC", "AZ": "AZRVAC", "AR": "ARRVAC",
    "CA": "CARVAC", "CO": "CORVAC", "CT": "CTRVAC", "DE": "DERVAC",
    "FL": "FLRVAC", "GA": "GARVAC", "HI": "HIRVAC", "ID": "IDRVAC",
    "IL": "ILRVAC", "IN": "INRVAC", "IA": "IARVAC", "KS": "KSRVAC",
    "KY": "KYRVAC", "LA": "LARVAC", "ME": "MERVAC", "MD": "MDRVAC",
    "MA": "MARVAC", "MI": "MIRVAC", "MN": "MNRVAC", "MS": "MSRVAC",
    "MO": "MORVAC", "MT": "MTRVAC", "NE": "NERVAC", "NV": "NVRVAC",
    "NH": "NHRVAC", "NJ": "NJRVAC", "NM": "NMRVAC", "NY": "NYRVAC",
    "NC": "NCRVAC", "ND": "NDRVAC", "OH": "OHRVAC", "OK": "OKRVAC",
    "OR": "ORRVAC", "PA": "PARVAC", "RI": "RIRVAC", "SC": "SCRVAC",
    "SD": "SDRVAC", "TN": "TNRVAC", "TX": "TXRVAC", "UT": "UTRVAC",
    "VT": "VTRVAC", "VA": "VARVAC", "WA": "WARVAC", "WV": "WVRVAC",
    "WI": "WIRVAC", "WY": "WYRVAC", "DC": "DCRVAC"
}

PLACES_URL = "https://places.googleapis.com/v1/places:searchText"

WRITE_FIELDS = (
    "Renter Percentage",
    "Housing Units",
    "Rental Vacancy Rate",
    "Property Name",
    "Property Rating",
    "Property Review Count",
    "Property Business Status",
    "Score",
    "Priority",
    "Score Reasoning",
    "Draft Email",
    "Status",
)
