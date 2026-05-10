# Prova escrita 02
"""
Exercici 1 (2 punts)
Escriu una funció crear_sequencia(inici, final) que generi una llista amb tots els números des de inici fins a final (ambdós inclosos). Valida que inici i final siguin dos enters positius i inici sigui més petit que final, sinó és així retorna una llista buida.
"""
def crear_sequencia(inici, final):
    l = []
    if isinstance(inici, int) and isinstance(final, int) and inici < final and inici >= 0:
        l = [i for i in range(inici, final + 1)]
    return l

"""
Exercici 2 (2 punts)
Crea una funció numeros_senars_majors(llista, limit) que retorni una nova llista amb només els números senars que siguin majors que limit. Valida que llista sigui una llista no buida i que limit sigui un número enter, sinó retorna una llista buida.
"""
def numeros_imparells_majors(llista, limit):
    l = []
    if isinstance(llista, list) and isinstance(limit, int) and llista:
        l = [i for i in llista if i % 2 != 0 and i > limit]
    return l
"""

Exercici 3 (2 punts)
Fes una funció primera_posicio(llista, element) que trobi la posició de la primera aparició d'un element a la llista. Si no existeix, ha de retornar -1. No pots utilitzar el mètode .index()
"""
def primera_posicio(llista, element):
    posicio = -1
    for i in range(len(llista)):
        if llista[i] == element:
            posicio = i
    return posicio

"""
Exercici 4 (2 punts)
Escriu una funció diagonal_principal(matriu) que retorni una llista amb els elements de la diagonal principal d'una matriu quadrada . Valida que matriu sigui una llista de llistes no buida, que totes les files tinguin la mateixa longitud i que sigui quadrada (mateix número de files i columnes), sinó retorna una llista buida.
"""
def diagonal_principal(matriu):
    l = []
    # penseu una solució més senzilla
    if isinstance(matriu, list) and all(isinstance(fila, list) and len(fila) == len(matriu[0]) for fila in matriu) and len(matriu) == len(matriu[0]):
        l = [matriu[i][i] for i in range(len(matriu))]
    return l


"""
Crida de les funcions (1 punt)
"""
def main():
    # Dades de prova
    llista_prova = [3, -1, 7, 2, -1, 9, 4, 7]
    matriu_prova = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    llista_buida = []
    matriu_no_quadrada = [[1, 2], [3, 4, 5]]

    print("=== PROVES DE LES FUNCIONS ===")

    # Prova 1: crear_sequencia
    print("\n1. Funció crear_sequencia:")
    resultat1a = crear_sequencia(5, 10)  # Cas vàlid
    resultat1b = crear_sequencia(10, 5)  # Cas invàlid
    resultat1c = crear_sequencia(-2, 5)  # Cas invàlid (negatiu)
    print(f"crear_sequencia(5, 10) = {resultat1a}")
    print(f"crear_sequencia(10, 5) = {resultat1b}")
    print(f"crear_sequencia(-2, 5) = {resultat1c}")

    # Prova 2: numeros_imparells_majors  
    print("\n2. Funció numeros_imparells_majors:")
    resultat2a = numeros_imparells_majors(llista_prova, 3)  # Cas vàlid
    resultat2b = numeros_imparells_majors(llista_buida, 3)  # Cas invàlid
    print(f"numeros_imparells_majors({llista_prova}, 3) = {resultat2a}")
    print(f"numeros_imparells_majors([], 3) = {resultat2b}")

    # Prova 3: primera_posicio
    print("\n3. Funció primera_posicio:")
    resultat3a = primera_posicio(llista_prova, 7)   # Cas vàlid
    resultat3b = primera_posicio(llista_prova, 15)  # Cas vàlid
    resultat3c = primera_posicio(llista_buida, 5)   # Cas invàlid
    print(f"primera_posicio({llista_prova}, 7) = {resultat3a}")
    print(f"primera_posicio({llista_prova}, 15) = {resultat3b}")
    print(f"primera_posicio([], 5) = {resultat3c}")

    # Prova 4: diagonal_principal
    print("\n4. Funció diagonal_principal:")
    resultat4a = diagonal_principal(matriu_prova)  # Cas vàlid
    resultat4b = diagonal_principal(matriu_no_quadrada)  # Cas invàlid
    print(f"diagonal_principal({matriu_prova}) = {resultat4a}")
    print(f"diagonal_principal({matriu_no_quadrada}) = {resultat4b}")


if __name__ == "__main__":
    main()

"""
Sortida Esperada per consola (1 punt):
Completa la sortida per consola segons el codi de la funció main()
=== PROVES DE LES FUNCIONS ===

1. Funció crear_sequencia:
crear_sequencia(5, 10) = [5, 6, 7, 8, 9, 10]
crear_sequencia(10, 5) = []
crear_sequencia(-2, 5) = []

2. Funció numeros_imparells_majors:
numeros_imparells_majors([3, -1, 7, 2, -1, 9, 4, 7], 3) = [7, 9, 7]
numeros_imparells_majors([], 3) = []

3. Funció primera_posicio:
primera_posicio([3, -1, 7, 2, -1, 9, 4, 7], 7) = 7
primera_posicio([3, -1, 7, 2, -1, 9, 4, 7], 15) = -1
primera_posicio([], 5) = -1

4. Funció diagonal_principal:
diagonal_principal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = [1, 5, 9]
diagonal_principal([[1, 2], [3, 4, 5]]) = []
"""