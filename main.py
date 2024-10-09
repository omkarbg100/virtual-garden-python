import os

work=input("if you wan to know information about som plant then type 'I' \n if you want to add info about any plant type 'N'\n")
if(work=='I'):
    x=input("enter the name of plant you want to know about : ")
    y=f"{x}.txt"
    l=os.listdir()
    print(l)
    if y in l:
        print("::::::  we found out ::::::")
        with open(y,'r') as f:
            print(f.read(), end="\n") 
    else:
        for i in l:
            if x in i:
                print(i.removesuffix(".txt"),end=" ")
        print(f"XXXX sorry we didnt find any plant name {x} in our data base")
else:
    x=input("enter the name of plant you want to know about : ")
    y=f"{x}.txt"
    l=os.listdir()
    if y in l:
        print("this information about this plant already exists ")
    else:
        with open(y,'a') as f:
            f.write(y)
            a=input("enter the type of the plant : ")
            f.write(f"type of plant : {a}\n")
            a=input("where the plants are aminly grown : \n")
            f.write(f"mostly found in : {a}\n")
            a=input(" enter its medicenal use : ")
            f.write(f"medicenal uses : {a}")
            a=input("tell some additional info about it : ")
            f.write(f"more info about it : {a}")
            print("::::::: thankyou for such a wonderfull information it has help alot for us to increas the data:::::::")



