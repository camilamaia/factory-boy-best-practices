import factory

from polls.models import Choice, Question


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice

    question = factory.SubFactory(
        "polls.tests.rule_5.good_factories.QuestionFactory"
    )


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
