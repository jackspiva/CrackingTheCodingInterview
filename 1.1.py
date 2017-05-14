def hasAllUniqueChars(word):
	seenChars = {}
	for c in word:
		if c in seenChars:
			return False
		else:
			seenChars[c] = 1
	return True

