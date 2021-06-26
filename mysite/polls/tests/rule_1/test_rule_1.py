from polls.tests.rule_1.bad_factories import (
    PersonFactory as BadPersonFactory,
)
from polls.tests.rule_1.good_factories import (
    ParentsInfoFactory as GodParentsInfoFactory,
)


def test_bad_factories():
    person = BadPersonFactory.build()
    parents = person.parents

    assert parents.mothers_first_name
    assert parents.mothers_last_name
    assert parents.fathers_first_name
    assert parents.fathers_last_name


def test_good_factories():
    parents = GodParentsInfoFactory.build()
    person = parents.person
    assert person.first_name
    assert person.last_name
