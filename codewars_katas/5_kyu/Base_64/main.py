def base64_to_base10(str):
  res = ''
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  # joining list into string
  set_zeros = lambda x: "".join((6 - len(x))*['0']) + x
  for char in str:
      if char in characters:
          # cutting '0b' prefiks from binary string and concatenate with res
          res += set_zeros(bin(characters.index(char))[2:])
  return int(res, 2)


def main():
    print base64_to_base10("WIN")


if __name__ == '__main__':
    main()