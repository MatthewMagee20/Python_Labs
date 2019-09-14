class Clock:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):

        newSeconds = self.seconds + other.seconds
        newMinutes = self.minutes + other.minutes
        newHours = self.hours + other.hours

        if newSeconds > 60:
            newSeconds = newSeconds - 60
            newMinutes += 1

        if newMinutes > 60:
            newMinutes = newMinutes - 60
            newHours += 1

        if newHours > 24:
            newHours = newHours - 24

        return 'Added time = ' +str(newHours) + ':' + str(newMinutes) + ':' + str(newSeconds)

    def __str__(self):
        return str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)


c1 = Clock(12, 24, 24)
c2 = Clock(24, 2, 6)
added = c1 + c2

print(c1)
print(c2)
print(added)


