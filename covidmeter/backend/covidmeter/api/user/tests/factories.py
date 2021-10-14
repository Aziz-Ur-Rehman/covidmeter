import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "user.User"
        django_get_or_create = (
            "email",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
        )

    email = factory.Faker("email")
    password = factory.Faker("password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_of_birth = factory.Faker("date")
