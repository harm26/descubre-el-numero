'''-> branch: tarea_1_conectarse_a_una_api
-> task:
    leer la documentacion de esta api http://www.omdbapi.com

    '''

import requests

url = "http://www.omdbapi.com"
response= requests.get(url)

if response.status_code==200:
      print(response.content)

else:
      print("error")
