""" 
Task 2 

In this task I will be use turtle librarry
"""
import turtle


def koh_algo(obj, order=4, size=100):
    """ koh algorithm """
    
    if order == 0:
        obj.forward(size)
    else:
        size /= 3
        koh_algo(obj, order-1, size)
        obj.left(60)
        koh_algo(obj, order-1, size)
        obj.right(120)
        koh_algo(obj, order-1, size)
        obj.left(60)
        koh_algo(obj, order-1, size)


def snizhynka(obj, order, size):
    """ koh algorithm handler """

    for _ in range(3):
        koh_algo(obj, order, size)
        obj.right(120)


def main():
    """ main function """
    
    window = turtle.Screen()
    window.bgcolor("white")
    obj = turtle.Turtle()
    obj.speed(0)
    obj.penup()
    obj.goto(-200, 100)
    obj.pendown()
    snizhynka(obj, 4, 400)
    obj.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
