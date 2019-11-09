#1.Charting practice
# holy_grail sample
holy_grail = "SOLDIER #1: Halt!  Who goes there?\nARTHUR: It is I, Arthur, son of Uther Pendragon, " \
             "from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign " \
             "of all England!\nSOLDIER #1: Pull the other one!"

# Split the script into lines: lines
import re
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
from nltk.tokenize import regexp_tokenize
tokenized_lines = [regexp_tokenize(s,r"\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
import matplotlib.pyplot as plt
plt.hist(line_num_words)

# Show the plot
plt.show()