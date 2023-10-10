word = 'paradigm'
for i in word:
    print(i)

list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for i in list1:
    for j in list2:
        print(i, j)

numbers = [12,3,56,67,89,90]
sum = 0

for i in numbers:
    sum += i

print(sum)

vehicles = ['Car','Cycle','Bus','Tempo']

for i in vehicles:
    if i == "Bus":
        break
    else:
        print(i)

list1 = ['Mango','Banana','Orange']
list2 = []

for i in list1:
    list2.append(i)

print(list2)

animal_list = ["cat", "dog", "tiger", "cow"]
for i in animal_list:
    print(i)

# how_deep = int(input("How deep into the Fibonacci would you like to go? "))

# def fibonacci(num):
#     for i in range(num):
#         x = i
#         y = x
#         z = x + y
#         x = z
#         print(x)

# fibonacci(how_deep)

user1 = input("User1: Rock, paper or scissors? ")
user2 = input("User2: Rock, paper or scissors? ")

winning_key = {
    
}

if (user1 == "Rock" or user1 == "rock") and (user2 == "paper" or user2 == "Paper"):
    print("User2 wins!")

if (user1 == "Scissors" or user1 == "scissors") and (user2 == "paper" or user2 == "Paper"):
    print("User1 wins!")

if (user1 == "Paper" or user1 == "paper") and (user2 == "paper" or user2 == "Paper"):
    print("User2 wins!")