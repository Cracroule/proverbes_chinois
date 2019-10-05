from _contexte import all_articles, all_nombres, all_genres, all_voyelles


def ajoute_article(mot, genre="masculin", nombre="singulier", article="defini"):
    assert (nombre in all_nombres)
    assert (article in all_articles)
    assert (genre in all_genres)
    if (nombre, article, genre) == ("singulier", "defini", "masculin"):
        return ("l\'" + mot) if mot[0] in all_voyelles else ("le " + mot)
    if (nombre, article, genre) == ("singulier", "defini", "feminin"):
        return ("l\'" + mot) if mot[0] in all_voyelles else ("la " + mot)
    if (nombre, article, genre) == ("singulier", "indefini", "masculin"):
        return "un " + mot
    if (nombre, article, genre) == ("singulier", "indefini", "feminin"):
        return "une " + mot
    if (nombre, article, genre) == ("pluriel", "defini", "masculin"):
        return "les " + mot
    if (nombre, article, genre) == ("pluriel", "defini", "feminin"):
        return "les " + mot
    if (nombre, article, genre) == ("pluriel", "indefini", "masculin"):
        return "des " + mot
    if (nombre, article, genre) == ("pluriel", "indefini", "feminin"):
        return "des " + mot
    raise TypeError("Nope")
