
if __name__ == '__main__':
    lin, col = map(int, input().split())
    for l in range(lin):
        if l < (lin//2):
            ornaments = 2*l+1
        elif l > (lin//2):
            ornaments = (2*l)*-1+(lin*2)-1
        else:
            ornaments = 0

        if ornaments == 0:
            print('WELCOME'.center(col, '-'))
        else:
            print('-' * ((col - ornaments*3)//2), end = '')
            print('.|.' * (ornaments), end = '')
            print('-' * ((col - ornaments*3)//2))
