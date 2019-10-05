import numpy as np

from proverbes_chinois._mot import formate_proverbe
from proverbes_chinois.proverbes import ProverbesVeriteGenerale, ProverbesConceptRedefini, ProverbesMomentAction, genere_random_proverbe

if __name__ == "__main__":
    np.random.seed(4)

    # n = 100
    # proverbes_verites_generales = [formate_proverbe(ProverbesVeriteGenerale().get_and_format()) for i in range(n)]
    # proverbes_concept_redefini = [formate_proverbe(ProverbesConceptRedefini().get_and_format()) for i in range(n)]
    # proverbes_moment_action = [formate_proverbe(ProverbesMomentAction().get_and_format()) for i in range(n)]
    #
    # print(proverbes_moment_action)

    for i in range(30):
        print(genere_random_proverbe())


