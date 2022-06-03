from alphabet import alphabet,Harf,beggining_after,TATWEEL,tashkeel

# Reverse returns its argument string reversed rune-wise left to right.
def Reverse(r):
	s = list(r)
	i,j = 0,len(s)-1
	while i<(len(s)/2):
    
		s[i],s[j] = s[j],s[i]
		i,j = i+1,j-1

	s = ''.join(s)
	return str(s)


# SmartLength returns the length of the given string
# without considering the Arabic Vowels (Tashkeel).
def SmartLength(s):
	# len() use int as return value, so we'd better follow for compatibility
	length = 0
	r = list(s)

	for value in r :
		if tashkeel[value]: 
			continue
		
		length+=1
	

	return length


# RemoveTashkeel returns its argument as rune-wise string without Arabic vowels (Tashkeel).
def RemoveTashkeel(s) :
	# var r []rune
	# the capcity of the slice wont be greater than the length of the string itself
	# hence, cap = len(s)
	r = list (s)

	for  value in s:
		if tashkeel[value] :
			continue
		
		r.append(value)
	

	return str(r)


# RemoveTatweel returns its argument as rune-wise string without Arabic Tatweel character.
def RemoveTatweel(s) :
	r = list(s)
	for  value in s :
		if TATWEEL.equals(value):
			continue
		
		r.append(value)
	

	return str(r)


def getCharGlyph(previousChar, currentChar, nextChar ):
	glyph      = currentChar
	previousIn = False     # in the Arabic Alphabet or not
	nextIn     = False     # in the Arabic Alphabet or not

	for s in alphabet :
		if s.equals(previousChar) : # previousChar in the Arabic Alphabet ?
			previousIn = True
		

		if s.equals(nextChar) : # nextChar in the Arabic Alphabet ?
			nextIn = True
		
	

	for s in alphabet :

		if not s.equals(currentChar):  # currentChar in the Arabic Alphabet ?
			continue
		

		if previousIn and nextIn : # between two Arabic Alphabet, return the medium glyph
			for s in beggining_after :
				if s.equals(previousChar) :
					return getHarf(currentChar).beggining
				
			

			return getHarf(currentChar).medium
		

		if nextIn : # beginning (because the previous is not in the Arabic Alphabet)
			return getHarf(currentChar).beggining
		

		if previousIn : # final (because the next is not in the Arabic Alphabet)
			for s in  beggining_after :
				if s.equals(previousChar) :
					return getHarf(currentChar).isolated
				
			
			return getHarf(currentChar).final
		

		if not previousIn and not nextIn :
			return getHarf(currentChar).isolated
		
	return glyph


# equals() return True if the given Arabic char is alphabetically equal to
# the current Harf regardless its shape (Glyph)

def validateHarf(char) :
	if   Harf == char.unicodee :
		return True

	elif Harf == char.beggining:
		return True

	elif Harf == char.isolated:
		return True

	elif Harf == char.medium:
		return True

	elif Harf == char.final:
		return True

	else:
		return False



# getHarf gets the correspondent Harf for the given Arabic char
def getHarf(char) :
	for s in alphabet :
		if s.equals(char) :
			return s

	return Harf(unicodee= char, isolated= char, medium= char, final= char)


#RemoveAllNonAlphabetChars deletes all characters which are not included in Arabic Alphabet
def RemoveAllNonArabicChars(text ) :
	runes   = str(text)
	newText = list(runes)

	for current in  runes :
		inAlphabet = False

		for s in alphabet:
			if s.equals(current) :
				inAlphabet = True

		if inAlphabet :
			newText.append(current)
	
	return str(newText)


# ToGlyph returns the glyph representation of the given text
def ToGlyph(text ) :

	runes   = text
	length  = len(runes)
	newText = list(runes)

	for i, current in runes:
		# get the previous char
		if (i - 1) < 0 :
			prev = 0
		else:
			prev = runes[i-1]

		# get the next char
		if (i + 1) <= length-1 :
			next = runes[i+1]
		else:
			next = 0

		# get the current char representation or return the same if unnecessary
		glyph = getCharGlyph(prev, current, next)

		# append the new char representation to the newText
		newText.append(glyph)

	return str(newText)

lis = "نَصٌ عَربِيٌّ"

if SmartLength("نَصٌ عَربِيٌّ") == 7:
        print('Test is OK!')
        