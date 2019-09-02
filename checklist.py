checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[int(index)]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

        # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option ")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)
    print(read(0))
    select("C")
    user_value = user_input("Enter another item: ")
    print(user_value)
    list_all_items()

    # print(read(1))


test()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    running_two = select(selection)
