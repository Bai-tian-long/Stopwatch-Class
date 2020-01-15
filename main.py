"""
 (Stopwatch) Design a class named StopWatch. The class contains:
■ The private data fields startTime and endTime with get methods.
■ A constructor that initializes startTime with the current time.
■ A method named start() that resets the startTime to the current time.
■ A method named stop() that sets the endTime to the current time.
■ A method named getElapsedTime() that returns the elapsed time for the
stop watch in milliseconds.
Draw the UML diagram for the class, and then implement the class. Write a test
program that measures the execution time of adding numbers from 1 to
1,000,000.
"""
import time

class Stopwatch():
  def __init__(self):
    self.__startTime = time.time()
    self.__endTime = 0


  def getStartTime(self):
    return self.__startTime

  def start(self):
    self.__startTime = time.time()

  def stop(self):
    self.__endTime = time.time()

  def getEndTime(self):
    return self.__endTime

  def getElapsedTime(self):
    return str((self.__endTime - self.__startTime) * 1000)


def main():
  timer = Stopwatch()

  total = 0
  
  print("Timer started")
  timer.start()

  for i in range(1000000):
    total += i

  timer.stop()
  print("Timer stopped")
  
  r = timer.getElapsedTime()

  print("The time in milliseconds the addition took was:", r)

main()