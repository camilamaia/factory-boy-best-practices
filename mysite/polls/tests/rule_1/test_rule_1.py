from pytest import mark

from polls.tests.rule_1.bad_factories import RecentQuestionFactory
from polls.tests.rule_1.good_factories import ChoiceFactory


@mark.django_db
def test_bad_to_string_with_non_premium_question_without_author():
    question = RecentQuestionFactory.create(
        with_choices=True,
        question_text="Pepsi or Coke?",
        premium=False,
        author=None,
    )
    choices = question.choices.all()

    assert str(question) == "Pepsi or Coke?"
    assert len(choices) == 2


def test_good_to_string_with_non_premium_question_without_author():
    choice = ChoiceFactory.build(
        question__question_text="Pepsi or Coke?",
        question__premium=False,
        question__author=None,
    )

    assert str(choice.question) == "Pepsi or Coke?"
