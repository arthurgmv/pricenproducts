products = ("pen", 1,
            "pencil", 1,
            "notebook", 10,
            "book", 20,
            "ereaser", 2)
print ("--"*30)
print ("Products & Prices")
print ("--"*30)
for position in range (0, len(products)):
    if position % 2 == 0:
        print (f"{products[position]:.<30}", end=" ")
    else:
        print (f"US${products[position]:>3}")
print ("--"*30)
print ("End")
print ("--"*30)
input ("Press enter to leave the program ")
