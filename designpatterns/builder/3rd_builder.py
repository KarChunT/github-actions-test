class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} - {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()
    
    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def calleda(self, name):
        self.person.name = name
        return self


class PersonPositionBuilder(PersonInfoBuilder):
    def called(self, position):
        self.person.position = position
        return self


pb = PersonPositionBuilder()
me = pb\
        .called('software engineer')\
        .calleda('')\
        .build()