# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number


def numbers_in_lists(string):
    length = len(string)
    i = 0
    numstring = []
    while i < length:
        numstring.append(int(string[i]))
        i += 1
    i = 0
    list = []
    sublist = []
    while i < length:
        if i != 0:
            if numstring[i] > lastNum:
                lastNum = numstring[i]
                list.append(numstring[i])
                sublist = []
            elif numstring[i] <= lastNum:
                sublist.append(numstring[i])
                if sublist != list[len(list) - 1]:
                    list.append(sublist)
        else:
            list.append(numstring[i])
            lastNum = numstring[i]
        i += 1
    return list


print(numbers_in_lists('455532123266'))
print(numbers_in_lists('543987'))
print(numbers_in_lists('987654321'))
print(numbers_in_lists('123456789'))

