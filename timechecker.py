import time
current=str(list(time.ctime()))
file=open("date.txt","r")
file2=file.readlines()
print(file2)
if len(file2)<1:
    file.close()
    file=open("date.txt","w")
    file.write(current)
    print("Have fun waiting!")
else:
    before=file.readlines()
    premin=int(before[10:12])
    nowmin=int(current[10:12])
    wait=nowmin-premin
    print("You have waited for ",wait," hours17")
file.close()
#day=current[0:3]
#month=current[4:7]
#ddmm=[day,month]
#print(ddmm)
