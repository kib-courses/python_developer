from ArrayList import ArrayList

print("ArrayList('abc', 'df')")
test = ArrayList('abc', 'df')
test.print()
# __getitem check
print("GetItem - test[4]")
print(test[4])
# __iter__ check
print("Iter - iter(test)")
print(iter(test))
# Contains check
print("Contains - test.__contains__(4)")
b = test.__contains__(4)
print(b)
print("__len__ - len(test)")
# __len__ check
b = len(test)
print(b)
print("Count - test.count('d')")
# count
print(test.count('d'))
print("index - test.index('c')")
# index
print(test.index('c'))
print("reverse - test.reverse()")
# Reverse and reversed
test.reverse()
test.print()
print("reversed - reversed(test)")
reversed(test)
test.print()
print("extend - test.extend(test2)")
test2 = ArrayList("efj")
test.extend(test2)
test.print()
print("extend - test.extend('ff')")
test.extend('ff')
# remove
print("Remove - ")
test.remove('d')
# pop
print("pop - test.pop(2")
test.pop(2)
test.print()
# insert
print("Insert - test.insert(0, ['o', 'aaaa'])")
test.insert(0, ['o', 'aaaa'])
test.print()
print("Insert - test.insert(3, 'k')")
test.insert(3, 'k')
print("Append - test.append('daa')")
test.append('daa')
test.print()

print("ArrayList(1,2,3)")
test = ArrayList(1, 2, 2, 3)
test.print()
# __getitem check
print("GetItem - test[2]")
print(test[2])
# __iter__ check
print("Iter - iter(test)")
print(iter(test))
# Contains check
print("Contains - test.__contains__(2)")
b = test.__contains__(2)
print(b)
print("__len__ - len(test)")
# __len__ check
b = len(test)
print(b)
print("Count - test.count(2)")
# count
print(test.count(2))
print("index - test.index(3)")
# index
print(test.index(3))
print("reverse - test.reverse()")
# Reverse and reversed
test.reverse()
test.print()
print("reversed - reversed(test)")
reversed(test)
test.print()
print("extend - test.extend(test2)")
test2 = ArrayList(4,5,6)
test.extend(test2)
test.print()
print("extend - test.extend(7)")
test.extend(7)
# remove
print("Remove - test.remove(3)")
test.remove(3)
# pop
print("pop - test.pop(2")
test.pop(2)
test.print()
# insert
print("Insert - test.insert(0, [1, 2, 3])")
test.insert(0, [1, 2, 3])
test.print()
print("Insert - test.insert(3, 10)")
test.insert(3, 10)
print("Append - test.append(22)")
test.append(22)
test.print()


print("ArrayList(1.5, 2.4, 3.3)")
test = ArrayList(1.5, 2.4, 3.3)
test.print()
# __getitem check
print("GetItem - test[0]")
print(test[0])
# __iter__ check
print("Iter - iter(test)")
print(iter(test))
# Contains check
print("Contains - test.__contains__(0)")
b = test.__contains__(0)
print(b)
print("__len__ - len(test)")
# __len__ check
b = len(test)
print(b)
print("Count - test.count(3.3)")
# count
print(test.count(3.3))
print("index - test.index(3.3)")
# index
print(test.index(3.3))
print("reverse - test.reverse()")
# Reverse and reversed
test.reverse()
test.print()
print("reversed - reversed(test)")
reversed(test)
test.print()
print("extend - test.extend(test2)")
test2 = ArrayList(4.2,5.1,6.0)
test.extend(test2)
test.print()
print("extend - test.extend(7.9)")
test.extend(7.9)
# remove
print("Remove - test.remove(3.3)")
test.remove(3.3)
# pop
print("pop - test.pop(2")
test.pop(2)
test.print()
# insert
print("Insert - test.insert(1, [0.1, 0.2, 0.3])")
test.insert(1, [0.1, 0.2, 0.3])
test.print()
print("Insert - test.insert(4, 10.10000)")
test.insert(4, 10.10000)
print("Append - test.append(22.22)")
test.append(22.22)
test.print()

print("Исправление ошибок")
test = ArrayList(1,2,3,4,5,6)
test.print()
test.insert(-2, 35)
test.print()
test[1::1]
test.print()
test[1:5:2]
test.print()

test = ArrayList('aa', 'bb', 'cc')
test.print()
test[1::1]
test.print()
test = ArrayList()
test.print()
test.append('gg')
test.print()