import requests
from concurrent.futures import ThreadPoolExecutor

headers = {'Content-Type': 'application/json', "action":"bypass","clientCountryName":"HK",
"clientIP":"112.120.208.54","clientRefererHost":"xxx","clientRefererPath":"xxx","datetime":"2022-01-18T16:11:43Z",
"rayName":"6cf919ceda3c1969","User-Agent":"test7", 'Origin':'154.555.444.22'}

def get_url(url):
    return requests.get(url, headers=headers)
list_of_urls = ["https://coinflex.com/home7"]*10000
with ThreadPoolExecutor(max_workers=1000) as pool:
    response_list = list(pool.map(get_url,list_of_urls))
for response in response_list:
    print(response.status_code)