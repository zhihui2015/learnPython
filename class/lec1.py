class Animals():
    def breathe(self):
        print("breathing")
    def move(self):
        print("moving")
    def eat(self):
        print("eating food")


class Mammals(Animals):
    def breastfeed(self):
        self.eat()
        print("feeding young")


class Cats(Mammals):
    def __init__(self, spots):
        self.spots = spots
    def catch_mouse(self):
        print("catch mouse")
    def left_foot_forward(self):
        print("left foot forward")
    def left_foot_backward(self):
        print("left foot backward")
    def dance(self):
        self.move()
        self.left_foot_forward()
        self.left_foot_backward()
        self.left_foot_forward()
        self.left_foot_backward()


kitty = Cats(10)
print(kitty.spots, kitty.dance(), kitty.breastfeed())

