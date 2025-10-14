print("A Space Odyssey")

adjective1: str = input("Choose an adjective 'e.g., Rusty': ")
plural_noun: str = input("Choose a plural noun 'e.g., Potatoes': ")
verb_ing: str = input("Choose a verb ending in -ing: ")
place: str = input("Choose a place (not a location) 'e.g., Oven': ")
number: int = int(input("Choose a number 'like 500 or 48': "))
adjective2: str = input("Choose another adjective: ")
exclamation: str = input("Choose an exclamation 'e.g., Yikes!': ")



story: str = f'''
Captain Bob boarded his {adjective1} spaceship. He had a mission: to deliver a shipment of
{plural_noun} to the new space station. As he was {verb_ing} past the asteroid field,
the ship's navigation system suddenly directed him to a strange, dark {place}!

He saw {number} alien beings with {adjective2} skin looking in the window. {exclamation}!
He quickly rerouted and finished his delivery, but he'll never forget that detour.
'''

print(story)