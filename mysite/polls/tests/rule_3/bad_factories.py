import factory

from django.utils import timezone

from polls.models import Question


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Faker("sentence")
    pub_date = factory.LazyFunction(timezone.now)
    language = Question.PT_BR
    author = "João"
    premium = True
