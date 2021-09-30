import webbrowser
import requests

url = "https://jooheonchoi.github.io/"
webbrowser.open(url)

html = requests.get(url)
print(html.text)



