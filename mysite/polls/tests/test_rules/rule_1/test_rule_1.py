from polls.tests.test_rules.rule_1.bad_factories import (
    QuestionFactory as BadQuestionFactory,
)
from polls.tests.test_rules.rule_1.good_factories import (
    PollFactory as GoodPollFactory,
)


def test_bad_factories():
    question = BadQuestionFactory.build()
    assert question.poll
    assert question.poll.pub_date


def test_good_factories():
    poll = GoodPollFactory.build()
    assert poll.question
    assert poll.question.question_text
