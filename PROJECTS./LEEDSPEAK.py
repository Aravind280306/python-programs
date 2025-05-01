import random
def english_to_leetspeak(message):
    char_mapping = { 'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],'v': ['\\/']  }
    return ''.join(random.choice(char_mapping.get(char.lower(), [char])) if random.random() <= 0.7 else char for char in message)
message = input("Enter your message: ")
leetspeak = english_to_leetspeak(message)
print(leetspeak)
