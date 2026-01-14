from enum import nonmember


##a=20
# b=10

# def grom(a):
#    if a == b:
#        return
#    grom (a-1)
#    print(a)

##grom(a)


# def cou_n(i):
#   if i=="":
#      return 0
# return 1 + cou_n(i[1:])
# text= "Over is over"
# print(cou_n(text))

li = [1, 2, 3, 4, 5]


def listing(lis):
    if not lis:
        return 0
    return lis[0] + listing(lis[1:])


print(listing(lis))


def back(i):
    if len(i) <= 1:
        return i
    return i[-1] + back(i[:-1])


text = "Over is over"
print(back(text))
