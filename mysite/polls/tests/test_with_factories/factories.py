from django.utils import timezone
from factory import Faker, LazyFunction, RelatedFactory, SubFactory, Trait
from factory.django import DjangoModelFactory

from polls.models import Choice, Poll, Question


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    question = SubFactory("polls.factories.QuestionFactory")


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = Faker("sentence")

    class Params:
        english = Trait(language=Question.EN)
        portuguese = Trait(language=Question.PT_BR)
        with_choices = Trait(
            choice_1=RelatedFactory(
                ChoiceFactory,
                "question",
                choice_text="Option 1",
            ),
            choice_2=RelatedFactory(
                ChoiceFactory,
                "question",
                choice_text="Option 2",
            ),
        )


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll

    pub_date = LazyFunction(timezone.now)
    question = SubFactory(QuestionFactory)

    class Params:
        with_author = Trait(author=Faker("name"))


class PastPollFactory(PollFactory):
    pub_date = Faker(
        "date_time_between",
        end_date="-2d",
        tzinfo=timezone.get_current_timezone(),
    )


class RecentPollFactory(PollFactory):
    pub_date = LazyFunction(timezone.now)


class FuturePollFactory(PollFactory):
    pub_date = Faker(
        "date_time_between",
        start_date="+1d",
        tzinfo=timezone.get_current_timezone(),
    )
