from numpy.random import choice

from _mot import Phrases, formate_proverbe
from _contexte import all_nombres
from proverbes_chinois.contrainte import contrainte_possede_tag, contrainte_genre, compose_contraintes
from proverbes_chinois.sujet import SujetsQualifies, Sujets
from proverbes_chinois.verbe import SujetsQualVerbesComplements, VerbesComplements
from proverbes_chinois.complement import ComplementsVeriteGenerale, ComplementsObjectif, ComplementsContextes, ComplementsDefiniConcept, ComplementsMoment


class ProverbesVeriteGenerale(Phrases):

    def __init__(self, poids_phrase=10):
        self.poids_phrase = poids_phrase

    def get_and_format(self, nombre_s1="singulier", article_s1="defini", nombre_s2="singulier",
                       article_s2="defini"):
        _VC = VerbesComplements()
        debut_l = ComplementsVeriteGenerale().get_and_format()
        verbes_l = _VC.get_and_format(type_v="infinitif", nombre_compl=nombre_s1, article_compl=article_s1)
        contexte_l = ComplementsContextes().get_and_format() if choice([True, False], 1, p=(0.3, 0.7))[0] else []
        obj_l = ComplementsObjectif().get_and_format()
        verbes_fin_l = _VC.get_and_format(type_v="infinitif", nombre_compl=nombre_s2, article_compl=article_s2)

        if choice([True, False], 1, p=(0.7, 0.3))[0]:
            return [*debut_l, *verbes_l, *contexte_l, *obj_l, *verbes_fin_l]
        else:
            return [*obj_l, *verbes_fin_l, *debut_l, *verbes_l, *contexte_l]


class ProverbesConceptRedefini(Phrases):

    def __init__(self, poids_phrase=10):
        self.poids_phrase = poids_phrase

    def get_and_format(self, nombre_s1="singulier", article_s1="defini", nombre_s2="singulier", article_s2="defini"):
        concept_l = Sujets().get_and_format(ctr=contrainte_possede_tag("concept"), nombre="singulier", article="defini")
        compl_l = ComplementsDefiniConcept().get_and_format()
        if choice([True, False], 1, p=(0.7, 0.3))[0]:  # take random 'sujet' ?
            sujet_l = SujetsQualifies().get_and_format(nombre=nombre_s1, article=article_s1)
        else:
            sujet_l = ["celui"] if nombre_s1 == "singulier" else ["ceux"]
        qui_l = ["qui"]
        action_l = VerbesComplements().get_and_format(type_v=nombre_s1, nombre_compl=nombre_s2, article_compl=article_s2)
        contexte_l = ComplementsContextes().get_and_format() if choice([True, False], 1, p=(0.15, 0.85))[0] else []

        return [*concept_l, *compl_l, *sujet_l, *qui_l, *action_l, *contexte_l]


class ProverbesMomentAction(Phrases):

    def __init__(self, poids_phrase=10):
        self.poids_phrase = poids_phrase

    def get_and_format(self, nombre_s1="singulier", article_s1="defini", nombre_s2="singulier", article_s2="defini"):
        action = SujetsQualVerbesComplements()
        moment_l = ComplementsMoment().get_and_format()
        action1_l = action.get_and_format(type_vs=nombre_s1, article_s=article_s1,
                                          nombre_compl=nombre_s1, article_compl=article_s1)
        transition_l = [',']
        action2_l = action.get_and_format(type_vs=nombre_s2, article_s=article_s2,
                                          nombre_compl=nombre_s2, article_compl=article_s2)
        if not choice([True, False], 1, p=(0.3, 0.7))[0]:  # add context ?
            return [*moment_l, *action1_l, *transition_l, *action2_l]
        else:
            contexte_l = ComplementsContextes().get_and_format()
            if choice([True, False], 1, p=(0.5, 0.5))[0]:  # where we place context ?
                return [*moment_l, *action1_l, *contexte_l, *transition_l, *action2_l]
            else:
                return [*moment_l, *action1_l, *transition_l, *action2_l, *contexte_l]


def genere_random_proverbe():
    p1 = ProverbesVeriteGenerale()
    p2 = ProverbesConceptRedefini()
    p3 = ProverbesMomentAction()

    poids_l = [p1.poids_phrase, p2.poids_phrase, p3.poids_phrase]
    poids_l = [p / sum(poids_l) for p in poids_l]

    nombre_s1 = choice(["singulier", "pluriel"], 1, p=(0.7, 0.3))[0]
    nombre_s2 = choice(["singulier", "pluriel"], 1, p=(0.7, 0.3))[0]
    article_s1 = choice(["defini", "indefini"], 1, p=(0.8, 0.2))[0]
    article_s2 = article_s1

    p = choice(["ProverbesVeriteGenerale", "ProverbesConceptRedefini", "ProverbesMomentAction"], 1, p=poids_l)[0]
    if p == "ProverbesVeriteGenerale":
        proverbe = formate_proverbe(p1.get_and_format(nombre_s1=nombre_s1, article_s1=article_s1,
                                                      nombre_s2=nombre_s2, article_s2=article_s2))
    elif p == "ProverbesConceptRedefini":
        proverbe = formate_proverbe(p2.get_and_format(nombre_s1=nombre_s1, article_s1=article_s1,
                                                      nombre_s2=nombre_s2, article_s2=article_s2))
    elif p == "ProverbesMomentAction":
        proverbe = formate_proverbe(p3.get_and_format(nombre_s1=nombre_s1, article_s1=article_s1,
                                                      nombre_s2=nombre_s2, article_s2=article_s2))
    else:
        raise Exception("flute de zut")

    return proverbe


