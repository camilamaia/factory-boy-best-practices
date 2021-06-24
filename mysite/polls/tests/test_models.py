import datetime

from django.utils import timezone

from polls.models import Question
from polls.tests.factories import (
    FutureQuestionFactory,
    PastQuestionFactory,
    QuestionFactory,
    RecentQuestionFactory,
)


class TestQuestion:
    def test_to_string_with_non_premium_question_without_author(self):
        """
        str(question) returns the question_text for non premium questions without author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?", premium=False, author=None
        )
        assert str(question) == "Pepsi or Coke?"

    def test_to_string_with_english_non_premium_question_with_author(self):
        """
        str(question) returns the `question_text - By author` for English non premium questions
        with author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?",
            language=Question.EN,
            premium=False,
            with_author=True,
        )
        assert str(question) == f"Pepsi or Coke? - By {question.author}"

    def test_to_string_with_portuguese_non_premium_question_with_author(self):
        """
        str(question) returns the `question_text - Por author` for English non premium questions
        with author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?",
            language=Question.PT_BR,
            with_author=True,
            premium=False,
        )
        assert str(question) == f"Pepsi or Coke? - Por {question.author}"

    def test_to_string_with_premium_question_without_author(self):
        """
        str(question) returns the `⭐️ question_text` for premium questions without author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?", premium=True, author=None
        )
        assert str(question) == "⭐️ Pepsi or Coke?"

    def test_to_string_with_english_premium_question_with_author(self):
        """
        str(question) returns the `⭐️ question_text - By author` for English premium questions with
        author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?",
            language=Question.EN,
            premium=True,
            with_author=True,
        )
        assert str(question) == f"⭐️ Pepsi or Coke? - By {question.author}"

    def test_to_string_with_portuguese_premium_question_with_author(self):
        """
        str(question) returns the `⭐️ question_text - Por author` for Portuguese premium questions
        with author
        """
        question = QuestionFactory(
            question_text="Pepsi or Coke?",
            language=Question.PT_BR,
            with_author=True,
            premium=True,
        )
        assert str(question) == f"⭐️ Pepsi or Coke? - Por {question.author}"

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        question = PastQuestionFactory.build()
        assert question.was_published_recently() is False

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        question = RecentQuestionFactory.build()
        assert question.was_published_recently() is True

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question = FutureQuestionFactory.build()
        assert question.was_published_recently() is False

    def test_is_english_with_english_question(self):
        """
        is_in_english returns True for English questions
        """
        question = question = QuestionFactory(
            language=Question.EN,
        )
        assert question.is_in_english is True

    def test_is_english_with_english_question(self):
        """
        is_in_english returns False for Portuguese questions
        """
        question = question = QuestionFactory(
            language=Question.PT_BR,
        )
        assert question.is_in_english is False

    def test_is_portuguese_with_english_question(self):
        """
        is_in_portuguese returns False for English questions
        """
        question = question = QuestionFactory(
            language=Question.EN,
        )
        assert question.is_in_portuguese is False

    def test_is_portuguese_with_english_question(self):
        """
        is_in_portuguese returns True for Portuguese questions
        """
        question = question = QuestionFactory(
            language=Question.PT_BR,
        )
        assert question.is_in_portuguese is True
