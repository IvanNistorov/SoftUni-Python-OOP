from project_exam.horse_specification.horse import Horse


class Appaloosa(Horse):
    SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed += 2
        if self.speed > self.SPEED:
            self.speed = self.SPEED
