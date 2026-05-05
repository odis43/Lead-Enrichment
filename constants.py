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

CENSUS_BASE_URL = "https://api.census.gov/data/2022/acs/acs5"

CENSUS_VARIABLES = "B25003_001E,B25003_002E,B25001_001E,B19013_001E"

WALKSCORE_BASE_URL = "https://api.walkscore.com/score"


CENSUS_TOTAL_OCCUPIED_UNITS = "B25003_001E"
CENSUS_RENTER_OCCUPIED_UNITS = "B25003_002E"
CENSUS_TOTAL_HOUSING_UNITS = "B25001_001E"
CENSUS_MEDIAN_HOUSEHOLD_INCOME = "B19013_001E"
CENSUS_VARIABLES = f"{CENSUS_TOTAL_OCCUPIED_UNITS},{CENSUS_RENTER_OCCUPIED_UNITS},{CENSUS_TOTAL_HOUSING_UNITS},{CENSUS_MEDIAN_HOUSEHOLD_INCOME}"
