import json
from pathlib import Path


def get_questions():
    questions_path = Path(__file__).parent.parent / "questions.json"
    with open(questions_path) as file:
        return json.load(file)


def test_questions_exist():
    questions = get_questions()
    assert len(questions) > 0


def test_each_question_has_four_choices():
    questions = get_questions()

    for question in questions:
        assert len(question["choices"]) == 4
        assert question["answer"] in question["choices"]
