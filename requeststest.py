import requests

params = {"#q":}
r = requests.get("http://google.com")
print("Status:", r.status_code)

print(r.url)
print(r.text)

f = open("./page.html","w+")

f.write(r.text)