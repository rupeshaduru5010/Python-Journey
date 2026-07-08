class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case Point(x = 0, y = 0):
            print("Origin")
        case Point(x = 0, y = y):
            print(f"Y = {y}")
        case Point(x = x, y = 0):
            print(f"X = {x}")
        case Point(x = x, y = y):
            print(f"SomeWhere else ({x}, {y})")
        case _:
            print("Not a Point")

where_is(Point(0, 6))            
where_is(Point(2, 5))
where_is(Point("what"))