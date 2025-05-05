vowels = ('a','e','i','o','u')

message = input("Enter a message : ")

new_message = ""

for letter in message:
    if letter not in vowels:
        new_message += letter
    
    if letter in vowels:
        print(letter, "I am a vowel.")

print(new_message)