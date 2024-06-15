ep1 = {122: 82, 156: 89, 182: 91, 270: 82, "harry":59}
# ep2 = {333: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()
# del ep1[122]

# print(ep1)

def add():
        key = input("Enter Name : ")
        val = int(input("Enter Age : "))
        dic.update({key:val})


dic = {}

addItem = int(input("Add key-values press(1) or (0) to exit : "))

for i in range(3):
    if len(dic) == 3:
          print("\n\n", dic)
          break
    else:
        if addItem == 1:
            add()
            List = int(input("List of keys/values press(1) : "))
            if List == 1:
                # print(dic.items())
                for key, value in dic.items():
                    print(f"The value corresponding to the key {key} is {value}")
                options = int(input("\nRemove key press(2)\nChange Value of the key press(3)\npress 0 to exit : "))
                if options == 2:
                    remove = input("Enter key to remove: ")
                    del dic[remove]
                    # add = print(input("Add the Key: "))
                elif options == 3:
                    name = input("Enter key name: ")
                    change = input("Enter new value: ")
                    dic[name] = change
                    print("Successfully Works!")
                elif options == 0:
                    break
        elif addItem == 0:
            break
        else:
            print("Wrong Input!")

