from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.arrival= {}
        self.destination= defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrival[id]= (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        arr_station=self.arrival[id][0]
        arr_time= self.arrival[id][1]
        self.destination[(arr_station, stationName)].append(t-arr_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        get=self.destination[(startStation, endStation)]
        avg = sum(get)/len(get)
        return avg

undergroundSystem=UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");    #     // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");       #    // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");       #   // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");       #  // return 12.00000


