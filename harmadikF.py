def harmadik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="UTF-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    #lista kiírása
    kiFajl = open("fajlok/harmadik.txt", "w", encoding="UTF-8")
    for index in range(0, len(lista), 1):
        print(lista[index], file=kiFajl, end="")
        # kiFajl.write(lista[index])
    kiFajl.close()