from datetime import datetime
import requests

PIXELA_URL = "https://pixe.la/v1"

# Create User
user_data = {
    "token": "O&MfvGqt1@FhZHr",
    "username": "dev4venera",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# r = requests.post(f"{PIXELA_URL}/users", json=user_data)
# r.raise_for_status()
# print(r.text)


# Create Graph
graph_data = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": "O&MfvGqt1@FhZHr"}

# r = requests.post(
#     f"{PIXELA_URL}/users/{user_data['username']}/graphs",
#     headers=headers,
#     json=graph_data,
# )
# r.raise_for_status()
# print(r.status_code)
# print(r.text)

# Post Data
# today = datetime.now()
# value_data = {"date": today.strftime("%Y%m%d"), "quantity": "10.01"}
# r = requests.post(
#     f"{PIXELA_URL}/users/{user_data['username']}/graphs/{graph_data['id']}",
#     headers=headers,
#     json=value_data,
# )
# r.raise_for_status()
# print(r.text)

# Update Data
# date = datetime(2022, 9, 30)
# update_data = {"quantity": "6.4"}
# r = requests.put(
#     f"{PIXELA_URL}/users/{user_data['username']}/graphs/{graph_data['id']}/{date.strftime('%Y%m%d')}",
#     headers=headers,
#     json=update_data,
# )
# r.raise_for_status()
# print(r.text)

# Delete Data
# date = datetime(2022, 9, 30)
# r = requests.delete(
#     f"{PIXELA_URL}/users/{user_data['username']}/graphs/{graph_data['id']}/{date.strftime('%Y%m%d')}",
#     headers=headers,
# )
# r.raise_for_status()
# print(r.text)

# Get Graph SVG
# params = {"mode": "short"}
r = requests.get(
    f"{PIXELA_URL}/users/{user_data['username']}/graphs/{graph_data['id']}",
    # params=params,
)
r.raise_for_status()
with open("graph.html", "w") as graph_file:
    graph_file.write(r.text)
