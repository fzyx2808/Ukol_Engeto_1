                       
#Psal jsem dané věci v angličtině, protože zadání bylo v angličtině, ale rád bych to přeložil do češtiny, pokud byste chtěli.

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"}

username = input("Username:")
password = input("Password:")

if username in users and users[username] == password:
    print(20 * "-")
    print("Welcome to the app,", username)
    print("We have", len(TEXTS), "texts to be analyzed, are you ready :-) ??")
    print(20* "-") 
else:
    print("Wrong username or password, terminating the program..., sorry")
    exit()

Text_number = input("Enter a number btw. 1 and" + str(len(TEXTS)) +  "to select:")
if not Text_number.isdigit() or int(Text_number) < 1 or int(Text_number) > len(TEXTS):
    print("Invalid input, I have to terminate the program, sorry")
    exit()

selected_text = TEXTS[int(Text_number) - 1]
words = selected_text.split()

cleaned_words =[]
for word in words:
    cleaned_word = word.strip(".,;:!?")
    cleaned_words.append(cleaned_word)

word_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
number_count = 0
number_sum = 0
lengths = {}

for word in cleaned_words:
    word_count = word_count +1

    if word.istitle():
        titlecase_count = titlecase_count + 1
    
    if word.isupper():
        uppercase_count = uppercase_count + 1

    if word.islower():
        lowercase_count = lowercase_count + 1

    if word.isdigit():
        number_count = number_count + 1
        number_sum = number_sum + int(word)
    
    length = len(word)
    if length in lengths:
        lengths[length] = lengths[length] + 1
    else:
        lengths[length] = 1

print("--------------------------------")
print("There are", word_count, "words in the selected text.")
print("There are", titlecase_count, "titlecase words.")
print("There are", uppercase_count, "uppercase words.")
print("There are", lowercase_count, "lowercase words.")
print("There are", number_count, "numeric strings.")
print("The sum of all the numbers", number_sum)
print("--------------------------------")
print("LEN| OCCURRENCES |NR.")
print("--------------------------------")

for length in sorted(lengths):
    stars = "*" * lengths[length]
    print(str(length).rjust(3) + "|" + stars.ljust(13) + "|" +
          str(lengths[length]))

print("Thank you for using the app, goodbye!")




