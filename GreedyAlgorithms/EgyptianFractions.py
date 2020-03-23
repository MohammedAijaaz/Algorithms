import math


def main():

    nr = int(input("Enter the Numerator = "))
    dr = int(input("Enter the Denominator = "))

    print("{}/{}".format(nr, dr))

    denoms = []

    while nr > 0:
        x = math.ceil(dr/nr)
        denoms.append(x)
        nr = nr*x - dr
        dr = dr * x

    for i in denoms:
        print("{}/{} ".format(1, i))


if __name__ == "__main__":
    main()
