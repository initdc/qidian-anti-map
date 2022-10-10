# encoding=utf-8
import json
import jieba

PATCH = ".patch"
JSON = ".json"

DIFF = "diff"
DIST = "dist"

file = "111"

f = open(f"{DIFF}/{file}{PATCH}", "r", encoding="utf-8")

lastI = 0
last = ""
pairs = []

for i, line in enumerate(f):
    if line.startswith("---"):
        continue

    if line.startswith("+++"):
        continue

    if line.startswith("-"):
        lastI = i
        last = line
    elif line.startswith("+"):
        if i == lastI + 1:
            pairs.append([last, line])
            last = ""

# print(pairs)

obj = []

for i, pair in enumerate(pairs):
    s1 = pair[0].removeprefix("-")
    s2 = pair[1].removeprefix("+")

    l1 = jieba.cut(s1)
    # print("|".join(l1))

    # l2 = jieba.cut(s2)
    # print("|".join(l2))

    list2 = list(s2)

    for i, word in enumerate(l1):
        length = len(word)
        
        copyWord = "".join(list2[:length])
        # print(copyWord)
        if word != copyWord:
            if word != "\n" and word != "\u2019":
                print(word, "->", copyWord)
                obj.append([copyWord ,word])

        del list2[:length]

fmt = json.dumps(obj, ensure_ascii=False, indent=2)
# print(fmt)

j = open(f"{DIST}/{file}{JSON}", "w")
j.write(fmt)
j.close()