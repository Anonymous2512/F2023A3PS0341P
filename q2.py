def max_vowels(strings):
    max = 0
    max_vowels_string = ""

    for string in strings:
        vowels_count = sum(1 for char in string if char.lower() in "aeiou")
        if vowels_count > max:
            max = vowels_count
            max_vowels_string = string

    return max_vowels_string

def main():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        string = input(f"Enter string {i+1}: ")
        strings.append(string)

    string = max_vowels(strings)
    print("String with the most vowels:", string)

if __name__ == "__main__":
    main()
