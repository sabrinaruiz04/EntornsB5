# Prova escrita 03 - Tests
"""
Tests parametritzats per a Prova Escrita 03.
Inclou proves per als exercicis 1, 2, 3 i 4.
"""

import pytest
import prova_escrita_03 as p3   # ← Canvia el nom si cal


# -------------------------------------------------------------------
# EXERCICI 1 — afegir_edat_a_tots
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "persones, anys, esperat",
    [
        (
            [{'nom': 'Anna', 'edat': 20}, {'nom': 'Marc', 'edat': 30}],
            5,
            [{'nom': 'Anna', 'edat': 25}, {'nom': 'Marc', 'edat': 35}]
        ),
        (
            [{'nom': 'Laura', 'edat': 10}],
            2,
            [{'nom': 'Laura', 'edat': 12}]
        ),
        (
            [{'nom': 'Jordi', 'edat': 50}],
            -3,
            [{'nom': 'Jordi', 'edat': 50}]   # No ha de modificar res
        )
    ]
)
def test_afegir_edat_a_tots(persones, anys, esperat):
    """
    Comprova que la funció modifica correctament les edats
    i que ignora increments no vàlids.
    """
    p3.afegir_edat_a_tots(persones, anys)
    assert persones == esperat



# -------------------------------------------------------------------
# EXERCICI 2 — trobar_edat_maxima
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "persones, esperat",
    [
        (
            [{'nom': 'Anna', 'edat': 20}, {'nom': 'Marc', 'edat': 40}],
            40
        ),
        (
            [],
            -1
        ),
        (
            [{'nom': 'Anna'}, {'nom': 'Marc', 'edat': 40}],
            -1
        ),
        (
            [{'nom': 'Anna', 'edat': '20'}, {'nom': 'Marc', 'edat': 40}],
            -1
        )
    ]
)
def test_trobar_edat_maxima(persones, esperat):
    """
    Comprova que la funció retorna l'edat màxima
    i valida correctament errors de format.
    """
    assert p3.trobar_edat_maxima(persones) == esperat



# -------------------------------------------------------------------
# EXERCICI 3 — trobar_producte_mes_car
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "productes, esperat",
    [
        (
            [
                {'nom': 'A', 'preu': 10},
                {'nom': 'B', 'preu': 50},
                {'nom': 'C', 'preu': 30}
            ],
            {'nom': 'B', 'preu': 50}
        ),
        (
            [],
            None
        )
    ]
)
def test_trobar_producte_mes_car(productes, esperat, monkeypatch):
    """
    Comprova que retorna el producte amb preu més alt
    i None si la llista global està buida.
    """
    # Substituïm la variable global productes
    monkeypatch.setattr(p3, "productes", productes)

    assert p3.trobar_producte_mes_car() == esperat



# -------------------------------------------------------------------
# EXERCICI 4 — comptar_empleats_per_departament
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "empresa, esperat",
    [
        (
            {
                'nom': 'Test',
                'departaments': [
                    {'nom': 'IT', 'empleats': [{'nom': 'A'}, {'nom': 'B'}]},
                    {'nom': 'RH', 'empleats': [{'nom': 'C'}]}
                ]
            },
            {'IT': 2, 'RH': 1}
        ),
        (
            {
                'nom': 'Test',
                'departaments': []
            },
            {}
        )
    ]
)
def test_comptar_empleats_per_departament(empresa, esperat):
    """
    Comprova que retorna un diccionari amb el nombre d'empleats
    per cada departament.
    """
    assert p3.comptar_empleats_per_departament(empresa) == esperat
