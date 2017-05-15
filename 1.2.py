def reverseString(word):
	length = len(word)
	reversedWord = ""
	for c in word:
		reversedWord = c + reversedWord
	return reversedWord

