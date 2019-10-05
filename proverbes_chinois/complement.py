from proverbes_chinois._mot import Mot, Mots


class Complement(Mot):
    def __init__(self, mot, poids=10):
        self.mot = mot
        self.poids = poids

    def __str__(self):
        return self.mot

    def __repr__(self):
        return self.mot

    def f(self):
        return str(self)


class ComplementsMoment(Mots):
    mots = [Complement("si"),
            Complement("quand"),
            Complement("lorsque"),
            Complement("à chaque fois que"),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]


class ComplementsObjectif(Mots):
    mots = [Complement("afin de"),
            Complement("avant de"),
            Complement("pour"),
            Complement("dans l'objectif de", poids=5),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]


class ComplementsVeriteGenerale(Mots):
    mots = [Complement("il est plus facile de"),
            Complement("il faut commencer par"),
            Complement("il faut toujours"),
            Complement("il est préférable de"),
            Complement("il faut"),
            Complement("il faudrait", poids=5),
            Complement("il vaut mieux"),
            Complement("le sage dit qu'il faut"),
            Complement("le sage dit qu'il vaut mieux"),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]


class ComplementsDefiniConcept(Mots):
    mots = [Complement("n'est que", poids=5),
            Complement("ne sourit qu'à"),
            Complement("ne s'apprend qu'avec"),
            Complement("n'est en aucun cas contradictoire avec"),
            Complement("ne s'apprivoise qu'avec"),
            Complement("ne se maitrise qu'en observant"),
            Complement("est à l'image de"),
            Complement("met en valeur le paradigme de"),
            Complement("sublime"),
            Complement("magnifie"),
            Complement("transcende"),
            Complement("approuve"),
            Complement("dépasse"),
            Complement("peut être à l'origine de"),
            Complement("permet de comprendre"),
            Complement("n'est pas la cause de"),
            Complement("n'ignore pas"),
            Complement("n'est pas étranger à la réussite de"),
            Complement("rend possible"),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]


class ComplementsContextes(Mots):
    mots = [Complement("à la tombée de la nuit"),
            Complement("lorqu'il fait froid"),
            Complement("derrière chaque sourire"),
            Complement("à l'aube"),
            Complement("selon le contexte"),
            Complement("pendant la bataille"),

            Complement("avec joie"),
            Complement("avec entrain"),
            Complement("silencieusement", poids=15),
            Complement("calmement", poids=10),
            Complement("dans le calme", poids=15),
            Complement("brutalement", poids=15),
            Complement("en silence"),
            Complement("sagement"),
            Complement("avec fracas"),
            Complement("dans les buissons"),
            Complement("à l'entrée du temple"),
            Complement("au sommet de la colline"),
            Complement("en haut de la montagne"),
            Complement("au milieu de la foret"),
            Complement("dans les bois"),
            Complement("dans la capitale"),
            Complement("à la campagne"),
            Complement("au beau milieu des rizières"),
            Complement("dans les champs"),
            Complement("au milieu des bambous"),
            Complement("dans l'enceinte du temple"),
            Complement("en haut de la grande muraille"),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]


class SujetsVagues(Mots):
    mots = [Complement("celui qui"),
            Complement("on"),
            Complement("qui"),
            Complement("le sage qui"),
            ]

    def get_and_format(self, ctr=None):
        return [self.get_one(ctr_fct=ctr).f(), ]
