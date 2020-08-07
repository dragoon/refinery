import requests

from refinery.environ import API_URL, HOME_LATITUDE, HOME_LONGITUDE

UVI_URL = f"https://{API_URL}/v1/weather/uvi?lat={HOME_LATITUDE}&lon={HOME_LONGITUDE}"


def get_current_uv_index() -> float:
    result = requests.get(UVI_URL).json()
    return result[0]['value']
