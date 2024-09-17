from ArrayListt import ArrayList

print("\n**********CHECK UNICODE**********\n")

test = ArrayList('u', 'a', 'b', 'c', 'd', 'f')
# getitem check
print("\n----getitem check----\n")
print(test[4])
#сontains check
print("\n----сontains check----\n")
b = test.__contains__('k')
print(b)
# len check
print("\n----len check----\n")
b = len(test)
print(b)
#count
print("\n----count----\n")
a = test.count('a')
print(a)
# index
print("\n----index----\n")
indc = test.index('c')
print(indc)
#iter__ check
print("\n----iter__ check----\n")
s = ''
itt = [_ for _ in test]
print(s.join(itt))
#reversed
print("\n----reversed----\n")
s = ''
verg = [_ for _ in test]
print(s.join(verg))
rev = reversed(test)
gerv = [_ for _ in rev]
print(s.join(gerv))


print("\n**********CHECK INT**********\n")

test = ArrayList('i', 1, 2, 3, 6, 4)
# getitem check
print("\n----getitem check----\n")
print(test[4])
#сontains check
print("\n----сontains check----\n")
b = test.__contains__('k')
print(b)
# len check
print("\n----len check----\n")
b = len(test)
print(b)
#count
print("\n----count----\n")
a = test.count('a')
print(a)
# index
print("\n----index----\n")
indc = test.index('c')
print(indc)
#iter__ check
print("\n----iter__ check----\n")
s = ''
itt = [str(_) for _ in test]
print(s.join(itt))
#reversed
print("\n----reversed----\n")
s = ''
verg = [str(_) for _ in test]
print(s.join(verg))
rev = reversed(test)
gerv = [str(_) for _ in rev]
print(s.join(gerv))

print("\n**********CHECK FLOAT**********\n")

test = ArrayList('f', 0.7, 1.4, 3.0)
# getitem check
print("\n----getitem check----\n")
print(test[2])
#сontains check
print("\n----сontains check----\n")
b = test.__contains__(1.4)
print(b)
# len check
print("\n----len check----\n")
b = len(test)
print(b)
#count
print("\n----count----\n")
a = test.count(3.0)
print(a)
# index
print("\n----index----\n")
indc = test.index(3.0)
print(indc)
#iter__ check
print("\n----iter__ check----\n")
itt = [str(_) for _ in test]
print(itt)
#reversed
print("\n----reversed----\n")
verg = [str(_) for _ in test]
print(verg)
rev = reversed(test)
gerv = [str(_) for _ in rev]
print(gerv)