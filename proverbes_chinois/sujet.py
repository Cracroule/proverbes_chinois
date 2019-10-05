from numpy.random import choice

from _mot import Mot, Mots
from _contexte import all_tags_sujets, all_genres, all_nombres, all_articles
from article import ajoute_article
from adjectif import AdjectifsPre, AdjectifsPost
from contrainte import contrainte_evite_tag, compose_contraintes


class Sujet(Mot):
    def __init__(self, singulier, pluriel, genre, tags=None, poids=10):
        if tags is None:
            tags = list()

        assert(genre in all_genres)
        assert(all(t in all_tags_sujets for t in tags))

        self.singulier = singulier
        self.pluriel = pluriel
        self.genre = genre
        self.tags = tags[:]
        self.poids = poids

    def __str__(self):
        return self.singulier

    def __repr__(self):
        return self.singulier

    def f(self, nombre="singulier", article="defini"):
        mot = self.singulier if nombre == "singulier" else self.pluriel
        if article is None:
            return mot
        assert (nombre in all_nombres)
        return ajoute_article(mot, genre=self.genre, nombre=nombre, article=article)


class Sujets(Mots):
    mots = [Sujet("homme", "hommes", "masculin", ["vivant", "humain", ]),
            Sujet("femme", "femmes", "feminin", ["vivant", "humain", ]),
            Sujet("garçon", "garçons", "masculin", ["vivant", "humain", ]),
            Sujet("enfant", "enfants", "masculin", ["vivant", "humain", ]),
            Sujet("professeur", "professeurs", "masculin", ["vivant", "humain", ]),
            Sujet("courtisane", "courtisanes", "feminin", ["vivant", "humain", ]),
            Sujet("fille", "filles", "feminin", ["vivant", "humain", ], poids=5),
            Sujet("sage", "sages", "masculin", ["vivant", "humain", ]),
            Sujet("moine", "moines", "masculin", ["vivant", "humain", ]),
            Sujet("philosophe", "philosophes", "masculin", ["vivant", "humain", ]),
            Sujet("idiot", "idiots", "masculin", ["vivant", "humain", ]),
            Sujet("soldat", "soldats", "masculin", ["vivant", "humain", ]),
            Sujet("commandant", "commandants", "masculin", ["vivant", "humain", ]),
            Sujet("armée", "armées", "feminin", ["vivant", "humain", ]),
            Sujet("empereur", "empereurs", "masculin", ["vivant", "humain", ]),
            Sujet("mendiant", "mendiants", "masculin", ["vivant", "humain", ]),
            Sujet("marchant", "marchants", "masculin", ["vivant", "humain", ]),
            Sujet("prisonnier", "prisonniers", "masculin", ["vivant", "humain", ]),

            Sujet("chien", "chiens", "masculin", ["vivant", "animal", "comestible"]),
            Sujet("tigre", "tigres", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("panda", "pandas", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("chat", "chats", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("cochon", "cochons", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("serpent", "serpents", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("poney", "poneys", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("taureau", "taureaux", "masculin", ["vivant", "animal", "comestible", ]),
            Sujet("boeuf", "boeufs", "masculin", ["vivant", "animal", "comestible", ]),

            Sujet("dragon", "dragons", "masculin", ["vivant", "animal", ]),
            Sujet("papillon", "papillons", "masculin", ["vivant", "animal", ]),
            Sujet("rat", "rats", "masculin", ["vivant", "animal", ]),
            Sujet("souris", "souris", "feminin", ["vivant", "animal", ]),
            Sujet("singe", "singes", "masculin", ["vivant", "animal", ]),
            Sujet("éléphant", "éléphants", "masculin", ["vivant", "animal", ], ),
            Sujet("oiseau", "oiseaux", "masculin", ["vivant", "animal", ], ),

            Sujet("banane", "bananes", "feminin", ["comestible", "inerte", ], poids=5),
            Sujet("ratatouille", "ratatouilles", "feminin", ["comestible", "inerte", ], poids=3),
            Sujet("pomme", "pommes", "feminin", ["comestible", "inerte", ], poids=5),
            Sujet("bol de riz", "bols de riz", "masculin", ["comestible", "inerte", ], poids=3),
            Sujet("grain de riz", "grains de riz", "masculin", ["comestible", "inerte", ]),
            Sujet("tofu", "morceaux de tofu", "masculin", ["comestible", "inerte", ], poids=6),
            Sujet("soja", "sojas", "masculin", ["comestible", "inerte", ], poids=5),

            Sujet("amour", "amours", "masculin", ["concept", "unique", ]),
            Sujet("tristesse", "tristesses", "feminin", ["concept", "unique", ]),
            Sujet("bonheur", "bonheurs", "masculin", ["concept", "unique", ]),
            Sujet("mélancolie", "mélancolies", "feminin", ["concept", "unique", ]),
            Sujet("joie", "joies", "feminin", ["concept", "unique", ]),
            Sujet("destin", "destins", "masculin", ["concept", "unique", ]),
            Sujet("chemin", "chemins", "masculin", ["concept", "unique", ]),
            Sujet("périple", "périples", "masculin", ["concept", "unique", ]),
            Sujet("sagesse", "sagesses", "feminin", ["concept", "unique", ]),
            Sujet("intelligence", "intelligences", "feminin", ["concept", "unique", ]),
            Sujet("gloire", "gloires", "feminin", ["concept", "unique", ]),
            Sujet("reconnaissance", "reconnaissances", "feminin", ["concept", "unique", ]),
            Sujet("animosité", "animosités", "feminin", ["concept", "unique", ]),
            Sujet("mensonge", "mensonges", "masculin", ["concept", ]),
            Sujet("vérité", "vérités", "feminin", ["concept", "unique", ]),
            Sujet("bien", "biens", "masculin", ["concept", "unique", ]),
            Sujet("mal", "mals", "masculin", ["concept", "unique", ]),
            Sujet("animosité", "animosités", "feminin", ["concept", "unique", ]),
            Sujet("camaraderie", "camaraderies", "feminin", ["concept", "unique", ]),
            Sujet("regret", "regrets", "masculin", ["concept", ]),
            Sujet("rire", "rires", "masculin", ["concept", ]),
            Sujet("endoctrinement", "endoctrinements", "masculin", ["concept", "unique", ], poids=5),
            Sujet("connaissance", "connaissances", "feminin", ["concept", "unique", ]),
            Sujet("fierté", "fiertés", "feminin", ["concept", "unique", ]),
            Sujet("innocence", "innocences", "feminin", ["concept", "unique", ]),
            Sujet("imagination", "imaginations", "feminin", ["concept", "unique", ]),
            Sujet("lumière", "lumières", "feminin", ["concept", "unique", ]),
            Sujet("peur", "peurs", "feminin", ["concept", "unique", ]),
            Sujet("malice", "malices", "feminin", ["concept", "unique", ]),
            Sujet("subconscient", "subconscients", "masculin", ["concept", "unique", ]),
            Sujet("espoir", "espoirs", "masculin", ["concept", "unique", ]),

            Sujet("lune", "lunes", "feminin", ["inerte", "unique", ]),
            Sujet("soleil", "soleils", "masculin", ["inerte", "unique", ]),
            Sujet("eau", "eaux", "feminin", ["inerte", ]),
            Sujet("vent", "vents", "masculin", ["inerte", ]),
            Sujet("feu", "feux", "masculin", ["inerte", ]),
            Sujet("grande muraille", "bordures de la grande muraille", "feminin", ["inerte", ]),
            Sujet("caillou", "cailloux", "masculin", ["inerte", ]),
            Sujet("épee", "épees", "feminin", ["inerte", ], poids=5),
            Sujet("sabre", "sabres", "masculin", ["inerte", ], poids=5),
            Sujet("arc", "arcs", "masculin", ["inerte", ]),
            Sujet("parchemin", "parchemins", "masculin", ["inerte", ]),
            Sujet("océan", "océan", "masculin", ["inerte", ]),
            Sujet("forêt de bambous", "forêts de bambous", "feminin", ["inerte", ]),
            Sujet("bambou", "bambous", "masculin", ["inerte", ]),
            Sujet("encre de chine", "encre de chine", "feminin", ["inerte", ]),
            Sujet("livre", "livres", "masculin", ["inerte", ]),
            Sujet("statue", "statues", "feminin", ["inerte", ]),
            Sujet("feu d'artifice", "feux d'artifice", "feminin", ["inerte", ]),
            Sujet("drapeau", "drapeaux", "masculin", ["inerte", ]),

            Sujet("regard", "regards", "masculin", []),
            Sujet("oeil", "yeux", "masculin", []),
            Sujet("oreille", "oreilles", "feminin", []),
            Sujet("discours", "discours", "masculin", []),
            ]

    def get_and_format(self, ctr=None, nombre="singulier", article="defini"):
        return [self.get_one(ctr).f(nombre=nombre, article=article), ]


class SujetsQualifies(Mots):

    def __init__(self, poids_qualificatif=0.3):
        assert(0. <= poids_qualificatif <= 1.)
        self.poids_qualificatif = poids_qualificatif

    def get_and_format(self, ctr_sujet=None, ctr_adjectif=None, nombre="singulier", article="defini"):
        assert nombre in all_nombres and article in all_articles
        if nombre == "pluriel" or article == "indefini":
            sujet = Sujets().get_one(ctr_fct=compose_contraintes(ctr_sujet, contrainte_evite_tag("unique")))
        else:
            sujet = Sujets().get_one(ctr_fct=ctr_sujet)
        adj_pre = AdjectifsPre()
        adj_post = AdjectifsPost()

        # weight handling for adjectives
        if self.poids_qualificatif:
            poids_pre = sum([m.poids for m in adj_pre.get_all(ctr_adjectif)])
            poids_post = sum([m.poids for m in adj_post.get_all(ctr_adjectif)])
            poids_no_adj = 1. / self.poids_qualificatif * (poids_pre + poids_post)
            p_tot = poids_pre + poids_post + poids_no_adj
            q = choice(["aucun", "avant", "apres"], 1, p=(poids_no_adj/p_tot, poids_pre/p_tot, poids_post/p_tot))[0]
        else:
            q = "aucun"
        if q == "avant":
            q = adj_pre.get_and_format(ctr=ctr_adjectif, nombre=nombre, genre=sujet.genre)[0]
            q = ajoute_article(q, genre=sujet.genre, nombre=nombre, article=article)
            s = sujet.singulier if nombre == "singulier" else sujet.pluriel
            res = [q, s]
        elif q == "apres":
            q = adj_post.get_and_format(ctr=ctr_adjectif, nombre=nombre, genre=sujet.genre)[0]
            s = sujet.f(nombre=nombre, article=article)
            res = [s, q]
        else:
            res = [sujet.f(nombre=nombre, article=article), ]
        return res
