word1 = input("Adj meg egy szót! ")
word2 = input("Adj meg egy másik szót! ")

if len(word1) > len(word2):
    print(f"A hosszabb szó: {word1}")
elif len(word1) < len(word2):
    print(f"A hosszabb szó: {word2}")
else:
    print("A két szó egyforma hosszú.")