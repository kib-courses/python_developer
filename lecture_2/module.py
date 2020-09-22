def hello():
    print('Hello, world!')

def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

def ex():
    if __name__ == "__main__":
        hello()
        for i in range(10):
            print(fib(i))
    else:
        print("not in __main__")
        print(__name__)
        
        
print("all run")