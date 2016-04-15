def snail(array):
    res_tab = []
    right, down = 2 * (len(array),)
    left, top = 0, 0
    len_arr = len(array)
    all_el = (len_arr * len(array[0]))
    while True:
        # right
        res_tab.extend(array[top][left:right])
        print "right", res_tab
        top += 1
        if  all_el == len(res_tab):
            break
        # down
        res_tab.extend([row[right-1] for row in array[top:down]])
        print "down", res_tab
        right -= 1
        if  all_el == len(res_tab):
            break
        # left
        res_tab.extend(reversed(array[down-1][left:right]))
        print "left", res_tab
        down -= 1
        if  all_el == len(res_tab):
            break
        # top
        res_tab.extend(reversed([row[left] for row in array[top:down]]))
        print "top", res_tab
        left += 1
        if  all_el == len(res_tab):
            break

    return res_tab

def main():
    # print snail([[1,2,3],
    #              [4,5,6],
    #              [7,8,9]])

    print snail([[1,2,3],
         [8,9,4],
         [7,6,5]])

if __name__ == '__main__':
    main()