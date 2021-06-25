from polls.tests.rule_2.good_factories import QuestionFactory
from polls.tests.rule_2.bad_factories import QuestionFactory


def test_bad_to_string_with_non_premium_question_without_author():
    question = QuestionFactory.build()
    assert str(question) == "What's Up?"


def test_good_to_string_with_non_premium_question_without_author():
    question = QuestionFactory.build(
        question_text="Pepsi or Coke?", premium=False, author=None
    )
    assert str(question) == "Pepsi or Coke?"
