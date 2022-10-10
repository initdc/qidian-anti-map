SRC = "source"
DEST = "dest"

`mkdir -p #{DEST}`

def perline src, *opt
    dest = opt[0]
    add = opt[1] || "\n"

    buffer = ""
    File.foreach(src) {|line|
        last = line
        if line != "\n"
            buffer += line + add
        else
            buffer += line
        end
    }

    if dest.empty?
        return buffer
    else
        IO.write(dest, buffer)
    end
end

orig = "qidian.txt"
copy = "copy.txt"

# perline "#{SRC}/#{orig}", "#{DEST}/#{orig}"
# perline "#{SRC}/#{copy}", "#{DEST}/#{copy}"