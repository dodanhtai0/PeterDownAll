import httpx

with open("http.txt", 'w') as file:
	file.write(httpx.get("https://dodanhtai.site/proxy/http.txt").text)