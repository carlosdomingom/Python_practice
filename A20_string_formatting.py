if __name__ == '__main__':
    n = int(input())
    maxlenght = len(bin(n))-1
    for x in range(1, n+1):
        print(str(x).rjust(maxlenght-1), end = '')
        print(oct(x)[2:].upper().rjust(maxlenght), end='')
        print(hex(x)[2:].upper().rjust(maxlenght), end='')
        print(bin(x)[2:].upper().rjust(maxlenght))
