def canConstruct(ransomNote, magazine):
    magDict = {}
    for letter in magazine:
        if letter in magDict:
            continue
        else: magDict[letter] = magazine.count(letter)
    for letter in ransomNote:
        if letter not in magDict:
            return False
        elif ransomNote.count(letter) <= magDict[letter]:
            continue
        else:
            return False
    return True

rn1 = 'aab'
m1 = 'a'

print(canConstruct(rn1,m1))