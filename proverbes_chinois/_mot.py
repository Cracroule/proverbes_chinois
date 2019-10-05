from numpy.random import choice

from _contexte import all_voyelles


def formate_proverbe(liste_de_mots):
    remplace_voyelles = dict(zip([" de " + v for v in all_voyelles], [" d'" + v for v in all_voyelles]))
    remplace_all = {" de les": " des",
                    " de des": " des",
                    " de le": " du",
                    " de un": " d'un",
                    "à le": "au",
                    "à les": "aux",
                    " , ": ", ",
                    **remplace_voyelles}
    proverbe = " ".join(liste_de_mots)
    for k, v in remplace_all.items():
        proverbe = proverbe.replace(k, v)
    return proverbe.capitalize()


# any word defined in the project should inherit from Mot.
class Mot:

    # minimal attributes
    tags = list()  # tags are additional information about Mot, can be used in constraint filtering
    poids = 10  # default weight is 10 (bigger means more likely)

    # transform word into its final form
    def f(self):
        raise NotImplementedError("To be implemented in child class")


# any group of words defined in the project should inherit from Mots
class Mots:

    mots = []

    # select all instances of the group compliant with constraint
    def get_all(self, ctr_fct=None):
        mots_possibles = [m for m in self.mots if ctr_fct(m)] if ctr_fct is not None else self.mots
        assert (len(mots_possibles))
        return mots_possibles

    # select one instance of the group compliant with constraint
    def get_one(self, ctr_fct=None):
        mots_possibles = self.get_all(ctr_fct=ctr_fct)
        poids = [m.poids for m in mots_possibles]
        total_poids = float(sum(poids))
        probas = [p/total_poids for p in poids]
        return choice(mots_possibles, 1, p=probas)[0]

    # select one instance compliant with the group, format its components, return as a list
    def get_and_format(self, ctr=None):
        raise NotImplementedError("To be implemented in child class")

    def f(self):
        return str(self)


# basically the same as 'Mots', but should create a consistent sentence on its own
class Phrases(Mots):

    poids_phrase = 10

    # select one instance compliant with the group, format its components, return as a list
    def get_and_format(self, ctr=None):
        raise NotImplementedError("To be implemented in child class")
