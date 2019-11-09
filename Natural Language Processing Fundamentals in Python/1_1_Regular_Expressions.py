# Regular expressions

""" Notes
match first word it finds
re.match(r"\w+", my_string)
\d [digits]
\s [spaces]
.* [wildcard, any letter or symbol]
+ or * [greedy match, grab repeats]
\S [not a space]
[a-z] [lowercase group]
"""

# find all words
import re
my_string_test = "Let's write RegEx!"
results_1 = re.findall(r"\w+", my_string_test)
print(results_1)

# Write a pattern to match sentence endings: sentence_endings
my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))