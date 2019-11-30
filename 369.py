class StockTracker():
    def __init__(self, dry_run=False, verbose=False):
        self.data = {}

    def add(self, timestamp, price):
        self.data[timestamp] = price

    def update(self, timestamp, price):
        self.data[timestamp] = price

    def remove(self, timestamp):
        del self.data[timestamp]

    def min(self):
        return min(self.data.values())

    def max(self):
        return max(self.data.values())

    def average(self):
        total_price = 0
        for time in self.data:
            total_price += self.data[time]
        return total_price / len(self.data)
