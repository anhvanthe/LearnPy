# Calculate Area of a circle with radius r in easy way and in hard way

import math
import turtle

def get_radius(radius):
    pass



def print_a_cicle(n):
    for i in range(n):
        for j in range(n + 1):
            if ((j <= 1 or j <= n) and (i != 0 and i != (n-1)):
                print('*', end='')

            elif((i > n–2) and (j > 0 and j < n)):
                print('*', end='')
            else:
                print(end=' ')
                print()
    # row = 6
    # col = 6
    #
    # for i in range(0, row):
    #     for j in range(0, col):
    #         if ((j == 0 or j == col - 1) and (i != 0 and i != row - 1)):
    #             print('*', end='')  # end='' so that print statement should not change the line.
    #         elif (((i == 0 or i == row - 1) and (j > 0 and j < col - 1))):
    #             print('*', end='')
    #         else:
    #             print(end=' ')  # to print the space.
    #
    #     print()  # to change the line after iteration of inner loop.

def calculate_area(radius):
    """
    :param radius:
    """
    area = math.pi * radius * radius
    return radius, area


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_a_cicle(5)
    # turtle.circle(100)
    # r = 0
    # A = 0
    # r, A = calculate_area(5)
    # A = float("{:.2f}".format(A))
    # print(" Area of circle radius " + str(r) + " is: " + str(A))
