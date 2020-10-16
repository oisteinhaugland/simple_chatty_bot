word1 = input()
word2 = input()

# How many letters does the longest word contain?
words = [word1, word2]

max_length = 0
for word in words:
    max_length = len(word) if len(word) >= max_length else max_length

print(max_length)

print(max(len(word1), len(word2)))
