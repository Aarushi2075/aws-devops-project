from flask import Flask, jsonify, request, render_template
import json
import os
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

TASK_FILE = "tasks.json"


def load_tasks():
    try:
        if not os.path.exists(TASK_FILE):
            app.logger.warning("tasks.json not found. Initializing empty task list.")
            return []

        with open(TASK_FILE, "r") as f:
            return json.load(f)

    except Exception:
        app.logger.exception("Failed to load tasks.")
        return []


def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)

    except Exception:
        app.logger.exception("Failed to save tasks.")


@app.route("/")
def home():
    app.logger.info("Home page accessed")
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/health")
def health():
    app.logger.info("Health check endpoint accessed")
    return jsonify({
        "status": "healthy",
        "application": "AWS DevOps Project",
        "version": "1.0.0"
    })


@app.route("/version")
def version():
    app.logger.info("Version endpoint accessed")
    return jsonify({
        "version": "1.0.0",
        "environment": "development"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    app.logger.info("Fetching all tasks")
    return jsonify(load_tasks())


@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = load_tasks()
    data = request.json

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    app.logger.info(f"Task created: {task['title']}")

    return jsonify(task), 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            save_tasks(tasks)

            app.logger.info(f"Task completed: ID {id}")

            return jsonify(task)

    app.logger.warning(f"Task not found for update: ID {id}")
    return jsonify({"message": "Task not found"}), 404


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    tasks = load_tasks()

    if not any(task["id"] == id for task in tasks):
        app.logger.warning(f"Task not found for deletion: ID {id}")
        return jsonify({"message": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != id]
    save_tasks(tasks)

    app.logger.info(f"Task deleted: ID {id}")

    return jsonify({
        "message": "Deleted"
    })


if __name__ == "__main__":
    app.logger.info("Starting Flask application")
    app.run(debug=True)