"""
CP1404/CP5632 Practical
Program to count occurrences of word in string

Word Occurrences
Estimate: 30 minutes
Actual: 18 minutes
"""
text = str(input("Text: "))
words = text.split()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

longest_word_length = max(len(word) for word in word_to_count)
for word in sorted(word_to_count):
    print(f"{word:{longest_word_length}}: {word_to_count[word]}")
