def name_list():
    result = list()
    count = 1
    while True:
        name = input(f"Enter name {count}: ")
        if name:
            result.append(name)
            count += 1
        else:
            break
    return result

print(name_list())


def remove_the_thirds(list1: list):
    index = 2 # start from the first third element
    while index < len(list1):
        list1.pop(index)
        index += 2

def main():
    list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
    remove_the_thirds(list1)
    print(list1)

main()

def get_the_difference(list1, list2):
    difference_list = []

    for i in list1:
        if i not in list2 and i not in difference_list:
            difference_list.append(i)
    for i in list2:
        if i not in list1 and i not in difference_list:
            difference_list.append(i)
    return difference_list

def main():
    list1 = [3, 1, 1, 1, 2, 7, 9, 9]
    list2 = [4, 1, 1, 2, 2, 5]
    print(get_the_difference(list1, list2))

main()


import turtle

def draw_bar(height, text):
    width = 20
    turtle.fillcolor("purple")
    
    for i in range(2):
        turtle.begin_fill()

        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

        turtle.end_fill()

    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x + 5, y - 15)
    turtle.write(text)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)


def nums_frequency_histogram():
    arr = [1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4]
    arr.sort()
    unique_nums = list()
    unique_nums_count = list()
    space = 35

    for i in arr:
        if i not in unique_nums:
            unique_nums.append(i)
    for i in unique_nums:
        unique_nums_count.append(arr.count(i))

    turtle.left(90)
    turtle.forward(max(unique_nums_count) * 20)
    turtle.backward(max(unique_nums_count) * 20)
    turtle.right(90)
    turtle.forward(space)
    
    for i in range(len(unique_nums)):
        draw_bar(unique_nums_count[i] * 20, unique_nums[i])
    turtle.forward(space)

    turtle.done()

nums_frequency_histogram()



def merge(list1, list2):
    merged_list = list1 + list2
    # bubble sort algorithm
    for i in range(len(merged_list) - 1):
        for j in range(len(merged_list) - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j] # swap
    return merged_list

def main():

    list1 = [1, 5, 16, 61, 111]
    list2 = [2, 4, 5, 6]

    print("The merged list is ", end="")
    for i in merge(list1, list2):
        print(i, end=" ")
    print()

main()
