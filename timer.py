class Timer():
    def __init__(self):
        while True:
            try:
                self.time = int(input('Please input the amount of time the timer will last.\n:'))
                self.warn_1 = int(input('Please input the first warning time.\n:'))
                self.warn_2 = int(input('Please input the second warning time.\n:'))
                self.warn_3 = int(input('Please input the third warning time.\n:'))
            except ValueError:
                print('Error: Invalid. Please try again.')
            else:
                break;

    def start(self):
        import time
        for i in range(self.time):
            if self.time-i==self.warn_1:

                print("Warning 3: " + str(self.warn_1) + " seconds left!")
            elif self.time-i==self.warn_2:
                print("Warning 2: " + str(self.warn_2) + " seconds left!")
            elif self.time-i==self.warn_3:
                print("Warning 1: " + str(self.warn_3) + " seconds left!")
            print(self.time-(i))
            time.sleep(1)
