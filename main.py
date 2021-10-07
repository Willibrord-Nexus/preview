class App(object):
    def __init__(self) -> None:
        print("life sucks")
        super().__init__()

    def test_operations(self) -> int:
        a = 1
        b = 4
        return a + b

    '''
    returns the sum of a and b (wich are numbers)
    '''
    def test_parameters(self, a:int, b:int) -> int:
        return a + b

    def test_numbers(self):
        a:float = 0.5
        b:int = 10

        c:float = b + a
        print(c)

        d:float = 14978.3832742
        e:int = int(d)
        print(d)
        print(e)

    def if_statement(self, check:bool) -> bool:
        if bool:
            print("the statement is true")
            return True
        else:
            print("the statement is false")
            return False

    '''
    only return the values that are even
    '''
    def solve_simple_problem(self, check_for_even:bool):
        arr = [4,6,8,2,5,3,24,56,235,568,23,734,234,753,123,436523,324,54,23,56,234,452]

        dummy = []
        for num in arr:
            if num % 2 == 0 and check_for_even:
                dummy.append(num)
            elif num % 2 != 0 and not check_for_even:
                dummy.append(num)

        return dummy

    def sort(self, collection: list) ->list:
        for insert_index, insert_value in enumerate(collection[1:]):
            temp_idx = insert_index
            while insert_index >= 0 and insert_value < collection[insert_index]:
                collection[insert_index + 1] = collection[insert_index]
                insert_index -= 1
            if insert_index != temp_idx:
                collection[insert_index + 1] = insert_value
        return collection



if __name__== "__main__":
    app = App()

    print("1 + 4 =", app.test_operations())
    print(app.test_parameters(6, 1000))
    app.test_numbers()

    app.if_statement(True)
    app.if_statement(False)

    print(app.solve_simple_problem(False))

    import random
    import time

    def current_milli_time():
        return round(time.time() * 1000)

    l:list = []
    print("filling list...")
    for i in range(10000):
        l.append(random.randint(0, 50000))
    print("list filled!")
    print("sorting...")
    
    before = current_milli_time()

    _list = app.sort(l)

    after = current_milli_time()

    print(_list)

    print("done!")
    print(f"Finished in {after - before}ms")




