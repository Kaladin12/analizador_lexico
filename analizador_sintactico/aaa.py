import requests

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/null/"

headers = {
	"X-RapidAPI-Key": "9ad1df3743mshdce1f17a9b7bf83p186cb7jsna05e2578088a",
	"X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)