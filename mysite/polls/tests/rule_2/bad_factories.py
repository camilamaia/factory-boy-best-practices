import factory

from django.utils import timezone

from polls.models import Question


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = "What's Up?"
    pub_date = factory.LazyFunction(timezone.now)
