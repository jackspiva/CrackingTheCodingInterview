# 1.1
def hasAllUniqueChars(word):
	seenChars = {}
	for c in word:
		if c in seenChars:
			return False
		else:
			seenChars[c] = 1
	return True

# 1.2
def reverseString(word):
	length = len(word)
	reversedWord = ""
	for c in word:
		reversedWord = c + reversedWord
	return reversedWord

# 1.3
def isPermutation(word1, word2):
	word1 = sorted(word1)
	word2 = sorted(word2)
	if word1 == word2:
		return True
	else:
		return False

print(isPermutation("dog", "god"))
print(isPermutation("save", "savee"))
print(isPermutation("log", "lo"))
print(isPermutation("asdfjkl", "kjasdlf"))

# 1.4
def replaceSpaces(word, length):
	return word[:length].replace(" ", "%20")

print(replaceSpaces("Mr John Smith", 13))