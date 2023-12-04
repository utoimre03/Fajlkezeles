def negyedik():
    # beolvasás
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="UTF-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    #lista kiírása
    kiFajl = open("fajlok/negyedik.txt", "w", encoding="UTF-8")
    for index in range(0, len(lista), 1):
        # a sorokat eldarabolom szóközök mentén egy listába
        daraboltSor = lista[index].split(" ")
        # a lista 0. elemét (1. szót) írom a fájlba
        print(daraboltSor[0], file=kiFajl)
        # kiFajl.write(lista[index])
    kiFajl.close()