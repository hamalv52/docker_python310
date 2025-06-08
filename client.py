import requests

res = requests.post("http://cnt-ollama-elyza:11434/api/generate", json={
    "model": "pakachan/elyza-llama3-8b",
    "prompt": "こんにちは！自己紹介して",
    "stream": False
})
print("💬 モデルからの返答：\n", res.json()["response"])