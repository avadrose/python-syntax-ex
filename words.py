
"""Print all words in uppercase"""

words = ["hello", "hey", "goodbye", "yo", "yes"]

for word in words:
    print(word.upper())

"""Turn it into a function"""

def print_upper_words(words):
    """Print each word in uppercase on a seperate line"""

    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye"])

"""Only print words starting with letter e"""

def print_upper_words(words):
    """Print unppercase words that start with letter e"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words(["hello", "elephant", "Egg", "yes"])

"""Allow set of letters"""

def print_upper_words(words, must_start_with):
    """Print uppercase words that strart with any of given letters"""

    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

print_upper_words(
    ["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"}
)