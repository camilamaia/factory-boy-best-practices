from pytest import mark

from polls.tests.rule_5.good_factories import ChoiceFactory


def test_to_string_with_non_premium_question_without_author():
    choice = ChoiceFactory.build(
        question__question_text="Pepsi or Coke?",
        question__premium=False,
        question__author=None,
    )

    assert str(choice.question) == "Pepsi or Coke?"
