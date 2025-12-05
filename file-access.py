devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    #print(item)
    devices.append(item)
file.close()
print(devices)
