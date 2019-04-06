# Author:hxj

def num_div(num1, num2):
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1 / num2)


if __name__ == '__main__':
    num_div(100, 50)
