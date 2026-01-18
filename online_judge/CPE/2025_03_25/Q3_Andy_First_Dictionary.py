import re
import sys

text = sys.stdin.read()
text_lower = text.lower()

words = re.findall('[a-z]+', text_lower)
sorted_words = sorted(set(words))
for sorted_word in sorted_words:
    print(sorted_word)