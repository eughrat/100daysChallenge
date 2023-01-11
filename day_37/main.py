import requests
from datetime import datetime


TOKEN = "12345678"
USERNAME = "eughrat"
today = datetime.today()
some_day = datetime(year=2023, month=1,day=10)
today_formated = today.strftime("%Y%m%d")

################################################################################

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

################################################################################

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

################################################################################

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

pixel_params = {
    "date": some_day.strftime("%Y%m%d"),
    "quantity": "12.0",
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

################################################################################

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today_formated}"

pixel_put_params = {
    "quantity": "20",
}

# response = requests.put(url=pixel_put_endpoint, json=pixel_put_params, headers=headers)
# print(response.text)

################################################################################

pixel_del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today_formated}"

# response = requests.delete(url=pixel_del_endpoint, headers=headers)
# print(response.text)