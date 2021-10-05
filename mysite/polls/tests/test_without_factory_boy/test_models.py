import datetime

from django.utils import timezone

from polls.models import Poll, Question


class TestPoll:
    def test_to_string_non_premium_and_without_author(self):
        question = Question(question_text="Summer or Winter?")
        assert (
            str(Poll(question=question, premium=False, author=None))
            == "Summer or Winter?"
        )

    def test_to_string_non_premium_and_with_author_on_english(self):
        question = Question(
            question_text="Summer or Winter?", language=Question.EN
        )
        assert (
            str(Poll(question=question, premium=False, author="John"))
            == "Summer or Winter? - By John"
        )

    def test_to_string_non_premium_and_with_author_on_portuguese(self):
        question = Question(
            question_text="Summer or Winter?", language=Question.PT_BR
        )
        assert (
            str(Poll(question=question, premium=False, author="João"))
            == "Summer or Winter? - Por João"
        )

    def test_to_string_premium_and_without_author(self):
        question = Question(question_text="Summer or Winter?")
        assert (
            str(Poll(question=question, premium=True, author=None))
            == "⭐️ Summer or Winter?"
        )

    def test_to_string_premium_and_with_author_on_english(self):
        question = Question(
            question_text="Summer or Winter?", language=Question.EN
        )
        assert (
            str(Poll(question=question, premium=True, author="John"))
            == "⭐️ Summer or Winter? - By John"
        )

    def test_to_string_premium_and_with_author_on_portuguese(self):
        question = Question(
            question_text="Summer or Winter?", language=Question.PT_BR
        )
        assert (
            str(Poll(question=question, premium=True, author="João"))
            == "⭐️ Summer or Winter? - Por João"
        )

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently returns False for polls whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_poll = Poll(pub_date=time)
        assert old_poll.was_published_recently is False

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently returns True for polls whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recent_poll = Poll(pub_date=time)
        assert recent_poll.was_published_recently is True

    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently returns False for polls whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Poll(pub_date=time)
        assert future_question.was_published_recently is False


class TestQuestion:
    def test_is_in_english_when_language_is_english(self):
        question = Question(language=Question.EN)
        assert question.is_in_english is True

    def test_is_in_english_when_language_is_not_english(self):
        question = Question(language=Question.PT_BR)
        assert question.is_in_english is False

    def test_is_in_portuguese_when_language_is_portuguese(self):
        question = Question(language=Question.PT_BR)
        assert question.is_in_portuguese is True

    def test_is_in_portuguese_when_language_is_not_portuguese(self):
        question = Question(language=Question.EN)
        assert question.is_in_portuguese is False
