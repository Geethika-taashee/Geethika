#successfull conection request
# import requests
# r=requests.get("http://www.google.com")
# print(r.status_code)



#exception handling for http errors
# import requests 
# url = "https://www.amazon.com/nothing_here"
# try: 
# 	r = requests.get(url, timeout=1) 
# 	r.raise_for_status() 
# except requests.exceptions.HTTPError as errh: 
# 	print("HTTP Error") 
# 	print(errh.args[0]) 
# print(r.status_code) 



#general exception handling
# import requests
# url = "https://www.google.com"
# try: 
# 	r = requests.get(url, timeout=1) 
# 	r.raise_for_status() 
# except requests.exceptions.RequestException as errex: 
# 	print("Exception request") 



#timeout exception
# import requests 
# url = "https://www.google.com"
# try: 
# 	r = requests.get(url, timeout=1) 
# 	r.raise_for_status() 
# except requests.exceptions.ReadTimeout as errrt: 
# 	print("Time out") 
# print(r.status_code) 



#exception handling for missing schema
# import requests
# url = "www.google.com"
# try:
#     r=requests.get(url, timeout=1)
#     r.raise_for_status()
# except requests.exceptions.MissingSchema as errmiss:
#     print("MissingSchema:include hhtp or https")
# except requests.exceptions.ReadTimeout as errrt:
#     print("Time out")



#exception handling for connection error
# import requests
# url="https://www.amazon.co"
# try:
#     r=requests.get(url, timeout=1, verify=True)
#     r.raise_for_status()
# except requests.exceptions.HTTPError as errh:
#     print("HTTP Error")
#     print(errh.args[0])
# except requests.exceptions.ReadTimeout as errrt:
#     print("Time out")
# except requests.exceptions.ConnectionError as conerr:
#     print("Connection error")
