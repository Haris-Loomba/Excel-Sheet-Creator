import pandas as pd

print("Hey! This is a excel sheet customizer!\nEnter words as the computer says, and then you will have a excel sheet in no time")
print()
dict1 = {

}
col = int(input("Enter no of columns: "))
row = int(input("Enter no of rows: "))
for i in range(1, col+1):
	cname = input(f"Enter column name {i}: ")
	dict1[cname] = []
print(dict1)	
for i in range(row):
	print("Enter detail for row %d."%(i+1))
	for j in dict1:
		item = input("Enter value for %s column: "%j)
		dict1[j].append(item)

print()
print("The process is complete!")
nameFile = input("What would you like to keep the name of the file? ").replace(' ','-')
df = pd.DataFrame(dict1)
df.to_csv(f'{nameFile}.csv')
