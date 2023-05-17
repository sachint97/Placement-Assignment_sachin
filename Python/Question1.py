"""Question 1: -
Write a program that takes a string as input, and counts the frequency
of each word in the string, there might be repeated characters in the string.
Your task is to find the highest frequency and returns the length of the
highest-frequency word."""


def find_max_frequency_length(input_str):
    str_count = dict()
    max_count = 0
    max_count_str = ""

    for word in input_str.split(" "):
        word = word.lower()
        if not str_count.get(word, False):
            str_count[word] = 1
        else:
            str_count[word] = str_count[word] + 1

        if str_count[word] > max_count:
            max_count = str_count[word]
            max_count_str = word

    print(f"The length of highest frequency word is {len(max_count_str)}")


# Test case 1
input_str1 = "Where can i find my bag, where"
find_max_frequency_length(input_str1)

# Test case 2
input_str1 = "Find find find my bag."
find_max_frequency_length(input_str1)

find_max_frequency_length(input("Enter your string.\n"))
