with open("sgb-words.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

filtered = [
    w
    for w in lines
    if (w.startswith("e") or w.endswith("e"))
    and (not "e" in w[1:4])
    and (not "i" in w[2:4])
    and (not "n" in w[3:])
]

eliminated = "aduopsbg"
filtered = [w for w in filtered if not any(c in w for c in eliminated)]

contained = "ien"
filtered = [w for w in filtered if all(c in w for c in contained)]
# p = r'([])'
print(len(filtered))
print(filtered)
