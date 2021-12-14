"""
num = int(input())


def fibonacci(n):
    # complete the recursive function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(num):
    print(fibonacci(i))


"""


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return self.name + ' (' + str(self.capacity) + 'L)'

    def __add__(self, other):
        return Juice(self.name + " & " + other.name, self.capacity + other.capacity)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
c = Juice("Peach", 1.0)

result = a + b + c
print(result)

