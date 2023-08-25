# Lab02
# ● Write a function that accepts two arguments (length, start) to 
# generate an array of a specific length filled with integer numbers 
# increased by one from start.

def generate_array(length, start):
    array = []
    for i in range(length):
        array.append(start)
        start += 1
    return array

print(generate_array(5, 2))

# ● write a function that takes a number as an argument and if the 
# number divisible by 3 return "Fizz" and if it is divisible by 5 return 
# "buzz" and if is is divisible by both return "FizzBuzz"

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number

print(fizz_buzz(15))
print(fizz_buzz(5))
print(fizz_buzz(3))

# ● Write a function which has an input of a string from user then it 
# will return the same string reversed.

def reverse_string(string):
    return string[::-1]

print(reverse_string("Hossam"))


# ● Ask the user for his name then confirm that he has entered his 
# name(not an empty string/integers). then proceed to ask him for 
# his email and print all this data (Bonus) check if it is a valid email 
# or not

def get_user_data():
    name = input("Please enter your name: ")
    while name == "":
        name = input("Please enter valid name: ")
    email = input("Please enter your email: ")
    while email == "" or "@" not in email:
        email = input("Please enter valid email: ")
    return name, email

get_user_data()

# ● Write a function that takes a string and prints the 
# longest alphabetical ordered substring occurred For example, if 
# the string is 'abdulrahman' then the output is: Longest substring in 
# alphabetical order is: abdu

def longest_substring(string):
    substrings = []

    current_alpha = ""

    for i in range(len(string)):
        if i == 0 :
            continue
        if string[i] > string[i-1] :
            current_alpha += string[i-1]
            print("char ",string[i])
            print("current ",current_alpha)
            continue
       
        current_alpha += string[i-1]
        if (len(string)-1) == i:
            current_alpha += string[i+1]
        substrings.append(current_alpha)
        current_alpha = ""

    print(max(substrings,key=len))  
    print(substrings)


longest_substring("abdulrahman")





# ● Write a program which repeatedly reads numbers until the user 
# enters “done”.

 # ○ Once “done” is entered, print out the total, count, and 
 # average of the numbers.

 # ○ If the user enters anything other than a number, detect their 
 # mistake, print an error message and skip to the next number.

def calculate_enter():
    total = 0
    count = 0
    while True:
        new_enter = input("enter new number : ")
        if new_enter == "done":
            print("average: ",(total/count))
            print("count: ",count)
            print("total: ",total)
            break
        elif (isinstance(new_enter ,(int,float) ) or new_enter.isdigit) and not new_enter == '':
            new_enter = int(new_enter)
            count +=1
            total += new_enter
        else :
            print("wrong enter please enter digit or 'done' ")
            print(type(new_enter))

calculate_enter()




# ● Word guessing game (hangman)
 # ○ A list of words will be hardcoded in your program, out of 
 # which the interpreter will



#  # ○ choose 1 random word.
#  # ○ The user first must input their names
#  # ○ Ask the user to guess any alphabet. If the random word 
#  # contains that alphabet, it

#  # ○ will be shown as the output(with correct placement)

#  # ○ Else the program will ask you to guess another alphabet.

 # ○ Give 7 turns maximum to guess the complete word.

 
words = ("ahmed","mohammed","Noha")

def hangman():
    word = words[0]
    print(word)
    turns = 7
    guessed_letters = []
    guessed_word = "_"
    while turns > 0:
        guess = input("Please enter your guess: ")
        if guess in word:
            guessed_letters.append(guess)
            print("you guessed right")
            guessed_word = ""
            for i in word:
                if i in guessed_letters:
                    guessed_word += i
                else:
                    guessed_word += "_"
            else:
                print(guessed_word)
        else:
            print("you guessed wrong")
            print("you have ",turns," turns left")
        if "_" not in guessed_word:
            print("you won")
            break
        turns -= 1
        if turns == 0:
            print("you lost")
            break

hangman()    




