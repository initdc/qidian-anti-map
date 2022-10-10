require "./perline"

orig = "qidian.txt"
copy = "copy.txt"

`git diff --ignore-all-space --diff-algorithm=myers --no-index #{DEST}/#{orig} #{DEST}/#{copy} > orig-copy.patch`