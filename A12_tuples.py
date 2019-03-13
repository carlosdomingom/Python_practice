if __name__ == '__main__':
    mytuple = ()
    n = int(input())
    mytuple = tuple(map(int, input().split()))
    print (hash(mytuple))
