import cowsay
from asciimatics.screen import Screen
from pydub import AudioSegment
from pydub.playback import play

class LlibreAccepcions:
    def __init__(self):
        self.diccionari = {}

    def afegir_paraula(self, paraula, accepcions):
        """
        Afegeix una nova paraula amb les seves accepcions al diccionari.

        :param paraula: La paraula a afegir.
        :param accepcions: Un diccionari que conté les accepcions de la paraula.
        """
        self.diccionari[paraula] = accepcions

    def afegir_accepcio(self, paraula, accepcio, significat):
        """
        Afegeix una nova accepció a una paraula existent.

        :param paraula: La paraula a la qual s'afegirà l'accepció.
        :param accepcio: El tipus o la definició de l'accepció.
        :param significat: El significat o la descripció de l'accepció.
        """
        if paraula in self.diccionari:
            self.diccionari[paraula][accepcio] = significat
        else:
            print("La paraula no existeix. Si us plau, afegiu primer la paraula.")

    def mostrar_paraules(self):
        """
        Mostra totes les paraules del diccionari.
        """
        print("Paraules:")
        for paraula in self.diccionari:
            print(paraula)

    def mostrar_accepcions(self, paraula):
        """
        Mostra les accepcions d'una paraula donada.

        :param paraula: La paraula de la qual es mostraran les accepcions.
        """
        if paraula in self.diccionari:
            print(f"Accepcions de '{paraula}':")
            for accepcio, significat in self.diccionari[paraula].items():
                print(f"{accepcio}: {significat}")
                # Representar l'accepció com una bombolla de text amb Cowsay
                cowsay.cow(f"{accepcio}: {significat}")
        else:
            print("La paraula no existeix.")

    def modificar_accepcio(self, paraula, accepcio, nou_significat):
        """
        Modifica el significat d'una accepció existent d'una paraula.

        :param paraula: La paraula a la qual pertany l'accepció.
        :param accepcio: El tipus o la definició de l'accepció a modificar.
        :param nou_significat: El nou significat o descripció de l'accepció.
        """
        if paraula in self.diccionari:
            if accepcio in self.diccionari[paraula]:
                self.diccionari[paraula][accepcio] = nou_significat
            else:
                print("L'accepció no existeix per a aquesta paraula.")
        else:
            print("La paraula no existeix.")

    def eliminar_paraula(self, paraula):
        """
        Elimina una paraula i totes les seves accepcions del diccionari.

        :param paraula: La paraula a eliminar.
        """
        if paraula in self.diccionari:
            del self.diccionari[paraula]
        else:
            print("La paraula no existeix.")

    def eliminar_accepcio(self, paraula, accepcio):
        """
        Elimina una accepció d'una paraula del diccionari.

        :param paraula: La paraula de la qual es eliminarà l'accepció.
        :param accepcio: El tipus o la definició de l'accepció a eliminar.
        """
        if paraula in self.diccionari:
            if accepcio in self.diccionari[paraula]:
                del self.diccionari[paraula][accepcio]
            else:
                print("L'accepció no existeix per a aquesta paraula.")
        else:
            print("La paraula no existeix.")

def mostrar_portada():
    """
    Mostra una portada animada del programa.
    """
    title = "El Llibre de les Accepcions"
    Screen.wrapper(_portada_animada, arguments=[title])

def _portada_animada(screen, title):
    """
    Funció interna per a mostrar la portada animada.

    :param screen: L'objecte de pantalla de Asciimatics.
    :param title: El títol del programa.
    """
    screen.clear()
    screen.print_at(title, 0, screen.height // 2, Screen.COLOUR_GREEN)
    screen.refresh()

def reproduir_audio(acció):
    """
    Reprodueix un àudio per a una determinada acció de l'usuari.

    :param acció: La descripció de l'acció de l'usuari.
    """
    if acció == "afegir":
        audio = AudioSegment.from_file("afegir_audio.mp3")
    elif acció == "eliminar":
        audio = AudioSegment.from_file("eliminar_audio.mp3")
    else:
        return

    play(audio)

# Exemple d'ús
llibre = LlibreAccepcions()
llibre.afegir_paraula("xarxa", {"PESCA": "Ormeig de pescar...", "TÈXTIL": "Teixit de les xarxes de pescar..."})

mostrar_portada()

while True:
    print("\nMenu:")
    print("1. Afegir paraula")
    print("2. Afegir accepcio")
    print("3. Mostrar paraules")
    print("4. Mostrar accepcions")
    print("5. Sortir")

    opcio = input("Escull una opció: ")

    if opcio == "1":
        paraula = input("Introdueix la paraula: ")
        accepcions = {}
        num_accepcions = int(input("Quantes accepcions té aquesta paraula? "))
        for _ in range(num_accepcions):
            accepcio = input("Introdueix l'accepció: ")
            significat = input("Introdueix el significat: ")
            accepcions[accepcio] = significat
        llibre.afegir_paraula(paraula, accepcions)
        reproduir_audio("afegir")
    elif opcio == "2":
        paraula = input("Introdueix la paraula: ")
        accepcio = input("Introdueix l'accepció: ")
        significat = input("Introdueix el significat: ")
        llibre.afegir_accepcio(paraula, accepcio, significat)
        reproduir_audio("afegir")
    elif opcio == "3":
        llibre.mostrar_paraules()
    elif opcio == "4":
        paraula = input("Introdueix la paraula: ")
        llibre.mostrar_accepcions(paraula)
    elif opcio == "5":
        print("Adeu!")
        break
    else:
        print("Opció invàlida. Si us plau, tria una opció vàlida.")