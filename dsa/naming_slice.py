from collections import Counter

# items = [0, 1, 2, 3, 4, 5, 6]
# a = slice(2, 4)
# print(items[2:4])
# print(items[a])

# Most Frequently Occurring
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
# print(word_counts)
# top_3 = word_counts.most_common(3)
# print(top_3)
# print(word_counts['not'])

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# word_counts = Counter()
# for word in more_words:
#     word_counts[word] += 1
# print(word_counts['eyes'])

word_counts.update(more_words)
a = Counter(words)
b = Counter(more_words)
# print(a)
# print(b)
c = a+b
print(c)
d = a-b
print(d)


