import math

def compute_circle_area(radius): #25.6
    return radius**2 * math.pi

x = '25.6'

def get_user_radius():
    user_string = input('please enter a radius: ')
    return float(user_string)

r = get_user_radius()
area = compute_circle_area(r)
print(area)
# x_num = compute_circle_area(float(x))

print(x)