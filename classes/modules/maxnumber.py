class MaxNumber:
    def __init__(self,numbers):
        self.numbers = numbers
        numbers = [10,3,6,2]
   
    def find_max(self):
        max = self.numbers[0]
        for number in self.numbers:
            if number >max:
                max = number
        print('find_max')   


number1 = MaxNumber(10)
number1.find_max()            