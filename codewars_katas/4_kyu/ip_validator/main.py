# with re
# import re
# def is_valid_IP(strng):
#     return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))

def is_valid_IP(strng):
    res = True
    if len(strng.split('.')) == 4:
        for oct in strng.split('.'):
            try:
                if not 256 > int(oct) >= 0 or ' ' in oct or (oct[0] == '0' and len(oct) > 1):
                    res = False
            except:
                res = False
    else:
        res = False
    return res


def main():
    print is_valid_IP('12.34.56 .1')



if __name__ == '__main__':
    main()