def hetedik():
    # beolvasás
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="UTF-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # kiírás visszafelé
    kiFajl = open("fajlok/hetedik.txt", "w", encoding="UTF-8")
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kiFajl)
    kiFajl.close()
