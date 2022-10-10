require "./comm"

`mkdir -p #{DIFF}`


file = "111"

`git diff --ignore-all-space --diff-algorithm=myers --no-index #{DEST}/#{file}-src.txt #{DEST}/#{file}-copy.txt > #{DIFF}/#{file}.patch`