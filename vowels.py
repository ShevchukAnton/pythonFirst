vowels = {}

word = input("Enter some nasty words and hit 'Enter':\n")
for ch in word:
    if ch in ["a", "i", "o", "u", "e"]:
        vowels.setdefault(ch, 0)
        vowels[ch] += 1

for k, v in sorted(vowels.items()):
    if v > 0:
        print(k, ":", v)

print()
