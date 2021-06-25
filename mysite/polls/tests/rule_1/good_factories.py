import factory

from polls.models import Choice, Question


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice

    question = factory.SubFactory("polls.tests.factories.QuestionFactory")


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question
