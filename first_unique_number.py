class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cache = Counter(nums)
        self.uniques = deque(nums)

    def showFirstUnique(self) -> int:
        while self.uniques and self.cache[self.uniques[0]] != 1: 
            self.uniques.popleft()
        return self.uniques[0] if self.uniques else -1

    def add(self, value: int) -> None:
        self.cache[value] += 1
        self.uniques.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)