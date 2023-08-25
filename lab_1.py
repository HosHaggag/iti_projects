# Install python interpreter on your machine.

# ● Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.

vowels = ['a', 'e', 'i', 'o', 'u']
string = input("Enter a string: ")
count = 0
for i in string:
    if i in vowels:
        count += 1
print("Number of vowels in the string: ", count)


# ● Fill an array of 5 elements from the user, Sort it in descending 
# and ascending orders then display the output.


user_array = []
for i in range(5):
    user_array.append(input("Enter a number: "))
print("The array is: ", user_array)
user_array.sort()
print("The array in ascending order is: ", user_array)
user_array.sort(reverse=True)
print("The array in descending order is: ", user_array)



# ● Write a program that prints the number of times the string 'iti' 
# occurs in anystring.

string = input("Enter a string: ")
print("Number of times 'iti' occurs is: ", string.count('iti'))



# ● Write a program that remove all vowels from the input word and 
# generate a brief version of it.

string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i in vowels:
        string = string.replace(i, '')
print("The brief version of the string is: ", string)




# ● Write a program that prints the locations of "i" character in any 
# string you added.

string = input("Enter a string: ")
for i in range(len(string)):
    if string[i] == 'i':
        print("The location of 'i' is: ", i)




# ● Write a program that generate a multiplication table from 1 to the 
# number passed.

number = int(input("Enter a number: "))
for i in range(1, number+1):
    for j in range(1, 11):
        print(i, " * ", j, " = ", i*j)
    print("\n")




# ● Write a program that build a Mario pyramid like below

number = int(input("Enter a number: "))
for i in range(1, number+1):
    for j in range(number-i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print("\n")

