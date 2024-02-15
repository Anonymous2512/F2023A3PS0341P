def dictionary(keys, values):
    dict = {}
    if len(keys) != len(values):
        print("The lists should have equal length")
        return None

    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        dict[key] = value

    return dict

def main():
    n = int(input("Enter the number of elements in the lists: "))
    
    keys = []
    values = []
    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value {i+1}: ")
        keys.append(key)
        values.append(value)

    result = dictionary(keys, values)
    print("Resulting Dictionary:", result)

if __name__ == "__main__":
    main()
