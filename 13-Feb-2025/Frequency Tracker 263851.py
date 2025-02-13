# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.frequency_map = defaultdict(int)
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:
        frq = self.frequency_map[number]

        if frq > 0:
            self.frequencies[frq] -= 1

        self.frequency_map[number] += 1
        self.frequencies[frq + 1] += 1

    def deleteOne(self, number: int) -> None:
        if self.frequency_map.get(number) is not None:
            frq = self.frequency_map[number]
            self.frequencies[frq] -= 1

            self.frequency_map[number] -= 1

            if frq - 1 > 0:
                self.frequencies[frq - 1] += 1
            else:
                del self.frequency_map[number]

    def hasFrequency(self, frequency: int) -> bool:
        
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)