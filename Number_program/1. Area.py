def main():
    user_1 = float(input("Enter Length: "))
    user_2 = float(input("Enter Breadth: "))

    area_rect, area_square_1, area_square_2 = area(user_1, user_2)

    print(f"Area of Rectangle: {area_rect}")
    print(f"Area of Square 1: {area_square_1}")
    print(f"Area of Square 2: {area_square_2}")

def area(l, b):
    area_rect = l * b
    area_square_1 = l * l
    area_square_2 = b * b
    return area_rect, area_square_1, area_square_2




