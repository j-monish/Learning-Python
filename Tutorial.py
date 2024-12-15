# # # # # # #Quote is used for strings. They are to be copied as they are.
# # # # # # password =input("light:")
# # # # # # if(light=="red"):
# # # # # #     print("stop")
# # # # # # elif(light=="yellow"):
# # # # # #     print("wait")
# # # # # # elif(light=="green"):
# # # # # #     print("go")
# # # # # # else:
# # # # # #     print("light gone bad")

# # # # # # dict1 = {"name": "monish", "phone": 9312}
# # # # # # students = {"monish", "mohit"}
# # # # # # # for key in students.
# # # # # # #     print(key)
# # # # # # print(students)
# # # # # pi=22/7
# # # # # print(pi)
# # # # # print(type(pi))
# # # # p=5
# # # # r=6
# # # # t=3
# # # # a=p*r*t/100
# # # # print(a)
# # # # a=2e3
# # # # print(a)
# # # # print(type(a))
# # # a = str(2.5555551e3)
# # # print(a)       # 2000
# # # print(type(a)) # <class 'int'>
# # # a=2//3
# # # print(a)
# # # b=int(2/3)
# # # print(b)
# # a=2
# # b=5
# # m=f"a={a} \nb={b}"
# # print(m)
# # first="Mohan"
# # last="Sharma"
# # Name=f"{first} {last}"
# # print(Name)
# # print(Name[:])#end index is not included
# # print(len(Name))
# # my_food='samosa,jalebi'
# # print(my_food)
# # print("jalebi" not in my_food)
# # print('salad' not in my_food)
# # print(my_food.replace("samosa","salad"))
# # print(dir(my_food))
# # my_fav_sweet = "I love jalebi, kaju katli and laddu."
# # print("jalebi" not in my_fav_sweet)
# x=5
# y=8
# # print(f'I eat {x} fr and {y} veg in a')
# line='The Himalayas are one of the youngest mountain ranges on the planet'
# print(line[4:13])
# print(line[-30:-15])
# string= "There are 9 planets in the solar system"; print(string.replace('9','8'))
# abc=f'{line[:13]} {line[-13:]}'
# print(abc)
# items=['rice','pasta','butter','bread','cheese']
# items.reverse()
# print(items)
# items.insert(1,'peas')
# items.remove('rice')
# print(items)
# print('rice' in items)
# print(items.sort())
# print(items)
# expenses=[8,9,3,6,2,8,5,0,3,8,3,1,4]
# expenses.sort(reverse=True)
# print(expenses)
# new_list=items+expenses
# print(new_list)
# print(len(new_list))
# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# print(len(avengers))
# avengers.append('spiderman')
# print(avengers)
# avengers.remove('Captain America')
# avengers.insert(0,'Captain America')
# print(avengers)
# n=input('Enter a number:')
# n=int(n)
# if n%2==0:
#     print('no is even')
# if n%3==0:
#     print("no is divisible by 3")
# else:
#     print('no is odd')
# indian=['rice','roti','paneer','dhokla']
# italian=['roll','pizza','pasta','risotto']
# chinese=['noodles','fried rice','manchurian','pot sticker']
# dish=input("dish is:")
# if dish in indian:
#     print(f"{dish} is indian")
# elif dish in italian:
#     print(f"{dish} is italian")
# elif dish in chinese:
#     print(f"{dish} is chinese")
# else:
#     print("cuisine is unknown")
# n=int(input("number is:"))
# message = "number is even" if n%2==0 else "number is odd"
# print(message)

# height=float(input("height is:")); print(height)
# weight=int(input("weight is:")); print(weight)
# BMI=weight/(height**2)
# if BMI>=30:
#     print("obese")
# elif 25<BMI<29:
#     print("overweight")
# elif 18.5<BMI<25:
#     print("normal")
# elif BMI<18.5:
#     print("underweight")
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "san francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
city_1=input("city 1 is:")
if city.lower() in India:
    print(f'{city} is in india')
elif city.lower() in USA:
    print(f'{city} is in USA')    
elif city in UK:
    print(f'{city} is in UK')    
else:
    print("Unknown")
city_2=input("city 2 is:")
if city_1 in India and city_2 in India:
    print(f'{city_1} and {city_2} are in india')
elif city_1 in USA and city_2 in USA:
    print(f'{city_1} and {city_2} are in USA')
elif city_1 in UK and city_2 in UK:
    print(f'{city_1} and {city_2} are in UK')
else:
    print("Both cities are not in same country")

