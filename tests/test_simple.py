from proverbes_chinois._mot import formate_proverbe
from proverbes_chinois.sujet import Sujets, SujetsQualifies
from proverbes_chinois.adjectif import AdjectifsPre, AdjectifsPost
from proverbes_chinois.verbe import VerbesTransitifs, VerbesIntransitifs, VerbesComplements, SujetsQualVerbesComplements
from proverbes_chinois.complement import Complement, ComplementsDefiniConcept, ComplementsMoment, ComplementsObjectif, ComplementsVeriteGenerale, ComplementsContextes

from proverbes_chinois.contrainte import contrainte_genre, contrainte_nombre, contrainte_possede_tag
#
# from proverbes_chinois.contrainte import Contrainte

import numpy as np


if __name__ == "__main__":
    np.random.seed(42)

    n = 100
    sujets = [formate_proverbe(Sujets().get_and_format()) for i in range(n)]
    adjectifs_pre = [formate_proverbe(AdjectifsPre().get_and_format()) for i in range(n)]
    adjectifs_post = [formate_proverbe(AdjectifsPost().get_and_format()) for i in range(n)]
    sujets_qualifies = [formate_proverbe(SujetsQualifies().get_and_format()) for i in range(n)]
    verbes_intransitifs = [formate_proverbe(VerbesIntransitifs().get_and_format()) for i in range(n)]
    verbes_transitifs = [formate_proverbe(VerbesTransitifs().get_and_format()) for i in range(n)]
    verbes_complements = [formate_proverbe(VerbesComplements().get_and_format()) for i in range(n)]
    sujetsq_verbes_complements = [formate_proverbe(SujetsQualVerbesComplements().get_and_format()) for i in range(n)]

    print(sujetsq_verbes_complements)

    s = Sujets().get_all(ctr_fct=contrainte_genre("masculin"))
    s = Sujets().get_all(ctr_fct=contrainte_possede_tag("comestible"))
    print(s)
