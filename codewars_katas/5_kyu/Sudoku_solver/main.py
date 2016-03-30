def done_or_not(board):
  digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
  first = True
  for i, row in enumerate(board):
      if not set(row) == digits:
          return 'Try again!'
      for j, el in enumerate(row):
          if first:
            col = [item[j] for item in board]
            if not set(col) == digits:
                return 'Try again!'
          if i % 3 == 0 and j % 3 ==0:
            a = [el[j:j+3] for el in board[i:i+3]]
            if not set(a[0] + a[1] + a[2]) == digits:
                return 'Try again!'
      first = False
  return 'Finished!'


def main():
    print done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

if __name__ == '__main__':
    main()