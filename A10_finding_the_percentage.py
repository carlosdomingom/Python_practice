if __name__ == '__main__':
    student_marks = {}
    n = int(input())
    for _ in range(n):
        student = input().split()
        # Almaceno en el nombre el primer split, el resto son las notas
        name, marks = student[0], list(map(float, student[1:]))
        # Almaceno en el diccionario
        student_marks[name] = marks

    getName = input()
    print("{0:.2f}".format(sum(student_marks[getName]) / len(student_marks[getName])))
