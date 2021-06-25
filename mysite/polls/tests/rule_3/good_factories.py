import factory

from polls.models import Choice, Question


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Faker("sentence")
