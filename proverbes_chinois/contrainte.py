# below functions define constraints that can be applied to select relevant words among a group
# the selection can be made on the tag, or on any other attribute (add constraint generator to handle it)


def contrainte_possede_tag(tag):
    return lambda mot: tag in mot.tags


def contrainte_evite_tag(tag):
    return lambda mot: tag not in mot.tags


def contrainte_genre(genre):
    return lambda mot: genre == mot.genre


def contrainte_nombre(nombre):
    return lambda mot: nombre == mot.nombre


def compose_contraintes(*args):
    return lambda mot: all([ctr(mot) for ctr in args if ctr is not None])


# class Contrainte():
#
#     def __init__(self, type, key):
#         self.type = type
#         self.key = key
#         if type == "tag":
#             self.fct = lambda mot: key in mot.tags
#         elif type == "genre":
#             self.fct = lambda mot: key == mot.genre
#         elif type == "nombre":
#             self.fct = lambda mot: key == mot.nombre
#         else:
#             raise TypeError("contraint_type must be in ('tag', 'genre', 'nombre')")
#
#     def __repr__(self):
#         return f"Contrainte: {self.type} doit etre {self.key}"
#
#     def __str__(self):
#         return f"Contrainte: {self.type} doit etre {self.key}"
#
#     def __call__(self, *args, **kwargs):
#         self.fct(*args, **kwargs)


