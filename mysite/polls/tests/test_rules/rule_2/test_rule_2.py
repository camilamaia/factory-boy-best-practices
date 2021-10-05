from polls.tests.test_rules.rule_2.bad_factories import (
    PollFactory as BadPollFactory,
)
from polls.tests.test_rules.rule_2.good_factories import (
    PollFactory as GoodPollFactory,
)


def test_bad_to_string_with_non_premium_question_without_author():
    poll = BadPollFactory.build()
    assert str(poll) == "What's Up?"


def test_good_to_string_with_non_premium_question_without_author():
    question = GoodPollFactory.build(
        premium=False, author=None, question__question_text="Pepsi or Coke?"
    )
    assert str(question) == "Pepsi or Coke?"
