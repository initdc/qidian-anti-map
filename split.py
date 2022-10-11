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
    lastPtr = 0
    lastWord = ""
    lastCopyWord = ""

    for j, word in enumerate(l1):
        length = len(word)
        newPtr = ptr + length

        FILTER = ["\n", "\u2019"]
        inf = True if word in FILTER else False
        if inf == False:
            copyWord = "".join(list2[ptr:newPtr])
            # print(copyWord)

            if lastWord == lastCopyWord:
                if word == copyWord:
                    lastPtr = newPtr
                    lastWord = ""
                    lastCopyWord = ""
                else:
                    lastPtr = ptr
                    lastWord = word
                    lastCopyWord = copyWord
            else:
                if word == copyWord:
                    w1 = lastWord
                    w2 = "".join(list2[lastPtr:ptr])

                    print(w1, "->", w2)
                    obj.append([w2 ,w1])
                    lastPtr = newPtr
                    lastWord = ""
                    lastCopyWord = ""
                else:
                    lastWord += word
                    lastCopyWord += copyWord

        ptr = newPtr
           

fmt = json.dumps(obj, ensure_ascii=False, indent=2)
# print(fmt)

jn = open(f"{DIST}/{file}{JSON}", "w")
jn.write(fmt)
jn.close()