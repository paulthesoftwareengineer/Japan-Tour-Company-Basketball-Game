class BasketballPlayer:
    def __init__(self, name, age, position,experience):
        self.name = name
        self.age = age
        self.position = position
        self.experience = experience

        def dunk(self):
            print('dunk')

        def free_throw(self):
            print('one point')

        def two_point(self):
            print('two points')

        def three_point(self):
            print('three points')

        player1 = BasketballPlayer('James', 22, 'center', 'junior')

        print(BasketballPlayer.dunk())

