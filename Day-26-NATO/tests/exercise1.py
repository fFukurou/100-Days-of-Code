
sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
words_list = sentence.split()
result = {word:len(word) for word in words_list}

print(result)
