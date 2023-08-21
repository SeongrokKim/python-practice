import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

while True:
    pw = input().rsplit()[0]
    if pw == 'end':
        break
    hasVowels = False
    for a in pw:
        if a in vowels:
            hasVowels = True
            break
    if hasVowels:
        hasThree = False
        for i in range(len(pw)-2):
            if (pw[i] in vowels and pw[i+1] in vowels and pw[i+2] in vowels) or (pw[i] not in vowels and pw[i+1] not in vowels and pw[i+2] not in vowels):
                hasThree = True
                break
        if hasThree == False:
            sameTwo = False
            for i in range(len(pw)-1):
                if pw[i] == pw[i+1]:
                    if pw[i] == 'e' or pw[i] == 'o':
                        continue
                    else:
                        sameTwo = True
                        break
            if sameTwo == False:
                print('<{0}> is acceptable.'.format(pw))
                continue
    
    print('<'+pw+'> is not acceptable.')
