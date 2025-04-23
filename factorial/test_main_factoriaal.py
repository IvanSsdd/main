from main import(
    factorial,
    is_prime,
    unique_element,
    sort
)

def test_factorials():
    assert factorial(5) == 120
    assert factorial(-1) == None
    assert factorial(10) == 3628800
    assert factorial(7) == 5040
    assert factorial(2) == 2
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(-5) == None
    assert factorial(3) == 6

def test_is_primes():
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(13) == True
    assert is_prime(9) == False
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(19) == True
    assert is_prime(15) == False
    assert is_prime(7) == True
    assert is_prime(0) == False
    assert is_prime(23) == True

def test_unique_elements():
    assert unique_element([1, 2, 3, 3, 4]) == [1, 2, 3, 4]
    assert unique_element(['a', 'b', 'b']) == ['a', 'b']
    assert unique_element([5, 5, 5, 5]) == [5]
    assert unique_element([1, 1, 2, 3, 3]) == [1, 2, 3]
    assert unique_element(['x', 'y', 'x']) == ['x', 'y']
    assert unique_element([10, 20, 20]) == [10, 20]
    assert unique_element([True, False, True]) == [True, False]
    assert unique_element(['cat', 'dog', 'cat']) == ['cat', 'dog']
    assert unique_element([1.1, 2.2, 1.1]) == [1.1, 2.2]
    assert unique_element([0, 0, 1]) == [0, 1]

def test_sorts():
    assert sort(words = ["apple"]) == {5: ["apple"]}
    assert sort(words = ["яблоко"]) == {6: ["яблоко"]}
    assert sort(words = ["hi"]) == {2: ["hi"]}
    assert sort(words = ["привет"]) == {6: ["привет"]}
    assert sort(words = ["code"]) == {4: ["code"]}
    assert sort(words = ["код"]) == {3: ["код"]}
    assert sort(words = ["test"]) == {4: ["test"]}
    assert sort(words = ["тест"]) == {4: ["тест"]}
    assert sort(words = ["python"]) == {6: ["python"]}
    assert sort(words = ["питон"]) == {5: ["питон"]}