import requests

from refinery.domain.uv_index import UVIndex
from refinery.environ import API_URL, HOME_LATITUDE, HOME_LONGITUDE, API_KEY

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "dashboard25.p.rapidapi.com"
}
querystring = {"lat": HOME_LATITUDE, "lon": HOME_LONGITUDE}


def get_current_uv_index() -> UVIndex:
    result = requests.request("GET", API_URL, headers=headers, params=querystring).json()
    return UVIndex(result['uv'])
