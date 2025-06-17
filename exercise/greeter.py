class GREETER: 
    def __init__(self):
        self.name = ""

    def ask_name(self):
      self.name = input("enter your name: ")
     
    def output(self): 
       print(f"hello,{self.name}! welcome to python.")  

obj = GREETER()
       
obj.ask_name()
obj.output()