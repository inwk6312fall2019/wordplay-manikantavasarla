def using_only(word, letters):
    """returns true if word is made only out of letters  else flase"""
    for letter in word:
        if letter not in letters:
            return False
    return True
