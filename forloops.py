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