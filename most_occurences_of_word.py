freq={}
#for piece in open("C:\Users\Koustav\Desktop\study materials\THE Spiral Effect.docx").read().lower.split()
for piece in open("random_test.txt").read().lower().split():
    word="".join(c for c in piece)
    print(word)
    if word:
        freq[word]=1+freq.get(word,0)
print(freq)
max_word='.'
max_count=0
for (w,c) in freq.items(): #(w = values c= keys)
    if c>max_count:
        max_word=w
        max_count=c
print("The most frequent word is-->",max_word)
print("It's occurence is ",max_count)