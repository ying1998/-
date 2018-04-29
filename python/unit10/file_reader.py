with open('millions.txt') as file_object:

    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

birthday = input("Enter your birthday , in the form mmddyy: ")
if birthday in pi_string:
    print("apears !")
else:
    print("sorry ~")
