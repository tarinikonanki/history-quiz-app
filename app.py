import json
import os
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions.json")


def load_questions() -> list[dict]:
    with open(QUESTIONS_FILE) as f:
        return json.load(f)


def get_current_question(questions: list[dict]) -> dict | None:
    index = session.get("current_index", 0)
    if index >= len(questions):
        return None
    return questions[index]


def record_answer(is_correct: bool) -> None:
    if is_correct:
        session["score"] = session.get("score", 0) + 1
    session["current_index"] = session.get("current_index", 0) + 1


def init_session() -> None:
    session["score"] = 0
    session["current_index"] = 0
    session["total"] = len(load_questions())


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/start")
def start() -> str:
    init_session()
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz() -> str:
    questions = load_questions()

    if request.method == "POST":
        selected = request.form.get("choice")
        index = session.get("current_index", 0)
        question = questions[index]
        is_correct = selected == question["answer"]
        record_answer(is_correct)
        return render_template(
            "feedback.html",
            question=question,
            selected=selected,
            is_correct=is_correct,
            next_index=session["current_index"],
            total=len(questions),
        )

    question = get_current_question(questions)
    if question is None:
        return redirect(url_for("results"))

    return render_template(
        "quiz.html",
        question=question,
        current=session.get("current_index", 0) + 1,
        total=len(questions),
    )


@app.route("/results")
def results() -> str:
    score = session.get("score", 0)
    total = session.get("total", len(load_questions()))
    return render_template("results.html", score=score, total=total)


if __name__ == "__main__":
    app.run(debug=True)
