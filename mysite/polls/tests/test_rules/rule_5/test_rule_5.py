from pytest import mark

from polls.tests.test_rules.rule_5.good_factories import (
    ChoiceFactory,
    QuestionFactory,
)


def test_build_choice():
    choice = ChoiceFactory.build(
        question__question_text="Pepsi or Coke?",
    )

    assert str(choice.question) == "Pepsi or Coke?"


def test_build_question_without_choices():
    question = QuestionFactory.build()

    assert not question.choices.all()


@mark.django_db
def test_build_question_with_choices():
    # We need to use `create` here in order to create the relationships
    question = QuestionFactory.create(with_choices=True)

    assert question.choices.count() == 2
