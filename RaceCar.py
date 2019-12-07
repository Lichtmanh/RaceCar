from Person import Person


class RaceCar:
    def __init__(self, make, top_speed, first, last, motor_size, wins, losses):
        self.make = make
        self.top_speed = top_speed
        self.driver = Person(first, last)
        self.motor_size = motor_size
        self.wins = wins
        self.losses = losses

    def description(self):
        return "The make is " + self.make + ", the top speed is " + str(self.top_speed) + ""

    def win_race(self):
        self.wins += 1

    def lose_race(self):
        self.losses += 1

    def win_ratio(self):
        total_races = self.wins + self.losses
        return self.wins / total_races
