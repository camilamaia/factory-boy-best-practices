import factory

from polls.models import Person, ParentsInfo


class ParentsInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ParentsInfo

    mothers_first_name = factory.Faker("first_name")
    mothers_last_name = factory.Faker("last_name")
    fathers_first_name = factory.Faker("first_name")
    fathers_last_name = factory.Faker("last_name")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    parents = factory.RelatedFactory(ParentsInfoFactory, "person")
