import time

def main():
    x = boi()
    b = x
    z = 0
    while x != 1:
        if x % 2 == 0:
            x = x/2
            print(int(x))
            z = z + 1
            time.sleep(.1)
        else:
            x = 3 * x + 1
            print(int(x))
            z = z + 1
            time.sleep(.1)
    print("It took the number ", b, ", a grand total of ", z, " steps to reach the number 1", sep="")

def boi():
    while True:
        try:
            x = int(input("positive number : "))
            if 0 >= x:
                print("Number must be positive")
                pass
            else:
                return x
        except ValueError:
            pass

main()
 