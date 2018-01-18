import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/getreviews"

# change page numbers here - put this in a loop
pageNum = str(0);
app_id = "com.myairtelapp"


querystring = {"authuser":"0"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"reviewType\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pageNum\"\r\n\r\n"+pageNum+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n"+app_id+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"reviewSortOrder\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"xhr\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"hl\"\r\n\r\nen\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.text[18:-9].encode('utf8').decode('unicode-escape'))

soup = BeautifulSoup(response.text[18:-9].encode('utf8').decode('unicode-escape','ignore'))
print soup.prettify()