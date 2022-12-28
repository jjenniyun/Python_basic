import requests
url = "https://blog.naver.com/gaebal1847"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("simchung.html","w", encoding="utf-8") as f:
    f.write(res.text)