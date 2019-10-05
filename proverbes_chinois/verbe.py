from _mot import Mot, Mots
from _contexte import all_nombres
from proverbes_chinois.contrainte import contrainte_possede_tag, contrainte_genre, compose_contraintes
from proverbes_chinois.sujet import SujetsQualifies


class Verbe(Mot):
    def __init__(self, infinitif, singulier, pluriel, ctr_suj=None, ctr_compl=None, poids=10):
        # constraints are functions returning a boolean
        assert(ctr_suj is None or callable(ctr_suj))
        assert (ctr_compl is None or callable(ctr_compl))
        self.infinitif = infinitif
        self.singulier = singulier
        self.pluriel = pluriel
        self.ctr_sujet = ctr_suj
        self.ctr_compl = ctr_compl
        self.poids = poids

    def __str__(self):
        return self.infinitif

    def __repr__(self):
        return self.infinitif

    def f(self, type="singulier"):
        assert(type in all_nombres or type in ["infinitif", ])
        if type == "singulier":
            return self.singulier
        if type == "pluriel":
            return self.pluriel
        if type == "infinitif":
            return self.infinitif
        raise TypeError("Nope")


# Define verbs that need a 'complement' following them
class VerbesTransitifs(Mots):
    mots = [Verbe("regarder", "regarde", "regardent"),            Verbe("manger", "mange", "mangent", ctr_compl=contrainte_possede_tag("comestible")),

            Verbe("parler avec", "parle avec", "parlent avec"),
            Verbe("danser avec", "danse avec", "dansent avec"),
            Verbe("marchander avec", "marchande avec", "marchandent avec"),
            Verbe("écouter", "écoute", "écoutent"),
            Verbe("contempler", "contemple", "contemplent"),
            Verbe("observer", "observe", "observent"),
            Verbe("admirer", "admire", "admirent"),
            Verbe("contempler", "contemple", "contemplent"),
            Verbe("torturer", "torture", "torturent"),
            Verbe("vénérer", "vénère", "vénèrent"),
            Verbe("combattre", "combat", "combattent"),
            Verbe("commander", "commande", "commandent"),
            Verbe("diriger", "dirige", "dirigent"),
            Verbe("se prosterner devant", "se prosterne devant", "se prosternent devant"),
            Verbe("frapper", "frappe", "frappent"),
            Verbe("discuter avec", "discute avec", "discutent avec"),
            Verbe("surprendre", "surprend", "surprennent"),
            Verbe("effrayer", "effraie", "effraient"),
            Verbe("comprendre", "comprend", "comprennent"),

            Verbe("s'approcher de", "s'approche de", "s'approchent de"),
            Verbe("s'éloigner de", "s'éloigne de", "s'éloignent de"),
            Verbe("s'envoler vers", "s'envole vers", "s'envolent vers"),
            Verbe("s'attaquer à", "s'attaque à", "s'attaquent à"),
            Verbe("obéir à", "obéit à", "obéissent à"),

            Verbe("prendre conscience de", "prend conscience de", "prennent conscience de",
                  ctr_compl=contrainte_possede_tag("concept")),
            Verbe("appréhender", "appréhende", "appréhendent", ctr_compl=contrainte_possede_tag("concept")),

            Verbe("être battu par", "est battu par", "sont battus par", poids=5,
                  ctr_suj=contrainte_genre("masculin")),
            Verbe("être battue par", "est battue par", "sont battues par", poids=5,
                  ctr_suj=contrainte_genre("feminin")),
            Verbe("être mangé par", "est mangé par", "sont mangés par", poids=5,
                  ctr_suj=compose_contraintes(contrainte_possede_tag("comestible"), contrainte_genre("masculin"))),
            Verbe("être mangée par", "est mangée par", "sont mangées par", poids=5,
                  ctr_suj=compose_contraintes(contrainte_possede_tag("comestible"), contrainte_genre("feminin"))),
            ]

    def get_and_format(self, ctr=None, type="singulier"):
        return [self.get_one(ctr).f(type=type), ]


