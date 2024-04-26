import turtle

class Point(object):
    
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
        
    def draw_action(self):
        turtle.dot()

#p = Point(1, 2, "blue")
#p.draw()

class Box(Point):
        
    def __init__(self, x1, y1, width, height, color):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
        super().__init__(x1, y1, color)

    def draw_action(self): #Creates an empty box
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

#b = Box(20, 20, 50, 50, "red")
#b.draw()
    
class Boxfilled(Box): #Creates a full box
    
    def __init__(self, x1, y1, width, height, color, fillcolor):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
        self.fillcolor = fillcolor
        super().__init__(x1, y1, width, height, color)

    def draw_action(self):
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        Box.draw_action(self)
        turtle.fillcolor(self.fillcolor)
        turtle.end_fill()

#Bf = Boxfilled(1, 2, 100, 100, "red", "blue")
#Bf.draw()

class Circle(Point):
        
    def __init__(self, x1, y1, radius, color):
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        self.color = color
        super().__init__(x1, y1, color)

    def draw_action(self): #Creates an empty circle
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.circle(self.radius)

#c = Circle(20, 20, 50, "blue")
#c.draw()

class Circlefilled(Circle):
    
    def __init__(self, x1, y1, radius, color, fillcolor):
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        self.color = color
        self.fillcolor = fillcolor
        super().__init__(x1, y1, radius, color)

    def draw_action(self): #Creates a full circle
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        Circle.draw_action(self)
        turtle.fillcolor(self.fillcolor)
        turtle.end_fill()
        
#cf = Circlefilled(20, 20, 50, "red", "blue")
#cf.draw()


