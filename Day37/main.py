import requests
from datetime import datetime

today = datetime.now()
FIRST_GRAPH_ID = "graph1"
date = today.strftime("%Y%m%d")
USERNAME = "omerfarukyilmaz"
TOKEN = "G9ljT3uit36bt7HRu3kn"
headers = {
    "X-USER-TOKEN": TOKEN
}
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": FIRST_GRAPH_ID,
    "name": "Mourning Routine",
    "unit": "commit",
    "type": "int",
    "color": "sora"

}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{FIRST_GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",

}

# response = requests.post(url=graph_update_endpoint, json=pixel_config, headers=headers)
# print(response.text)

new_pixel_data = {
    "quantity": "1"
}

graph_deleting_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{FIRST_GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.put(url=graph_deleting_update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
