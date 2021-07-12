# builtInFunction

# 1st method
# word = "Python Programming"
# x = len(word)
# print(x)

# 2nd method
# print(len(word))


# Write Paragraph

# 1st Method
# paragraph = "bjkhkjg kjbkjghjfhj mjbhjcghc mbnvbnc mnbvgh" \
#            "nbvmbkjnbkjvb n hvhjhj hjhjckjgy " \
#           "vvmnbk hvjhgh mhv" \
#           ""
# print(paragraph)

# 2nd Method
# paragraph = """bjkhkjg kjbkjghjfhj mjbhjcghc mbnvbnc mnbvgh
#               nbvmbkjnbkjvb n hvhjhj hjhjckjgy
#              vvmnbk hvjhgh mhv"""

# print(paragraph)


# word1 = "Python"
# word2 = "Programming"

# print(word1 + word2) # No Space
# print(word1 + " " + word2) # With Space
# print(word1, word2) # With Space

# (list counting start in 0)
# word = "Python Programming"
# a = word[0]
# b = word[-1] # counting start right to left (Stating Number -1)
# c = word[6] # space is a character
# print(c)

# print(word[0:6])
# print(word[-18:-12])
# print(word[:6])
# print(word[7:])
# print(word[:])

# a = "cat"
# print("r" + a[1:3])
# print(a[0:2] + "r")
# print(a[0] + "u" + a[2])

# word = "Python Programming"
# print(word.lower())
# print(word.upper())

# space remove
# word3 = "Python   "
# print(len(word3))
# y = word3.rstrip()
# print(len(y))

# word4 = "ppxPython   "
# print(len(word4))
# w = word4.lstrip("px")
# print(w)
# print(len(w))

# word5 = "yyyyPythonyyy"
# print(len(word5))
# p = word5.strip("y")
# print(p)
# print(len(p))

word6 = "Python"
word7 = "Programing"
word8 = "Java"

print(word6.startswith("p"))
print(word7.startswith("P"))
print(word8.startswith("Ja"))
print(word8.startswith("Java"))

print(word6.endswith("n"))
print(word7.endswith("n"))


