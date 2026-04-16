import calculator

def test_add():
    assert calculator.add(2,3) == 5

def test_subtract():
    assert calculator.subtract(10,3) == 7

def test_multiply():
    assert calculator.multiply(3,4) == 12

def test_divide():
    assert calculator.divide(10,2) == 5.0

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")