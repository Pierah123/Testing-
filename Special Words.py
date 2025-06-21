sentence = "The quick brown fox jumps over the lazy dog".lower()
words = set(sentence.split())
a_count = sum(w.count('a') for w in words)

print(len(words))
print(a_count)
