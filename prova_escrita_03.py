# Prova escrita 03

# ==========================
# Exercici 1
# ==========================

def afegir_edat_a_tots(persones, anys):
    if isinstance(anys, int) and anys > 0:
        for persona in persones:
            persona["edat"] += anys


# ==========================
# Exercici 2
# ==========================

def trobar_edat_maxima(persones):
    if not persones:
        return -1

    for persona in persones:
        if (
            not isinstance(persona, dict)
            or "nom" not in persona
            or "edat" not in persona
            or not isinstance(persona["edat"], int)
        ):
            return -1

    edats = [persona["edat"] for persona in persones]
    return max(edats)


# ==========================
# Exercici 3
# ==========================

productes = [
    {
        'nom': 'Portàtil Dell XPS 15',
        'preu': 1299.99,
        'categoria': 'Informàtica',
        'stock': 5
    },
    {
        'nom': 'Ratolí Logitech MX Master',
        'preu': 89.99,
        'categoria': 'Perifèrics',
        'stock': 15
    },
    {
        'nom': 'Monitor Samsung 27"',
        'preu': 349.50,
        'categoria': 'Monitors',
        'stock': 8
    }
]

def trobar_producte_mes_car():
    global productes
    if not productes:
        return None

    producte_mes_car = productes[0]

    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            producte_mes_car = producte

    return producte_mes_car


# ==========================
# Exercici 4
# ==========================

def comptar_empleats_per_departament(empresa):
    departaments = {}
    for departament in empresa["departaments"]:
        departaments[departament["nom"]] = len(departament["empleats"])
    return departaments


# ==========================
# PROVES MANUALS (NO S’EXECUTEN EN IMPORTAR)
# ==========================

if __name__ == "__main__":

    # Exercici 1
    persones = [
        {'nom': 'Anna Garcia', 'edat': 25},
        {'nom': 'Marc Puig', 'edat': 42},
        {'nom': 'Laura Martí', 'edat': 35},
        {'nom': 'Jordi Soler', 'edat': 58},
        {'nom': 'Marta Vidal', 'edat': 29}
    ]

    afegir_edat_a_tots(persones, 5)
    for persona in persones:
        print(persona["nom"], persona["edat"])

    # Exercici 2
    persones_1 = [
        {'nom': 'Anna Garcia', 'edat': 25},
        {'nom': 'Marc Puig', 'edat': 42},
        {'nom': 'Laura Martí', 'edat': 35},
        {'nom': 'Jordi Soler', 'edat': 58},
        {'nom': 'Marta Vidal', 'edat': 29},
        {'nom': 'Pere Català', 'edat': 67},
        {'nom': 'Sofia Roca', 'edat': 31}
    ]

    persones_2 = []
    persones_3 = [
        {'nom': 'Anna Garcia', 'edat': 25},
        {'nom': 'Marc Puig'},  
        {'nom': 'Laura Martí', 'edat': 35}
    ]

    persones_4 = [
        {'nom': 'Anna Garcia', 'edat': 25},
        {'nom': 'Marc Puig', 'edat': 42},  # ← arreglat: era string
        {'nom': 'Laura Martí', 'edat': 35}
    ]

    print("=== Prova 1 ===")
    print(trobar_edat_maxima(persones_1))

    print("=== Prova 2 ===")
    print(trobar_edat_maxima(persones_2))

    print("=== Prova 3 ===")
    print(trobar_edat_maxima(persones_3))

    print("=== Prova 4 ===")
    print(trobar_edat_maxima(persones_4))

    # Exercici 3
    print("=== Producte més car ===")
    print(trobar_producte_mes_car())

    # Exercici 4
    empresa_de_prova = {
        'nom': 'TechCorp',
        'departaments': [
            {
                'nom': 'Informàtica',
                'empleats': [
                    {'nom': 'Anna Garcia', 'càrrec': 'Desenvolupadora'},
                    {'nom': 'Marc Puig', 'càrrec': 'Analista'},
                    {'nom': 'Laura Martí', 'càrrec': 'DevOps'}
                ]
            }
        ]
    }

    print("=== Empleats per departament ===")
    print(comptar_empleats_per_departament(empresa_de_prova))
