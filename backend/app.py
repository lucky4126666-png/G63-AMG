from flask import Flask, request, jsonify, send_from_directory
from db import init, save
from ai import ask_ai
import os

init()

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")

@app.route("/api/ai", methods=["POST"])
def ai_api():
    text = request.json.get("text")
    reply = ask_ai(text)
    return jsonify({"reply": reply})

@app.route("/api/stats")
def stats():
    return {"users": 100, "messages": 5000}

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")
