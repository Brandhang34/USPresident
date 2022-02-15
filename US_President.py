first_Name = input("Enter a first name: ") 
found_Flag = False

infile = open("USPres.txt", 'r')

for line in infile:
    if line.startswith(first_Name + ' '):
        print(line.rstrip())
        found_Flag = True

if not found_Flag:
    print("No president had the first name" , first_Name + '.')