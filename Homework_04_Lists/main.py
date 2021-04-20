


myUniqueList = []
myLeftoversList = []

def addToList(i):
    if i in myUniqueList:
        addToLeftovers(i)
        return True
    else:
        myUniqueList.append(i)
        return False


def addToLeftovers(i):
    myLeftoversList.append(i)


print(addToList(1))
print(addToList("A"))
print(addToList(2))
print(addToList(1))
print(addToList(4))
print(addToList(5))
print(addToList("B"))
print(addToList(3))
print(addToList(6))
print(addToList(5))
print(addToList("A"))
print(addToList(3))
print(addToList(5))
print(addToList(2))
print(myUniqueList)
print(myLeftoversList)