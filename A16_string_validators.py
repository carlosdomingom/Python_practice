if __name__ == '__main__':
    # La función any aplica una función sobre un iterable y devuelve True o
    # False si al menos uno de los elementos del iterable comple la función

    string = input()
    print(any(s.isalnum() for s in string))
    print(any(s.isalpha() for s in string))
    print(any(s.isdigit() for s in string))
    print(any(s.islower() for s in string))
    print(any(s.isupper() for s in string))
