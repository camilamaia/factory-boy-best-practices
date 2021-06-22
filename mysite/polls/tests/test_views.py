import datetime
from pytest import fixture, mark

from django.urls import reverse
from django.utils import timezone

from polls.models import Question


def get_time(days):
    return timezone.now() + datetime.timedelta(days=days)


@mark.django_db
class TestIndexView:
    @fixture
    def past_question(self):
        published_at = get_time(days=-30)
        return Question.objects.create(
            question_text="Past question", pub_date=published_at
        )

    @fixture
    def recent_question(self):
        published_at = get_time(days=-1)
        return Question.objects.create(
            question_text="Recent question", pub_date=published_at
        )

    @fixture
    def future_question(self):
        published_at = get_time(days=30)
        return Question.objects.create(
            question_text="Future question", pub_date=published_at
        )

    def test_no_questions(self, client):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = client.get(reverse("polls:index"))
        assert response.status_code == 200
        assert "No polls are available." in str(response.content)
        assert len(response.context["latest_question_list"]) == 0

    def test_past_question(self, client, past_question):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        response = client.get(reverse("polls:index"))
        actual_questions = response.context["latest_question_list"]

        assert len(actual_questions) == 1
        assert past_question in actual_questions

    def test_future_question(self, client, future_question):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        response = client.get(reverse("polls:index"))
        actual_questions = response.context["latest_question_list"]

        assert "No polls are available." in str(response.content)
        assert future_question not in actual_questions
        assert len(actual_questions) == 0

    def test_future_question_and_past_question(
        self, client, past_question, future_question
    ):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        response = client.get(reverse("polls:index"))
        actual_questions = response.context["latest_question_list"]

        assert len(actual_questions) == 1
        assert past_question in actual_questions
        assert future_question not in actual_questions

    def test_two_past_questions(self, client, past_question, recent_question):
        """
        The questions index page may display multiple questions.
        """
        response = client.get(reverse("polls:index"))
        actual_questions = response.context["latest_question_list"]

        assert len(actual_questions) == 2
        assert past_question in actual_questions
        assert recent_question in actual_questions
