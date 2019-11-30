"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

You’re tracking stock price at a given instance of time. Implement an API with the following functions: add(), update(), remove(), which adds/updates/removes a datapoint for the stock price you are tracking. The data is given as (timestamp, price), where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the max/min/average of all values seen thus far.
"""


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
