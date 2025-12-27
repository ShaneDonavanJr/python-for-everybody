class Talker :
    """
    Docstring for Talker
    This class is for talking
    """
    def __init__(self):
        self.level = 0

    def level_up(self):
        self.level = self.level + 1
    
    def level_down(self):
        self.level = self.level - 1

    def say_hello(self):
        
        if self.level == 0:
            print("hi")
        elif self.level == 1:
            print("Hello")
        elif self.level == 2:
            print("What up bro!")
        elif self.level > 2:
            print("You are my world, hello world!")
        else:
            print("uhhh..") 

    def __del__(self):
        print(f"A talker has fallen at level {self.level}")
    

t = Talker()

t.say_hello()
t.level_up()
t.say_hello()
t.level_up()
t.say_hello()
t.level_up()
t.say_hello()
t.level_down()
t.say_hello()
t = "Death"
print(t)