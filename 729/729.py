class MyCalendar:

    def __init__(self):
        self.checkbook = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.checkbook:
            if((s < end)&(e > start)):
                return False
        self.checkbook.append([start,end])
        return True
