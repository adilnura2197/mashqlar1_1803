#1
students = {
    "Ali": 85,
    "Vali": 90,
    "Hasan": 78,
    "Husan": 92
}
print(students)
max_ball = max(students.values())

for v, k in enumerate(students):
    if max_ball == students[k]:
        print(k)
        break


#2
sales = {
    "apples": 50,
    "oranges": 75,
    "bananas": 30,
    "pears": 45
}

print(sales)

summa = sum(sales.values())
print(summa)


#3
grades = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85,
    "Biology": 90
}

for fan, ball in grades.items():
    if ball > 75:
        print(fan)


#4
inventory = {
    "pen": 10,
    "pencil": 20,
    "notebook": 15,
    "eraser": 5
}

print(inventory)

min_ball = min(inventory.values())

for v, k in enumerate(inventory):
    if min_ball == inventory[k]:
        print(k)
        break


#5
products = {
    "A": 100,
    "B": 200,
    "C": 150,
    "D": 250
}

print(products)

summa = sum(products.values())
print(summa)

x = summa // len(products)
print(x)
