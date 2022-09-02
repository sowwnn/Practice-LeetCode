class Foo:
    def __init__(self):
        self.first_exc = False
        self.second_exc = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_exc = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.first_exc:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_exc = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_exc:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
