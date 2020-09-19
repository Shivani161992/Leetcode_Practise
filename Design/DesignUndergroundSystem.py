from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.entry = defaultdict(list)
        self.dest = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.entry[id]= (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        Istationname= self.entry[id][0]
        Itime= self.entry[id][1]
        self.dest[(Istationname, stationName)].append(t-Itime)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        get_time= self.dest[(startStation, endStation)]
        avgtime = sum(get_time) / len(get_time)
        return float(avgtime)

obj=UndergroundSystem()
obj.checkIn(45, "Leyton", 3)
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
obj.checkOut(27, "Waterloo", 20)
obj.checkOut(32, "Cambridge", 22)
print(obj.getAverageTime("Paradise", "Cambridge")) #14
print(obj.getAverageTime("Leyton", "Waterloo")) #11
obj.checkIn(10, "Leyton", 24)
print(obj.getAverageTime("Leyton", "Waterloo")) #11
obj.checkOut(10, "Waterloo", 38)
print(obj.getAverageTime("Leyton", "Waterloo"))   #12
