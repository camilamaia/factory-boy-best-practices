# factory_boy Best Practices

1. Factories should represent their models

1. Do not rely on defaults from factories

    * If a default value is changed, all tests that depend on it will break
    * The setup of a test should contain all the logic to ensure it will always pass
    * Explicit better than implicit

1. Factories should contain only the required data

    * If the field is nullable (null=True) the attribute should be under a trait 
    and not as a default value
    * If we want to have explicitly the attribute, we can use MyFactory(with_myattr=True)
    * When are we going to remember to test the case MyFactory(myattr=None)?
    * We should not assume there is an author when DB actually allows to not have it.

1. Build over create

    * MyFactory.build(): creates a local object (memory)
    * MyFactory.create(): creates a local object + stores it in the DB

1. If FK is in the table: SubFactor

   If FK is in the other table: RelatedFactory + trait


    * SubFactory: builds/creates the SubFactory during the process of creation of the main factory
    * RelatedFactory: builds/creates the RelatedFactory after creating the main factory

1. Fixtures should be used only to wrap factories

1. Use fixtures to wrap factories to avoid duplication

1. Avoid sharing factories or fixtures among different files

1. get_or_create should be used only for unique keys
