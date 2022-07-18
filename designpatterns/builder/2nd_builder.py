class Person:
    def __init__(self) -> None:
        # Address Information
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment information
        self.company_name = None
        self.position = None
        self.annual_income = None
    
    def __str__(self):
        return 'Nicely first'


class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = person
    
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    
    def build(self):
        return self.person

# sub builder
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
    
    def at(self, company_name):
        self.person.company_name = company_name
        return self

# sub builder
class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
    
    def at(self, stress_address):
        self.person.stress_address = stress_address
        return self

pb = PersonBuilder()
person = pb\
    .lives\
        .at("new york")\
    .works\
        .at("Phantom")\
    .build()