class Time:
    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if self.seconds + 1 <= self.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes + 1 <= self.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours + 1 <= self.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0
        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())
