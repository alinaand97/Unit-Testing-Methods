# Методы Юнит-тестирования

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def add_runner(self, runner):
        self.participants.append(runner)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

class Tournament:
    def __init__(self, distance):
        self.distance = distance
        self.runners = []

    def add_runner(self, runner):
        self.runners.append(runner)

    def start(self):
        results = {}
        for runner in self.runners:
            time = self.distance / runner.speed
            results[runner.name] = time

        # Сортируем результаты по времени
        sorted_results = sorted(results.items(), key=lambda x: x[1])
        return {i + 1: runner for i, (runner, _) in enumerate(sorted_results)}

import unittest
class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == "Nick")

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90)
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)
        result = tournament.start()
        self.all_results.append(result)  
        self.assertTrue(result[3] == "Nick")


if __name__ == "__main__":
    unittest.main()