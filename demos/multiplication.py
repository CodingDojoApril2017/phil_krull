rowStr = ''
for x in range(13):
    rowStr += str(x)
    # print x
print rowStr


for y in range(1, 13):
    prodStr = ''
    prodStr += str(y)

    for k in range(1,13):
        prodStr += str(k * y)

    print prodStr
