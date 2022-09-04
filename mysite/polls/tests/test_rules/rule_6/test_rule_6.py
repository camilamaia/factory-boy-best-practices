from pytest import fixture

from polls.models import Question
from polls.tests.test_with_factories.factories import PollFactory

# Good


@fixture
def english_non_premium_with_author_poll():
    return PollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )


def test_1(english_non_premium_with_author_poll):
    # ...
    pass


def test_2(english_non_premium_with_author_poll):
    # ...
    pass


# Bad


def test_3():
    poll = PollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )
    # ...
    pass


def test_4():
    poll = PollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )
    # ...
    pass


# ...
