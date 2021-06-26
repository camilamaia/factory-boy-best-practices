from factory.django import DjangoModelFactory
from factory import Faker, LazyFunction, SubFactory, Trait

from django.utils import timezone

from polls.models import Choice, Question


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    question = SubFactory("polls.factories.QuestionFactory")


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = Faker("sentence")

    class Params:
        with_author = Trait(author=Faker("name"))


class PastQuestionFactory(QuestionFactory):
    pub_date = Faker(
        "date_time_between",
        end_date="-2d",
        tzinfo=timezone.get_current_timezone(),
    )


class RecentQuestionFactory(QuestionFactory):
    pub_date = LazyFunction(timezone.now)


class FutureQuestionFactory(QuestionFactory):
    pub_date = Faker(
        "date_time_between",
        start_date="+1d",
        tzinfo=timezone.get_current_timezone(),
    )
