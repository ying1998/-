while True:
    guest_name=input("dear guest ,please input your infotmation : name \n>>")
    with open("guest_name.txt","a") as file_object:
        file_object.write("%s\n"%guest_name)
    ifbreak = input(">>input quit you can quit >>>")
    if ifbreak == 'quit':
        break
    else:
        print("continue~~~~~~")
