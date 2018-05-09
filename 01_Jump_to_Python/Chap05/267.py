class Calculator:
    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        sum = 0
        for i in self.nums:
            sum += i
        return print(sum)

    def avg(self):
        return print(sum(self.nums)/len(self.nums))

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()
