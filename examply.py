temperature = 20

def print_temperature():
    print(temperature)
def test_print_temperature():
    assert 1+2 == 3
    
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    return a - b  # <--- fix this 


uncomment the following test
def test_subtract():
   assert subtract(2, 3) == -1
