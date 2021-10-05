from polls.models import Question
from polls.tests.test_rules.rule_3.bad_factories import (
    PollFactory as BadPollFactory,
)
from polls.tests.test_rules.rule_3.good_factories import (
    PollFactory as GoodPollFactory,
)


def test_bad_to_string_with_non_premium_english_question_with_author():
    poll = BadPollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        author="John",
    )
    assert str(poll) == "Pepsi or Coke? - By John"


def test_good_to_string_with_non_premium_english_question_with_author():
    poll = GoodPollFactory.build(
        question__question_text="Pepsi or Coke?",
        question__language=Question.EN,
        premium=False,
        with_author=True,
    )

    assert str(poll) == f"Pepsi or Coke? - By {poll.author}"
