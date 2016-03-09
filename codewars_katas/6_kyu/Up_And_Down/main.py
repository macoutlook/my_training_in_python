def arrange(strng):
    strings = strng.split(" ")
    for ind in xrange(len(strings)):
        if ind % 2:
            try:
                if len(strings[ind-1]) > len(strings[ind]):
                    strings[ind-1], strings[ind] = strings[ind], strings[ind-1]
                strings[ind-1] = strings[ind-1].lower()
                if len(strings[ind+1]) > len(strings[ind]):
                    strings[ind+1], strings[ind] = strings[ind], strings[ind+1]
                strings[ind+1] = strings[ind+1].lower()
            except IndexError:
                pass
            finally:
                strings[ind] = strings[ind].upper()

    return " ".join(strings)

def main():
    print arrange("on I came up were so grandmothers")
    print arrange("turn know great-aunts aunt look A to back")

# turn know great-aunts aunt look A to back
#
# turn great-aunts know aunt look A to back
#
# turn great-aunts know aunt A look to back

if __name__ == '__main__':
    main()
