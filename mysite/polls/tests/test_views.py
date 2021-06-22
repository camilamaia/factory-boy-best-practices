import datetime
from pytest import mark

from django.urls import reverse
from django.utils import timezone


from polls.models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


@mark.django_db
def test_no_questions(client):
    """
    If no questions exist, an appropriate message is displayed.
    """
    response = client.get(reverse("polls:index"))
    assert response.status_code == 200
    assert "No polls are available." in str(response.content)
    assert len(response.context["latest_question_list"]) == 0


@mark.django_db
def test_past_question(client):
    """
    Questions with a pub_date in the past are displayed on the
    index page.
    """
    question = create_question(question_text="Past question.", days=-30)
    response = client.get(reverse("polls:index"))
    actual_questions = response.context["latest_question_list"]

    assert len(actual_questions) == 1
    assert question in actual_questions


@mark.django_db
def test_future_question(client):
    """
    Questions with a pub_date in the future aren't displayed on
    the index page.
    """
    create_question(question_text="Future question.", days=30)
    response = client.get(reverse("polls:index"))
    actual_questions = response.context["latest_question_list"]

    assert "No polls are available." in str(response.content)
    assert len(actual_questions) == 0


@mark.django_db
def test_future_question_and_past_question(client):
    """
    Even if both past and future questions exist, only past questions
    are displayed.
    """
    question = create_question(question_text="Past question.", days=-30)
    future_question = create_question(question_text="Future question.", days=30)
    response = client.get(reverse("polls:index"))
    actual_questions = response.context["latest_question_list"]

    assert len(actual_questions) == 1
    assert question in actual_questions
    assert future_question not in actual_questions


@mark.django_db
def test_two_past_questions(client):
    """
    The questions index page may display multiple questions.
    """
    question1 = create_question(question_text="Past question 1.", days=-30)
    question2 = create_question(question_text="Past question 2.", days=-5)
    response = client.get(reverse("polls:index"))
    actual_questions = response.context["latest_question_list"]

    assert len(actual_questions) == 2
    assert question1 in actual_questions
    assert question2 in actual_questions
