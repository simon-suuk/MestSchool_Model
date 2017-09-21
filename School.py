class School:
    def __init__(self):
        self.eits = {}
        self.fellows = {}
        self.last_eit_id = 0
        self.last_fellow_id = 0

    def __repr__(self):
        return self.__dict__

    def add_eit(self, eit):
        self.last_eit_id += 10
        current_eit_id = "eit_" + str(self.last_eit_id)
        self.eits.__setitem__(current_eit_id, eit)

    def add_fellow(self, fellow):
        self.last_fellow_id += 10
        current_fellow_id = "fellow_" + str(self.last_fellow_id)
        self.fellows.__setitem__(current_fellow_id, fellow)

    def has_eit(self, name):
        pass

    def has_fellow(self, name):
        pass


class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class EIT(Person):
    def __init__(self, name, nationality):
        super().__init__(name, nationality)

    def recite_fun_fact(self, fun_fact):
        print("{}".format(fun_fact))


class MoneyException(Exception):
    def __init__(self, arg):
        self.args = arg


class Fellow(Person):
    number_of_fellows_created = 0

    def __init__(self, name, nationality, happiness_level=0):
        Fellow.number_of_fellows_created += 1
        if Fellow.number_of_fellows_created > 4:
            try:
                # raise Exception(name)
                raise MoneyException(name)
            except MoneyException as ex:
                print("{}: We cannot afford to hire {}".format(ex.__class__.__name__, "".join(ex.args)))

        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self, name, food, happiness_level=1):
        self.happiness_level += happiness_level
        print("{} {}".format(self.name, food, self.happiness_level))

    def teach(self, name, lesson, happiness_level=1):
        self.happiness_level -= happiness_level
        print("{}".format(self.name, lesson, self.happiness_level))


if __name__ == "__main__":
    # create new school
    mest = School()

    # create 5 fellows
    andrew = Fellow("Andrew", "American")
    simphiwe = Fellow("Simphiwe", "South African")
    miishe = Fellow("Miishe", "Ghanaian")
    edem = Fellow("Edem", "Ghanaian")
    kerry = Fellow("Kerry", "American")
    pascal = Fellow("Pascal", "DRC")

    # create 3 eits
    elohor = EIT("elohor", "Nigerian")
    simon = EIT("simon", "Ghanaian")
    kelvin_tyron = EIT("kelvin tyron", "Ghanaian")

    # add fellows to school
    mest.add_fellow(andrew)
    mest.add_fellow(simphiwe)

    # add eits to school
    mest.add_eit(elohor)
    mest.add_eit(simon)
    mest.add_eit(kelvin_tyron)