# Define verbs that do not need a 'complement' following them
class VerbesIntransitifs(Mots):
    mots = [Verbe("être malade", "est malade", "sont malades"),
            Verbe("voir l'avenir", "voit l'avenir", "voient l'avenir"),
            Verbe("écouter", "écoute", "écoutent"),
            Verbe("applaudir", "applaudit", "applaudissent"),
            Verbe("chanter", "chante", "chantent"),
            Verbe("jubiler", "jubile", "jubilent"),
            Verbe("s'emballer", "s'emballe", "s'emballent"),
            Verbe("se briser", "se brise", "se brisent"),
            Verbe("se préparer", "se prépare", "se préparent"),
            Verbe("relativiser", "relativise", "relativisent"),
            Verbe("devenir plus sage", "devient plus sage", "deviennent plus sage"),
            Verbe("patienter", "patiente", "patientent"),
            Verbe("hiberner", "hiberne", "hibernent"),
            Verbe("dépérir", "dépérit", "dépérissent"),
            Verbe("applaudir", "applaudit", "applaudissent"),
            Verbe("comprendre", "comprend", "comprennent", poids=5),
            Verbe("danser", "danse", "dansent"),
            Verbe("reculer", "recule", "reculent"),
            Verbe("relativiser", "relativise", "relativis ent"),
            Verbe("observer", "observe", "observent"),
            Verbe("attendre", "attend", "attendent"),
            Verbe("méditer", "médite", "méditent"),
            Verbe("persévérer", "persévère", "persévèrent"),
            Verbe("perdre patience", "perd patience", "perdent patience"),
            Verbe("agir", "agit", "agissent"),
            Verbe("vagabonder", "vagabonde", "vagabondent"),
            Verbe("prendre du recul", "prend du recul", "prennent du recul"),
            Verbe("endurer les souffrances", "endure les souffrances", "endurent les souffrances"),
            Verbe("s'envoler dans le ciel", "s'envole dans le ciel", "s'envolent dans le ciel"),
            ]

    def get_and_format(self, ctr=None, type="singulier"):
        return [self.get_one(ctr).f(type=type), ]


# Define verbs, either transitive or not, with a complement if needed
class VerbesComplements(Mots):

    def __init__(self):
        self.mot_verbes_transitifs = VerbesTransitifs().mots
        self.mot_verbes_intransitifs = VerbesIntransitifs().mots
        self.mots = self.mot_verbes_transitifs + self.mot_verbes_intransitifs

    def get_and_format(self, ctr=None, type_v="singulier", nombre_compl="singulier", article_compl="defini"):
        if ctr is None:
            v = self.get_one(ctr_fct=lambda v: v.ctr_sujet is None)  # no pre constraint ('Sujet' is unknown!)
        else:
            v = self.get_one(ctr_fct=lambda v: v.ctr_sujet is None and ctr(v))  # compose constraints

        if v in self.mot_verbes_transitifs:  # care, word comparison works only because it's the same instance
            compl_l = SujetsQualifies().get_and_format(ctr_sujet=v.ctr_compl, nombre=nombre_compl,
                                                       article=article_compl)
            return [v.f(type=type_v), *compl_l]
        return [v.f(type=type_v)]


# Same as VerbesComplements but with a SujetsQualififies
class SujetsQualVerbesComplements(Mots):

    def __init__(self):
        self.mots_verbes_transitifs = VerbesTransitifs().mots
        self.mots_verbes_intransitifs = VerbesIntransitifs().mots
        self.mots = self.mots_verbes_transitifs + self.mots_verbes_intransitifs

    def get_and_format(self, ctr_v=None, type_vs="singulier", article_s="defini",
                       nombre_compl="singulier", article_compl="defini"):
        v = self.get_one(ctr_fct=ctr_v)
        s_l = SujetsQualifies().get_and_format(ctr_sujet=v.ctr_sujet, article=article_s, nombre=type_vs)

        if v in self.mots_verbes_transitifs:  # care, word comparison works only because it's the same instance
            compl_l = SujetsQualifies().get_and_format(ctr_sujet=v.ctr_compl, nombre=nombre_compl,
                                                       article=article_compl)
            return [*s_l, v.f(type=type_vs), *compl_l]
        return [*s_l, v.f(type=type_vs)]
