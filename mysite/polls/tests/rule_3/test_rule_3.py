from polls.tests.rule_3.bad_factories import (
    QuestionFactory as BadQuestionFactory,
)
from polls.tests.rule_3.good_factories import (
    QuestionFactory as GoodQuestionFactory,
)

from polls.models import Question


def test_bad_to_string_with_non_premium_english_question_with_author():
    question = BadQuestionFactory.build(
        question_text="Pepsi or Coke?",
        language=Question.EN,
        premium=False,
        author="John",
    )
    assert str(question) == "Pepsi or Coke? - By John"


def test_good_to_string_with_non_premium_english_question_with_author():
    question = GoodQuestionFactory.build(
        question_text="Pepsi or Coke?",
        language=Question.EN,
        premium=False,
        with_author=True,
    )
    assert str(question) == f"Pepsi or Coke? - By {question.author}"
