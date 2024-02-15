def new_list(list):
    new_list = []

    for item in list:
        if item not in new_list:
            new_list.append(item)

    return new_list

def main():
    n = int(input("Enter the number of elements in the list: "))
    list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        list.append(element)

    print("Original List:", list)
    print("List with Duplicates Removed:", new_list(list))

if __name__ == "__main__":
    main()
