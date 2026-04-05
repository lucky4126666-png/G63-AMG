from flask import Flask, request, jsonify
from core.queue import queue
from worker.tasks import ai_task
from core.db import init_db, add_user

app = Flask(__name__)
init_db()

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    user_id = data.get("user_id")
    text = data.get("text")

    add_user(user_id)

    job = queue.enqueue(ai_task, text)

    return jsonify({"job_id": job.id})

@app.route("/stats")
def stats():
    return {"users": 100, "messages": 5000, "jobs": 10}
