if __name__ == '__main__':
    mylist = []
    command = []
    n = int(input())
    for _ in range(n):
        command = list(input().split())
        if(len(command) == 1):
            if(command[0] == 'print'):
                print(mylist)
            elif(command[0] == 'sort'):
                mylist.sort()
            elif(command[0] == 'pop'):
                mylist.pop(-1)
            elif(command[0] == 'reverse'):
                mylist = mylist[::-1]
        elif(len(command) == 2):
            if(command[0]) == 'remove':
                mylist.remove(int(command[1]))
            elif(command[0]) == 'append':
                mylist.append(int(command[1]))
        elif(command[0] == 'insert'):
            mylist.insert(int(command[1]), int(command[2]))
