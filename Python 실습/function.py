def add(a,b):
    return a+b
print(add(3,5))

def say():
    return 'HI'

a=say()
print(a)

def addMany(*argc):
    result = 0
    for i in argc:
        result = result + i
    return result

result = addMany(1,2,3,4,5,6,7)
print(result)
