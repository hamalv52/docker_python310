import requests

res = requests.post("http://your-ollama-containername:11434/api/generate", json={
    "model": "pakachan/elyza-llama3-8b",
    "prompt": "こんにちは！自己紹介して",
    "stream": False
})
print("💬 モデルからの返答：\n", res.json()["response"])
