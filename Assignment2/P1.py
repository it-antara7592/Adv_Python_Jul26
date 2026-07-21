# Q1. Functions, Loops, Lists, Strings
# Problem Statement
# Title: Character Frequency Counter
# Description
# Write a Python function named count_characters() that accepts a string as input and returns a
# dictionary containing the frequency of each alphabetic character present in the string.
# The function must satisfy the following conditions:
# 1. Ignore spaces.
# 2. Ignore digits and special characters.
# 3. Treat uppercase and lowercase letters as the same character.
# 4. Return the dictionary with keys in alphabetical order.
# 5. If the input string contains no alphabetic characters, return an empty dictionary.


def count_characters(text):
    list2=[]
    list1=list(filter(str.isalpha,text))
    list1.sort()
    
    for x in list1:
        
        if x in list2:
            continue
        
        current_char=x
        counter=0
        for y in list1:
            if current_char==y:
                counter=counter+1
            else:
                continue
        list2.append(counter)
        
    dict1=dict(zip(list1,list2))
    return dict1
    

str1=input("Enter the text: ").lower()
print(count_characters(str1))