

def eq(a, b, c):
    if int(a) != int(b):
        if int(a) != int(c):
            if int(b) != int(c):
                return False
            else:
                return True
        else:
            return True
    else:
        return True



print(eq("1",0,1))