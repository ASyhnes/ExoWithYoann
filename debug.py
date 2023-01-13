class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

rectangle1 = Rectangle(5, 3)

print(rectangle1.length)

class Voiture:
    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )
    def __init__(self, modele, marque, prix):
        self.modele = modele
        self.marque = marque
        self.nbr_siege = nbr_siege
        self.distance = distance

voiture1 = Voiture('modus','renaud',4000)
voiture2 = Voiture('ModeleS','Tesla',65000)


print(voiture2.modele)