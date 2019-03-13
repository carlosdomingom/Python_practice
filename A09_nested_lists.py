if __name__ == '__main__':
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])


    # Primero creo un set con las puntuaciones. Esto elimina los duplicados
    # A continuación la convierto en una lista para poder ordenarla
    # y escojo el segundo elemento de la lista, que será la segunda puntuación
    # más baja
    second_lowest = sorted(list(set([marks for names, marks in marksheet])))[1]

    # A continuación imprimo concateno todos los nombres cuya puntuación
    # coincida con la segunda más baja
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest]))
