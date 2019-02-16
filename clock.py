from datetime import timedelta, datetime


class Clock(object):
    def __init__(self, hour, minute):
        self.time = datetime(2019,1,1,0,0) + timedelta(hours=hour, minutes=minute)

    def __repr__(self):
        return str(self.time.time())[:-3]

    def __eq__(self, other):
        return self.time.time() == other.time.time()

    def __add__(self, minutes):
        return str((self.time + timedelta(minutes=minutes)).time())[:-3]

    def __sub__(self, minutes):
        return str((self.time - timedelta(minutes=minutes)).time())[:-3]
