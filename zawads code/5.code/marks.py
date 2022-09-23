mylist = list(map(int, [input('Enter mark {}: '.format(i)) for i in range(1, 7)]))
mylist.sort()
print(mylist)