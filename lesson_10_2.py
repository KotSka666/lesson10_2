import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days_fought = 0
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            self.enemies -= self.power
            self.enemies = max(self.enemies, 0)

            self.days_fought += 1
            print(f"{self.name}, сражается {self.days_fought} день(дня)..., осталось {self.enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.days_fought} дней(дня)!")

first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
