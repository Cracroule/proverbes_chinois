from _mot import Mot, Mots
from _contexte import all_genres, all_nombres


class Adjectif(Mot):
    def __init__(self, singulier_masc, singulier_fem, pluriel_masc, pluriel_fem, tags=None, poids=10):
        if tags is None:
            tags = list()

        self.singulier_masc = singulier_masc
        self.singulier_fem = singulier_fem
        self.pluriel_masc = pluriel_masc
        self.pluriel_fem = pluriel_fem
        self.tags = tags[:]
        self.poids = poids

    def __str__(self):
        return self.singulier_masc

    def __repr__(self):
        return self.singulier_masc

    def f(self, nombre="singulier", genre="masculin"):
        assert(nombre in all_nombres)
        assert(genre in all_genres)
        if (nombre, genre) == ("singulier", "masculin"):
            return self.singulier_masc
        if (nombre, genre) == ("singulier", "feminin"):
            return self.singulier_fem
        if (nombre, genre) == ("pluriel", "masculin"):
            return self.pluriel_masc
        if (nombre, genre) == ("pluriel", "feminin"):
            return self.pluriel_fem


class AdjectifsPost(Mots):
    mots = [Adjectif("le plus grand", "la plus grande", "les plus grands", "les plus grandes"),
            Adjectif("le plus beau", "la plus belle", "les plus beaux", "les plus belles"),
            Adjectif("parfait", "parfaite", "parfaits", "parfaites"),
            Adjectif("malin", "maline", "malins", "malines"),
            Adjectif("jaune", "jaune", "jaunes", "jaunes"),
            Adjectif("hésitant", "hésitante", "hésitants", "hésitantes"),
            Adjectif("bienveillant", "bienveillante", "bienveillants", "bienveillantes"),
            Adjectif("malveillant", "malveillante", "malveillants", "malveillantes"),
            Adjectif("maudit", "maudite", "maudits", "maudites"),
            Adjectif("bienheureux", "bienheureuse", "bienheureux", "bienheureuses"),
            Adjectif("sanguinaire", "sanguinaire", "sanguinaires", "sanguinaires"),
            Adjectif("lunatique", "lunatique", "lunatiques", "lunatiques"),
            Adjectif("empatique", "empatique", "empatiques", "empatiques"),
            Adjectif("malicieux", "malicieuse", "malicieux", "malicieuses"),
            Adjectif("blessé", "blessée", "blessés", "blessées"),
            Adjectif("souriant", "souriante", "souriants", "souriantes"),
            Adjectif("rouge", "rouge", "rouges", "rouges"),
            Adjectif("en greve", "en greve", "en greve", "en greve"),
            Adjectif("détraqué", "détraquée", "détraqués", "détraquées"),
            Adjectif("carnivore", "carnivore", "carnivores", "carnivores"),
            Adjectif("intelligent", "intelligente", "intelligents", "intelligentes"),
            Adjectif("éloquent", "éloquente", "éloquents", "éloquentes"),
            ]

    def get_and_format(self, ctr=None, nombre="singulier", genre="masculin"):
        return [self.get_one(ctr).f(nombre=nombre, genre=genre), ]


class AdjectifsPre(Mots):
    mots = [Adjectif("grand", "grande", "grands", "grandes"),
            Adjectif("beau", "belle", "beaux", "belles"),
            Adjectif("horrible", "horrible", "horribles", "horribles"),
            Adjectif("somptueux", "somptueuse", "somptueux", "somptueuses"),
            Adjectif("jeune", "jeune", "jeunes", "jeunes"),
            Adjectif("vieux", "vieille", "vieux", "vieilles"),
            Adjectif("paisible", "paisible", "paisibles", "paisibles"),
            Adjectif("vénérable", "vénérable", "vénérables", "vénérables"),
            Adjectif("petit", "petite", "petits", "petites"),
            ]

    def get_and_format(self, ctr=None, nombre="singulier", genre="masculin"):
        return [self.get_one(ctr).f(nombre=nombre, genre=genre), ]


if __name__ == "__main__":
    s = AdjectifsPre()
    for i in range(10):
        print(" ".join(s.get_and_format()))
