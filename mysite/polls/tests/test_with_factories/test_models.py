from polls.tests.test_with_factories.factories import (
    FuturePollFactory,
    PastPollFactory,
    PollFactory,
    QuestionFactory,
    RecentPollFactory,
)


class TestPoll:
    def test_to_string_non_premium_and_without_author(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            premium=False,
            author=None,
        )
        assert str(poll) == "Summer or Winter?"

    def test_to_string_non_premium_and_with_author_on_english(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            question__english=True,
            premium=False,
            author="John",
        )
        assert str(poll) == "Summer or Winter? - By John"

    def test_to_string_non_premium_and_with_author_on_portuguese(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            question__portuguese=True,
            premium=False,
            author="João",
        )
        assert str(poll) == "Summer or Winter? - Por João"

    def test_to_string_premium_and_without_author(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            premium=True,
            author=None,
        )
        assert str(poll) == "⭐️ Summer or Winter?"

    def test_to_string_premium_and_with_author_on_english(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            question__english=True,
            premium=True,
            author="John",
        )
        assert str(poll) == "⭐️ Summer or Winter? - By John"

    def test_to_string_premium_and_with_author_on_portuguese(self):
        poll = PollFactory.build(
            question__question_text="Summer or Winter?",
            question__portuguese=True,
            premium=True,
            author="João",
        )
        assert str(poll) == "⭐️ Summer or Winter? - Por João"

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently returns False for polls whose pub_date
        is older than 1 day.
        """
        old_poll = PastPollFactory.build()
        assert old_poll.was_published_recently is False

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently returns True for polls whose pub_date
        is within the last day.
        """
        recent_poll = RecentPollFactory.build()
        assert recent_poll.was_published_recently is True

    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently returns False for polls whose pub_date
        is in the future.
        """
        future_question = FuturePollFactory.build()
        assert future_question.was_published_recently is False


class TestQuestion:
    def test_is_in_english_when_language_is_english(self):
        assert QuestionFactory.build(english=True).is_in_english is True

    def test_is_in_english_when_language_is_not_english(self):
        assert QuestionFactory.build(portuguese=True).is_in_english is False

    def test_is_in_portuguese_when_language_is_portuguese(self):
        assert QuestionFactory.build(portuguese=True).is_in_portuguese is True

    def test_is_in_portuguese_when_language_is_not_portuguese(self):
        assert QuestionFactory.build(english=True).is_in_portuguese is False
