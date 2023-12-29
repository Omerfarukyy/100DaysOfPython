fruits = eval(input())
# 🚨 Do not change the code above

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")

# 🚨 Do not change the code below
make_pie(4)
