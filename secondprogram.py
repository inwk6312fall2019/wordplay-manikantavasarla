fin = open('words.txt')

def has_no_e(letter):
    for char in letter:
        if char in 'Ee':
            return False
    return True  

count = 0
for line in fin:
    letter = line.strip()
    if has_no_e(letter):
        count += 1
        print (letter)

percent = (count / 113809.0) * 100

print(str(percent) + "% of the words don't have an 'e'.")
