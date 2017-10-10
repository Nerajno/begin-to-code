for i in range(0, 9):
    print("\033[%dmI am the number %d.\033[0m" % (i, i))

for i in range(31, 37):
    print("\033[%dmI am the number %d.\033[0m" % (i, i))

for i in range(41, 48):
    print("\033[%dmI am the number %d.\033[0m" % (i, i))

for i in range(90, 97):
    print("\033[%dmI am the number %d.\033[0m" % (i, i))

print("\033[5mI am \033[41mblinking and \033[35mred\033[0m\033[0m and now \033[0m I am not.")
