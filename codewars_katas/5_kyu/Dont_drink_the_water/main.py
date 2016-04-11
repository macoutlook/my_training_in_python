
# Nice solution
# DENSITY = {'H': 1.36, 'W': 1, 'A': 0.87, 'O': 0.8}
#
#
# def separate_liquids(glass):
#     if not glass:
#         return []
#     column = len(glass[0])
#     liquids = sorted((b for a in glass for b in a), key=lambda c: DENSITY[c]) sorting by Density value
#     return [liquids[d:d + column] for d in xrange(0, len(liquids), column)]


def separate_liquids(glass):
    glass_dict = {'O':0, 'A':0, 'W':0, 'H':0}
    for row in glass:
        for el in row:
            glass_dict[el] += 1
    print glass_dict
    for i in xrange(len(glass)):
        for j in xrange(len(glass[0])):
            if glass_dict['O'] > 0:
                glass[i][j] = 'O'
                glass_dict['O'] -= 1
            elif glass_dict['A'] > 0:
                glass[i][j] = 'A'
                glass_dict['A'] -= 1
            elif glass_dict['W'] > 0:
                glass[i][j] = 'W'
                glass_dict['W'] -= 1
            elif glass_dict['H'] > 0:
                glass[i][j] = 'H'
                glass_dict['H'] -= 1
    return glass


    # O, A, W, H  = 0, 1, 2, 3
    # print glass
    # tmp = []
    # list_liq = [item for sublist in glass for item in sublist]
    # for k, g in groupby(sorted(list_liq)):
    #     tmp.extend(list(g))
    # act_ind = 0
    # if 'O' in tmp:
    #     ind = tmp.index('O')
    #     cnt = tmp.count('O')
    #     tmp.insert(act_ind, tmp[ind:ind+cnt])
    #     act_ind += cnt
    #     tmp[ind:ind+cnt]
    # if list(g[0]) == 'A':
    #     pass
    # if list(g[0]) == 'W':
    #     pass
    # if list(g[0]) == 'H':
    #     pass
    #
    #
    # print tmp
    # for row_ind in xrange(len(glass)):
    #     for col_ind in xrange(len(glass[0])):
    #         glass[row_ind][col_ind] =




def main():
    print separate_liquids([['H', 'H', 'W', 'H'],['W','W','O','W'],['H','H','O','O']])

# turn know great-aunts aunt look A to back
#
# turn great-aunts know aunt look A to back
#
# turn great-aunts know aunt A look to back

if __name__ == '__main__':
    main()