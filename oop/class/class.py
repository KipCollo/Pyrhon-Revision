class Shape:
    shape_name='circle'

    def __init__(self,radius):
        self.__radius =radius

    def setRadius(self,radius):
        self.radius=radius

circle =Shape(27)
circle.setRadius(3)
print(circle.radius)
print(circle.__dict__)