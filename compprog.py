import requests, json, webbrowser

def doggie():
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    data = json.loads(page.text)
    webbrowser.open(data["url"])
doggie()
