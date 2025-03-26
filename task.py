# num=[1,22,45,6,3,7,22,46,6,4,3,44]
# num.sort(reverse=True)
# print(num)
# print(num.index(1))
# print(len(num))

def filter_value(num):
    if(num>25):
        return True
    else:
        return False
price=[1,22,45,6,3,7,22,46,6,4,3,44]
filter_value1=filter(filter_value,price)
print(list(filter_value1))
