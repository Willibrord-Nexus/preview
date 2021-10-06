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
        arr = [4,6,7,8,2,5,3,24,56,235,568,23,734,234,753,123,436523,324,54,23,56,234,452]

        dummy = []
        for num in arr:
            if num % 2 == 0 and check_for_even:
                dummy.append(num)
            elif num % 2 != 0 and not check_for_even:
                dummy.append(num)

        return dummy

    def sort(self, collection: list) ->list:
        if len(collection) <= 1:
            return
        piv = collection.pop()
        high:list[int] =[]
        low:list[int] =[]
        for elem in collection:
            (high if elem > piv else low).append(elem)
        return self.sort(low) + piv + self.sort(high)



if __name__== "__main__":
    app = App()

    print("1 + 4 =", app.test_operations())
    print(app.test_parameters(6, 1000))
    app.test_numbers()

    app.if_statement(True)
    app.if_statement(False)

    print(app.solve_simple_problem(False))

    app.sort([3,35,56,576,874,23,73,4,73,23,7234,6,35,62,3638,313,71])




