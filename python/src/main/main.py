from python.src.main.Person import Person


def main():
    print("Hello Mark, welcome to the world of development")
    print("To run this class what you need to do is to right click")
    print("on the main method and press run")
    print("A terminal will pop up at the bottom with the contents of the main method")
    print("play around and see what you can do to start")

    numbers = range(0, 100, 10)

    for number in numbers:
        print 'I have seen %d women who I love today' % number

    mark = Person("mark", "holmes", 23, "bellend")
    mark.say_hello()

    print("marks a bellend")


if __name__ == '__main__': main()
