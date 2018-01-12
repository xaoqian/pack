pi = 3.14
ridius = int(input('введите радиус круга: '))
area = int(ridius * pi * ridius)
perimeter = int(ridius * pi * 2)

class Circle:
    def _init_(self, area):
        self.area = area
        print('(Initialized Circle:{})'.format(self.area))

    def _init_(self, perimeter):
        self.perimeter = perimeter
        print('(Initialized Circle:{})'.format(self.perimeter))




