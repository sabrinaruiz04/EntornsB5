# Prova escrita 01
videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {
            "nom": "Nintendo",
            "pais": "Japó"
        },
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {
            "nom": "CD Projekt Red",
            "pais": "Polònia"
        },
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {
            "nom": "EA Sports",
            "pais": "Estats Units"
        },
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []
"""
Exercici 1: Funció de visualització (1,5 punts)
Escriu una funció que rep un diccionari joc i mostra:
Títol en majúscules
Any entre parèntesis
Puntuació amb estrelles
Preu amb €
Exemple: 🎮 THE LEGEND OF ZELDA (2017) - ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ - 59.99€
"""
def mostrar_videojoc(joc):
    # Escriu aquí el teu codi (3-4 línies)
   
#Exemple: 🎮 THE LEGEND OF ZELDA (2017) - ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ - 59.99€
    
    titol = joc["titol"].upper()
    any_llancament = joc["any_llancament"]
    puntuacio = int(joc["puntuacio"])
    preu = joc["preu"]
    
    print(f"🎮 {titol} ({any_llancament}) - {'⭐' * int(puntuacio)} - {preu}€")

# Exercici 2: Funció de cerca (2,5 punts)
# Escriu una funció que busqui un videojoc pel títol (insensible a majúscules) i el retorni (el diccionari). Si no el troba, retorna None.
def buscar_per_titol(titol, videojocs):
    # Escriu aquí el teu codi (4-5 línies)
    
    for joc in videojocs:
        if joc["titol"].upper() == titol.upper():
            return joc
        
    return None
    
# Exercici 3: Gestió de biblioteca (3 punts)
# Escriu una funció afegir_a_biblioteca(titol, videojocs, biblioteca) que:
# Busqui el joc utilitzant buscar_per_títol()
# Si el joc no existeix, retorni "❌ Joc no trobat"
# Si el joc ja està a la biblioteca, retorni "⚠️ Ja està a la biblioteca" 
# Si tot va bé, l'afegeixi i retorni "✅ Joc afegit!"


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    # Escriu aquí el teu codi (8-10 línies)
    
    joc = buscar_per_titol(titol, videojocs)
    
    if joc is None:
        return "❌ Joc no trobat"
    
    if joc in biblioteca:
        return "⚠️ Ja està a la biblioteca"
    
    biblioteca.append(joc)
    return "✅ Joc afegit!"
    

# Exercici 4: Estadístiques (1,5 punts)
# Escriu una funció joc_mes_car() que retorni el videojoc (diccionari) amb el preu més alt de la llista videojocs.
def joc_mes_car(videojocs):
    # Escriu aquí el teu codi (5-6 línies) 
    
    preu_max = videojocs[0]["preu"]
    joc_mes_car = None
    
    for joc in videojocs:
        if joc["preu"] > preu_max:
            preu_max = joc["preu"]
            joc_mes_car = joc
            
    return joc_mes_car


# Exercici 5: Funció Main (1,5 punts)
# # Omple els buits amb les crides correctes a les funcions anteriors, recorda que tens accés a les variables videojocs i biblioteca_personal
def main():
    print("=== GESTIÓ DE VIDEOJOCS ===\n")
   
    # 1. Mostrar tots els videojocs
    print("1. CATÀLEG DE VIDEOJOCS:")
    for joc in videojocs:
        mostrar_videojoc(joc) # BUIT 1: Crida per mostrar cada videojoc
    
    print("\n" + "="*50)
    
    print("\n2. CERCA DE VIDEOJOC:")
    # BUIT 2: Buscar "cyberpunk 2077" (insensible a majúscules)
    joc_trobat = buscar_per_titol("cyberpunk 2077", videojocs)
    if not joc_trobat:
        print("Joc trobat:")
        mostrar_videojoc(joc_trobat) # BUIT 3: Mostrar el joc trobat
    else:
        print("Joc no trobat")
    
    print("\n" + "="*50)
    
    print("\n3. GESTIÓ DE BIBLIOTECA PERSONAL:")
    
    # BUIT 4: Afegir "FIFA 24" a la biblioteca
    resultat1 = afegir_a_biblioteca("FIFA 24", videojocs, biblioteca_personal)
    print(resultat1)

    print("\n" + "="*50)
    
    # 4. Mostrar estadístiques
    print("\n4. ESTADÍSTIQUES:")
    # BUIT 5: Trobar el joc més car
    joc_car = joc_mes_car(videojocs)
    print("El joc més car és:")
    # BUIT 6: Mostrar el joc més car
    mostrar_videojoc(joc_car)
    
    print("\n" + "="*50)
    
    # 5. Mostrar biblioteca personal
    print("\n5. LA MEVA BIBLIOTECA:")
    if biblioteca_personal:
        for joc in biblioteca_personal:
            # BUIT 7: Mostrar cada joc de la biblioteca
            mostrar_videojoc(joc)
    else:
        print("La biblioteca està buida")


if __name__ == "__main__":
    # BUIT 8: Crida a la funció principal
    main()           
    

# """