# word = 'paradigm'
# for i in word:
#     print(i)

# list1 = [5,10,15,20]
# list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

# for i in list1:
#     for j in list2:
#         print(i, j)

# numbers = [12,3,56,67,89,90]
# sum = 0

# for i in numbers:
#     sum += i

# print(sum)

# vehicles = ['Car','Cycle','Bus','Tempo']

# for i in vehicles:
#     if i == "Bus":
#         break
#     else:
#         print(i)

# list1 = ['Mango','Banana','Orange']
# list2 = []

# for i in list1:
#     list2.append(i)

# print(list2)

# animal_list = ["cat", "dog", "tiger", "cow"]
# for i in animal_list:
#     print(i)

# how_deep = int(input("How deep into the Fibonacci would you like to go? "))
# x = 0
# y = 1
# z = y  
# count = 1
 
# while count <= how_deep:
#     print(f"{z} ")
#     count += 1
#     x, y = y, z
#     z = x + y


user1 = input("User1: Rock, paper or scissors? ")
user2 = input("User2: Rock, paper or scissors? ")

if user1 == "Rock" or user1 == "rock":
    if user2 == "paper" or user2 == "Paper":
        print("User2 wins!")
    elif user2 == "scissors" or user2 == "Scissors":
        print("User1 wins!")
    elif user2 == "Rock" or user2 == "rock":
        print("You chose the same. Try again!")

if user1 == "Paper" or user1 == "paper":
    if user2 == "paper" or user2 == "Paper":
        print("You chose the same. Try again!")
    elif user2 == "scissors" or user2 == "Scissors":
        print("User2 wins!")
    elif user2 == "Rock" or user2 == "rock":
        print("User1 wins!")