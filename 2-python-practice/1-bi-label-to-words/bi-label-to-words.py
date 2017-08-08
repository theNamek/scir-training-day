#!/usr/bin/env python
import sys

def read_instance(fp):
    sentence = []
    while True:
        line = fp.readline()
        if not line:
            yield sentence
            break

        line = line.strip()

        if len(line) == 0:
            yield sentence
            sentence = []
        else:
            sentence.append( line.split() )


def bi2words(chars):
    # insert your code here
    for i in range(0, len(chars) - 3):
        if i % 2 == 0:
            if chars[i + 3] == 'B':
                print chars[i]
                print ' '
            else:
                i += 2
        else:
            i += 1

if __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    try:
        fpo = open(sys.argv[2], "w")
    except IOError:
        print >> sys.stderr, "failed to open file."
        sys.exit(1)

    for sentence in read_instance(fpi):
        print sentence
