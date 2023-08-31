user_name = input('What is your name? ')
user_age = int(input('What is your age? '))
user_gender = input('What is your gender? ')

if user_gender == 'male' or user_gender == 'Male':
    is_male = True
else:
    is_male = False

character = {
    "name": user_name,
    "age": user_age,
    "is_male": is_male,
    "fav_food_list": ['cookies', 'hot dogs', 'pretzels', 'ice cream', 'steaks']
}

print(character)