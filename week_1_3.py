#Write a program that prints the longest 
#substring of s in which the letters occur 
#in alphabetical order. For example, if 
#s = 'azcbobobegghakl', then your program should 


#In the case of ties, print the first substring. For example, 
#if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

#s = 'zyxwvutsrqponmlkjihgfedcba'

count = 0
wordlen = len(s)
i = 0
save = ''
substring = s[i]

while i < (wordlen - 1) :
#    print("\n\nThe loop is counting at " + str(i))
    if s[i] <= s[i+1]:
#        print(s[i] + " <= " +s[i+1])
        substring += s[i+1]
#        print("STARTING POINT    substring is " + substring)
        i += 1
        count += 1
#        print("currently counting at " + str(count))
        if len(substring) > len(save):
#            print("save is " + save)
            save = substring
#            print("save is now updated to " + save)
#            print("substring is " + substring)
    else:
#        print("didn't find the sequence so I'm passing")
        count = 0
        i += 1
        substring = s[i]
#        print("substring is " + substring)

if save == '':
    save = s[0]

print("Longest substring in alphabetical order is: " + save)
