def second_largest(list):
    if len(list) < 2:
        return "List must contain at least two elements"
    
    max1 = max(list[0], list[1])
    max2 = min(list[0], list[1])
    
    for num in list[2:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    
    return max2

def main():
    n = int(input("Enter the number of elements in the list: "))
    my_list = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)
    
    print("Second largest element:", second_largest(my_list))

if __name__ == "__main__":
    main()
