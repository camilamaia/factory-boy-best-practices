import factory
from django.utils import timezone

from polls.models import Poll, Question


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Poll

    pub_date = factory.LazyFunction(timezone.now)
    author = "João"
    premium = True
    question = factory.SubFactory(
        "polls.tests.test_rules.rule_3.bad_factories.QuestionFactory"
    )


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Faker("sentence")
    language = Question.PT_BR
