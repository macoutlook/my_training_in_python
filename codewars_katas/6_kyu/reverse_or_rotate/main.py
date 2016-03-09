import textwrap
import collections


def revrot(strng, sz):
    sum_of_cubes = 0
    if (not strng) or (sz <= 0) or (sz > len(strng)):
        return ""

    chunks = textwrap.wrap(strng, sz)
    if len(chunks[-1]) < sz:
        chunks = chunks[:-1]

    for ind, chunk in enumerate(chunks):
        for el in chunk:
            sum_of_cubes += int(el) ** 3
        if sum_of_cubes % 2 == 0:
            chunks[ind] = "".join(reversed(chunk))
        else:
            chunk_deq = collections.deque(chunk)
            chunk_deq.rotate(-1)
            chunks[ind] = "".join(chunk_deq)
        sum_of_cubes = 0
    return "".join(chunks)


def main():
    s = "733049910872815764"
    s1 = "7330499173304991"
    print revrot(s1, 8)
    # '733049910872815' should equal '330479108928157'         73304991

if __name__ == '__main__':
    main()
