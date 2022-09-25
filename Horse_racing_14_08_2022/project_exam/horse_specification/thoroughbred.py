from project_exam.horse_specification.horse import Horse


class Thoroughbred(Horse):
    SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed += 3
        if self.speed > self.SPEED:
            self.speed = self.SPEED

