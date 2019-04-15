def hexdump(raw):
    buf = ""
    line = ""

    start = 0
    done = False
    while not done:
        end = start + 16
        max = len(raw)
        if end > max:
            end = max
            done = True

        chunk = raw[start:end]
        for i in xrange(len(chunk)):
            if i > 0:
                spacing = " "
            else:
                spacing = ""
            buf += "%s%02x" % (spacing, ord(chunk[i]))

        if done:
            for i in xrange(16 - (end % 16)):
                buf += "   "

        buf += "  "

        for c in chunk:
            val = ord(c)
            if val >= 33 and val <= 126:
                buf += c
            else:
                buf += "."

        buf += "\n"

        start += 16

    return buf

