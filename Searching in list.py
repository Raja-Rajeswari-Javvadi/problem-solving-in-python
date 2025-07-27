#list searching 
if "Raji" in li:
    print("Exists")
else:
    print("Not exists")
#using loop
key="Jyothi"
flag=False
for i in li:
    if i==key:
        flag=True
        break
if flag:
    print("Exits")
else:
    print("Not exists")
#using any()
flag=any(x=="Shannuu" for x in li)
if flag:
    print("Exits")
else:
    print("Not exists")
#count()
if li.count("Raji")>0:
    print("Exits")
else:
    print("Not exists")
