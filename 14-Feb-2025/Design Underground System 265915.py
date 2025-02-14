# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.time_taken = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        # making sure the travler is checked in only once
        # storing id: (stationName, t)
        if self.checkins.get(id) is None:
            self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        # storing (startStation, endStation): (totalTime, trips)
        start_station, checkin_time = self.checkins[id]
        time_taken = t - checkin_time

        # checking if the trip is registered first
        if self.time_taken.get((start_station, stationName)) is not None:
            total_time, trips = self.time_taken[(start_station, stationName)]
            self.time_taken[(start_station, stationName)] = (total_time + time_taken, trips + 1)

        else:
            self.time_taken[(start_station, stationName)] = (time_taken, 1)

        # removing travleer from checkins cause he checkedout
        del self.checkins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        # dividing the total time for trips
        total_time, trips = self.time_taken[(startStation, endStation)]

        return total_time / trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)