print("please input two numbers :")
print("Enter q to quit")


while True:
    print("the first number is :")
    firstnumber = input(">")
    if firstnumber == 'q':
        break
    else:
        try:
            no_1 = int(firstnumber)
        except :
            print("please input numbers")
        else:
            print("the secondnumber is :")
            secondnumber = input(">")
            if secondnumber == 'q':
                break
            else:
                try:
                    no_2 = int(secondnumber)
                except :edrthb
                    print("please input numbers")
                else:
                    result = no_1 + no_2
                    print("the result is %s " %result)

    pass
