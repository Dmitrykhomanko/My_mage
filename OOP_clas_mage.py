class Mage:
    def __init__(self, name, good_or_bad, spells_book, main_weapon):
        self.name = name
        self.good_or_bad = good_or_bad
        self.spells_book = spells_book
        self.main_weapon = main_weapon

    def cast(self):
        print(f"{self.name} I am casting a Faer __night!")
        # if self.spells_book == "Школа моглний":
        #     print(f"{self.name} I am casting a lightnight!")

    def batlle_cry(self):
       print(f"{self.name} I Am not a good mage NOW I'm  a necromancer")

    def auto_atack(self):
        print(f'{self.name} У вас кончилась мана и терь ваш маг бьет посохом')

my_mage = Mage('Генд', 'B', 'Школа ', 'Длинный посох')
my_mage.cast()
my_mage.batlle_cry()
my_mage.auto_atack()


     # class Cat:
        #     def __init__(self, color, name):
        #         self.color = color
        #         self.name = name
        #
        #     def murk(self):
        #         print(f"{self.name} Mze .....")
        #
        #     def fight(self):
        #         print(f"{self.name} cats are fighting .....")
        #
        # my_cat = Cat('red', 'Tuti')
        # my_cat.murk()
        # my_cat.fight()
