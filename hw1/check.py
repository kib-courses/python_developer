from hw1.source import arraylist

if __name__ == "__main__":
    a = arraylist('i', [1, 2, 3, 4, 5])
    for i in reversed(a):
        print(i)
    a.insert(3, 3)
    print(a.arraylist)

    a.insert(0, 0)
    print(a.arraylist)

    a.extend([6,7,8])
    print(a.arraylist)

    a.append(9)
    print(a.arraylist)

    a.remove(9)
    print(a.arraylist)

    print(a.arraylist.count(3))

    print(a.pop(9))
    print(a.arraylist)

    a[1] = 11
    print(a.arraylist)

    a += 8
    print(a.arraylist)

    a+= [9,10]
    print(a.arraylist)

    del a[1]
    print(a.arraylist)
