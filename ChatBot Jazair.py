import requests

url = "https://copilot5.p.rapidapi.com/copilot"

session = requests.Session()
session.headers.update({
    "x-rapidapi-key": "769b502c36msh70a6926047f2379p107df1jsn4337141c8485",
    "x-rapidapi-host": "copilot5.p.rapidapi.com",
    "Content-Type": "application/json"
})

while True:
    message = input("You: ")
    if message.lower() == "exit":
        break

    payload = {
        "message": message,
        "conversation_id": None,
        "mode": "CHAT",
        "markdown": True
    }

    response = session.post(url, json=payload)
    data = response.json()
    print("Jazair: ", data["data"]["message"])
