file=open("devices.txt","a")

while True:
    newItem=input("New device to add: ")
    if newItem == 'q' or newItem == 'exit':
        print("All done!")
        break
    else:
        file.write(newItem + "\n")


file.close()
