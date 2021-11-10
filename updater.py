c = 0

t = "y"

while t=="y":
	print(c)
	choice = input("1. Increment\n2. Decrement\nChoose: ")
	if choice == 1:
		c+=1
	elif choice == 2:
		c-=1
	else:
		print("Wrong choice!")
	t = input("Try again? (y/n): ")
	print(c) 