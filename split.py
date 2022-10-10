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
    ptr = 0
    offset = 2

    for i, word in enumerate(l1):
        length = len(word)
        newPtr = ptr + length
        copyWord = "".join(list2[ptr:newPtr])
        # print(copyWord)
        if word != copyWord:
            if word != "\n" and word != "\u2019":
                leftOfWord = ""
                rightOfWord = ""

                if ptr - offset >= 0:
                    leftOfWord = "".join(list2[ptr - offset:ptr])

                if newPtr + offset < len(list2):   
                    rightOfWord = "".join(list2[newPtr:newPtr + offset])
                
                w1 = f"{leftOfWord}{copyWord}{rightOfWord}"
                w2 = f"{leftOfWord}{word}{rightOfWord}"

                print(w2, "->", w1)
                obj.append([w1 ,w2])

        ptr = newPtr

fmt = json.dumps(obj, ensure_ascii=False, indent=2)
# print(fmt)

j = open(f"{DIST}/{file}-a{JSON}", "w")
j.write(fmt)
j.close()