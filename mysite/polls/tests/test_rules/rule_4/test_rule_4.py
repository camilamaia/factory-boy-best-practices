from pytest import mark

from polls.models import Question
from polls.tests.test_rules.rule_4.good_factories import PollFactory


@mark.django_db
def test_bad_to_string_with_non_premium_english_question_with_author():
    question = PollFactory.create(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )
    assert str(question) == f"Pepsi or Coke? - By {question.author}"


def test_good_to_string_with_non_premium_english_question_with_author():
    question = PollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )
    assert str(question) == f"Pepsi or Coke? - By {question.author}"
