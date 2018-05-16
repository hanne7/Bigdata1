class Calculator:
    def __init__(self, num_list):
        self.num_list = num_list

    def sum(self):
        sum = 0
        for i in self.num_list:
            sum += i
        return sum

    def avg(self):
        return self.sum()/len(self.num_list)

if __name__ == "__main__":
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())

    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())
