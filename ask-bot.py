import requests

res = requests.post("http://cnt-ollama:11434/api/generate", json={
    "model": "pakachan/elyza-llama3-8b",
    "prompt": "日本の総理大臣は誰？",
    "stream": False
})
print("💬 モデルからの返答：\n", res.json()["response"])