import factory

from django.utils import timezone

from polls.models import Choice, Question


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    class Params:
        with_choices = factory.Trait(
            choice_1=factory.RelatedFactory(
                ChoiceFactory,
                "question",
                choice_text="Option 1",
            ),
            choice_2=factory.RelatedFactory(
                ChoiceFactory,
                "question",
                choice_text="Option 2",
            ),
        )


class RecentQuestionFactory(QuestionFactory):
    pub_date = factory.LazyFunction(timezone.now)
