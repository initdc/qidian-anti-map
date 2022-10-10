require "./comm"

FILTER = ["\n", "        \n"]
DELETE = "　　"

def perline src, *opt
    dest = opt[0]
    add = opt[1] || "\n"

    buffer = ""
    File.foreach(src) {|line|
        last = line
        # p line
        if !(FILTER.include? line)
            line = line.delete(DELETE)
            buffer += line + add
        end 
    }

    if dest.empty?
        return buffer
    else
        IO.write(dest, buffer)
    end
end

`mkdir -p #{DEST}`


file = "111"

perline "#{SRC}/#{file}#{TXT}", "#{DEST}/#{file}-src#{TXT}"
perline "#{COPY}/#{file}#{TXT}", "#{DEST}/#{file}-copy#{TXT}"