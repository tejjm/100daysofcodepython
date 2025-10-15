import requests
from datetime import datetime
TOKEN = "fbjldsbgdbfdfa"
USER_NAME = "uttej"
GRAPH_ID = "japaneselearning"
dt = datetime(year=2025,month=10,day=14) #Use datetime.today()
DATE = dt.strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {"token" : TOKEN,
              "username" : USER_NAME,
              "agreeTermsOfService" : "yes",
              "notMinor" : "yes"}
# response = requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
graph_params = {
  "id": GRAPH_ID,
  "name": "Japanese Study Hours",
  "unit": "hours",
  "type": "float",
  "color": "ajisai",
  "timezone": "Asia/Kolkata"
}
header = {"X-USER-TOKEN":TOKEN}
# response = requests.post(url=graph_endpoint,json=graph_params,headers=header)
# print(response.text)
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
post_params = {"date":DATE,
               "quantity":input("How many hours did you study Japanese today?")}
# response = requests.post(url=post_endpoint,json=post_params,headers=header)
# print(response.text)
put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
put_params = {"quantity":input("How many hours did you study Japanese today?")}
# response = requests.put(url=put_endpoint,json=put_params,headers=header)
# print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
response = requests.delete(url=delete_endpoint,headers=header)
print(response.text)