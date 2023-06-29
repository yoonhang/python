import requests
res = requests.get("http://naver.com")
print(res.status_code)

if res.status_code == requests.codes.ok:
    print("ok")
else:
    print(res.status_code)
    
res.raise_for_status()
print(res.text)


with open("naver.html", "w", encoding="utf8") as f:
    f.write(res.text)
    
    


