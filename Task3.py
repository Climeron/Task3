# Шматок А. P3175
# Задание №3
# За объёмную фигуру был взят куб
import math


class Cube:
    angles = [0, 0, 0]
    vertices = []

    def __init__(self, length):
        self.halfLength = length / 2
        self.vertices = \
            [
                [-self.halfLength, -self.halfLength, -self.halfLength],
                [-self.halfLength, -self.halfLength, self.halfLength],
                [-self.halfLength, self.halfLength, -self.halfLength],
                [-self.halfLength, self.halfLength, self.halfLength],
                [self.halfLength, -self.halfLength, -self.halfLength],
                [self.halfLength, -self.halfLength, self.halfLength],
                [self.halfLength, self.halfLength, -self.halfLength],
                [self.halfLength, self.halfLength, self.halfLength],
            ]

    # поворот по оси Х
    def rotate_x(self, angle):
        self.angles[0] = angle
        cos = round(math.cos(math.radians(angle)), 8)
        sin = round(math.sin(math.radians(angle)), 8)
        for i in range(8):
            vertice = self.vertices[i]
            self.vertices[i] = [vertice[0], cos * vertice[1] - sin * vertice[2], sin * vertice[1] + cos * vertice[2]]

    # поворот по оси Y
    def rotate_y(self, angle):
        self.angles[0] = angle
        cos = round(math.cos(math.radians(angle)), 8)
        sin = round(math.sin(math.radians(angle)), 8)
        for i in range(8):
            vertice = self.vertices[i]
            self.vertices[i] = [cos * vertice[0] - sin * vertice[2], vertice[1], sin * vertice[0] + cos * vertice[2]]

    # поворот по оси Z
    def rotate_z(self, angle):
        self.angles[0] = angle
        cos = round(math.cos(math.radians(angle)), 8)
        sin = round(math.sin(math.radians(angle)), 8)
        for i in range(8):
            vertice = self.vertices[i]
            self.vertices[i] = [cos * vertice[0] - sin * vertice[1], sin * vertice[0] + cos * vertice[1], vertice[2]]

# здесь задаётся длина ребра куба
length = Cube(2)
print(length.vertices)

# здесь указываются углы поворота по осям в градусах
length.rotate_x(0)
length.rotate_y(0)
length.rotate_z(0)
print(length.vertices)
