count = 0
wordlen = len(s)


for i in range(wordlen):
    if i + 3 <= wordlen and s[i: i + 3] == "bob":
        count += 1
print ("Number of times bob occues is : " +str(count))
