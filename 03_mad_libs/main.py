# User input
print('Bob\'s adventure!')
adjective1: str = input('Enter an adjective: ')
animal: str = input('Enter an animal: ')
adjective2: str = input('Enter another adjective: ')
noun2: str = input('Enter another noun: ')
verb: str = input('Enter a verb: ')
noun3: str = input('Enter one more noun: ')

# Story
story: str = f'''
Bob went to the zoo today. He saw a(n) {adjective1} {animal} jumping up and down in its tree.
He turned his back for two seconds, and when he turned around again, the {adjective1} {animal} had
transformed into a(n) {adjective2} {noun2}! He couldn't believe his eyes, so he started to
{verb} with his {noun3}. In the end, he woke up and realised it was all a dream.
'''

# Output
print('Result:')
print(story)


# Homework:
# 1. Create your own story and practice taking user input!