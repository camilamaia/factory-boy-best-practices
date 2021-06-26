from pytest import mark
from polls.tests.rule_4.good_factories import QuestionFactory
from polls.models import Question


@mark.django_db
def test_bad_to_string_with_non_premium_english_question_with_author():
    question = QuestionFactory.create(
        question_text="Pepsi or Coke?",
        language=Question.EN,
        premium=False,
        with_author=True,
    )
    assert str(question) == f"Pepsi or Coke? - By {question.author}"


def test_good_to_string_with_non_premium_english_question_with_author():
    question = QuestionFactory.build(
        question_text="Pepsi or Coke?",
        language=Question.EN,
        premium=False,
        with_author=True,
    )
    assert str(question) == f"Pepsi or Coke? - By {question.author}"
