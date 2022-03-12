class Super_heroes():

    def __init__(self, Name, Age, Weight):
        self.Name = Name
        self.Age = Age
        self.Weight = Weight

    def Saved_people(self):
        print(self.Name.title() + ' спас людей')

    def Stopped_the_fire(self):
        print(self.Name.title() + ' остоновил пожар')

    def Defeated_the_villains(self):
        print(self.Name.title() + ' победил злодеев ')


class Spider_man(Super_heroes):

    def __init__(self, Name, Age, Surname, Quarter_grade, Weight):
        super().__init__(Name, Age, Weight)
        self.Quarter_grade = Quarter_grade
        self.Surname = Surname

    def Threw_a_web(self):
        print(self.Name.title() + 'бросил паутину')

    def Got_an_A(self):
        print(self.Name.title() + 'получил пятёрку')


Spider_man1 = Spider_man('Питер', 16, 'паркер', 5, '76 KG')


class Hulk(Super_heroes):

    def __init__(self, Name, Age, Weight, Hulk_rise, Rise):
        super().__init__(Name, Age, Weight)
        self.Hulk_rise = Hulk_rise
        self.Rise = Rise

    def Became_a_hulk(self):
        print(self.Name.title() + ' стал халком ')

    def Became_a_human(self):
        print(self.Name.title() + ' стал халком ')


Hulk1 = Hulk('Брюс', '?', '58,522', 229, 175)


class Captain_America(Super_heroes):

    def __init__(self, Name, Age, Weight, Rise, Gender):
        super().__init__(Name, Age, Weight)
        self.Rise = Rise
        self.Gender = Gender

    def Killed_a_villain(self):
        print(self.Name.title + ' убил злодея')

    def Died_in_battle(self):
        print('к сожелению ' + self.Name.title + ' погиб в бою ')


Captain_America1 = Captain_America('Стив', 92, '109KG', 188, 'man')


class Iron_man(Super_heroes):

    def __init__(self, Name, Age, Weight, Battery_charge, Number_of_shots):
        super().__init__(Name, Age, Weight)
        self.Battery_charge = Battery_charge
        self.Number_of_shots = Number_of_shots

    def Flew(self):
        print(self.Name.title + ' взлетел ')

    def Fired(self):
        print(self.Name.title + ' выстрельнул')


Iron_man1 = Iron_man('Энтони', 53, '90KG', '10%', 10000000000000000000000000000000000)


class Tor(Captain_America):

    def __init__(self, Name, Age, Weight, Rise, Gender, Position, Name_wife):
        super().__init__(Name, Age, Weight, Rise, Gender)
        self.Position = Position
        self.Name_wife = Name_wife

    def Shot_lightning(self):
        print(self.Name.title + 'стрельнул молнией')

    def Flew(self):
        print(self.Name.title + 'взлетел')


Tor1 = Tor('tor', 1500, '?', 198, 'man', 'good', 'Jane')