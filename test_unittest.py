# test_unittest.py
"""
Fitxer de tests per a Prova_escrita_01 i Prova_escrita_02

Aquest fitxer importa les solucions de les dues proves i crea
dues classes de tests independents, cadascuna amb la seva bateria
de comprovacions. Cada mètode inclou docstrings i comentaris
"""

import unittest

# Importem les funcions de les dues proves
import prova_escrita_01 as p1
import prova_escrita_02 as p2


# TESTOS PER A LA PRIMERA PROVA
# -------------------------------------------------------------------

class TestProva1(unittest.TestCase):
    """Tests dels exercicis 1, 2, 3 i 4 de la Prova_escrita_02."""

    def test_ex1_buscar_per_titol(self):
        """
        Comprova que la cerca per títol funcioni correctament, incloent-hi
        la insensibilitat a majúscules i el cas d’un títol inexistent.
        """
        jocs = p1.videojocs

        # Cerca normal, sense tenir en compte majúscules/minúscules
        resultat = p1.buscar_per_titol("cyberpunk 2077", jocs)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "Cyberpunk 2077")

        # Quan el joc no existeix, ha de retornar None
        self.assertIsNone(p1.buscar_per_titol("Aquest no existeix", jocs))

    def test_ex2_afegir_a_biblioteca(self):
        """
        Valida el procés d’afegir videojocs a la biblioteca personal,
        comprovant afegits correctes, duplicats i intents amb jocs inexistents.
        """
        biblio = []

        # Afegim un joc per primer cop
        self.assertEqual(
            p1.afegir_a_biblioteca("FIFA 24", p1.videojocs, biblio),
            "✅ Joc afegit!"
        )

        # Intentem afegir-lo un altre cop → ja hi és
        self.assertEqual(
            p1.afegir_a_biblioteca("FIFA 24", p1.videojocs, biblio),
            "⚠️ Ja està a la biblioteca"
        )

        # Intentem afegir un joc que no existeix
        self.assertEqual(
            p1.afegir_a_biblioteca("No hi és", p1.videojocs, biblio),
            "❌ Joc no trobat"
        )

    def test_ex3_joc_mes_car(self):
        """
        Comprova que la funció retorni el videojoc amb el preu més alt
        de la llista proporcionada.
        """
        # FIFA 24 és el més car de la llista
        joc_car = p1.joc_mes_car(p1.videojocs)
        self.assertEqual(joc_car["titol"], "FIFA 24")



# TESTOS PER A LA SEGONA PROVA
# -------------------------------------------------------------------

class TestProva2(unittest.TestCase):
    """Tests dels exercicis 2, 3 i 4 de la Prova_escrita_01."""

    def test_ex2_crear_sequencia(self):
        """
        Comprova que crear_sequencia() generi correctament la llista de números
        i que retorni una llista buida quan els paràmetres no són vàlids.
        """
        # Cas normal: inici < final
        self.assertEqual(p2.crear_sequencia(2, 5), [2, 3, 4, 5])

        # Quan l’inici és més gran que el final, no té sentit generar res
        self.assertEqual(p2.crear_sequencia(8, 3), [])

        # Inici negatiu → no és vàlid segons l’enunciat
        self.assertEqual(p2.crear_sequencia(-4, 10), [])

        # Tipus incorrectes → la funció hauria de retornar llista buida
        self.assertEqual(p2.crear_sequencia("hola", 7), [])

    def test_ex3_numeros_imparells_majors(self):
        """
        Verifica que la funció filtri correctament els números senars que
        superen un límit i que gestioni bé casos buits o no vàlids.
        """
        # Llista amb diversos números, alguns senars i majors que el límit
        self.assertEqual(p2.numeros_imparells_majors([1, 4, 5, 9], 3), [5, 9])

        # Llista buida → no hi ha res a filtrar
        self.assertEqual(p2.numeros_imparells_majors([], 10), [])

        # Tipus incorrecte per a la llista
        self.assertEqual(p2.numeros_imparells_majors("text", 2), [])

    def test_ex4_primera_posicio(self):
        """
        Comprova que primera_posicio() retorni la primera coincidència d’un element
        o -1 quan no es troba dins la llista.
        """
        # L’element apareix diverses vegades, però només ens interessa la primera
        self.assertEqual(p2.primera_posicio([4, 7, 7, 2], 7), 1)

        # L’element no hi és
        self.assertEqual(p2.primera_posicio([1, 2, 3], 99), -1)

        # Llista amb un sol element
        self.assertEqual(p2.primera_posicio([8], 8), 0)

    def test_ex5_diagonal_principal(self):
        """
        Test de diagonal_principal() amb matrius quadrades vàlides i comprovacions
        de casos no vàlids com matrius rectangulars o tipus incorrectes.
        """
        # Matriu quadrada senzilla
        self.assertEqual(p2.diagonal_principal([[3, 1], [9, 7]]), [3, 7])

        # Matriu rectangular → no és quadrada, així que ha de fallar
        self.assertEqual(p2.diagonal_principal([[1, 2, 3], [4, 5, 6]]), [])

        # Tipus incorrecte (no és una matriu)
        self.assertEqual(p2.diagonal_principal("no és una matriu"), [])




# Execució directa del fitxer
# ----------------------------

if __name__ == "__main__":
    unittest.main()
