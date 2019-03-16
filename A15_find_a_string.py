if __name__ == '__main__':

    def count_substring(string, sub_string):
        counter = 0
        index = 0
        while index != -1:
            index = string.find(sub_string, index)
            if index != -1:
                index += 1
                counter += 1

        return(counter)


    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
