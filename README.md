# Proverbes_chinois

Package to create random chinese proverbs (in French)
Developed in Python 3.6.0


## Prerequisites

You need:
- a python 3.6 virtualenv (should be ok with any python 3 env)


## Setup

- install requirements:
````
pip install -r requirements.txt
````

- install package:
````
pip install proverbes_chinois
````

## Use

````
import numpy as np
from proverbes_chinois.proverbes import genere_random_proverbe


if __name__ == "__main__":
    np.random.seed(4)
    for i in range(30):
        print(genere_random_proverbe())
        
Lorsque des oreilles combattent des mendiants à l'entrée du temple, un commandant éloquent danse
Le subconscient n'est pas la cause de celui qui contemple un professeur
Lorsque les idiots contemplent les éléphants, l'endoctrinement s'envole vers la camaraderie dans le calme
La peur met en valeur le paradigme du prisonnier qui torture le livre
Pour marchander avec les grains de riz il faut attendre
Il faut observer les sojas afin de contempler l'innocence
La malice dépasse des cochons malveillants qui torturent un papillon
La malice rend possible le sage qui devient plus sage
Dans l'objectif de contempler la feu d'artifice il vaut mieux reculer
Il est plus facile d'écouter au sommet de la colline avant de relativiser
Il est plus facile de se briser brutalement pour comprendre les drapeaux
Si le grand subconscient observe le paisible caillou, le bonheur effraie le sabre
Si des bananes carnivores écoutent des regrets malins, des pandas combattent des tigres
Le regret approuve celui qui dépérit
La connaissance est à l'image de celui qui médite
La reconnaissance ne se maitrise qu'en observant un papillon qui applaudit
Si le mal intelligent écoute, les pommes rouges sont mangées par les yeux sanguinaires
La sagesse ne s'apprend qu'avec un moine qui s'approche d'un garçon maudit
Le sage dit qu'il vaut mieux écouter l'amour empatique dans les champs avant de contempler la souris
Le destin n'est que le bonheur jaune qui s'attaque à la fierté
L'animosité n'ignore pas celui qui observe
Le regret n'est pas étranger à la réussite de celui qui contemple l'encre de chine
La joie met en valeur le paradigme des enfants qui surprennent le destin carnivore
Quand la lumière contemple le garçon brutalement, le garçon applaudit
Dans l'objectif de perdre patience le sage dit qu'il faut prendre du recul
La sagesse transcende ceux qui s'attaquent à un professeur
Avant de marchander avec les rats il vaut mieux admirer la courtisane
La lumière magnifie le petit périple qui surprend la malice
Le subconscient dépasse les vénérables serpents qui discutent avec le rat
L'animosité dépasse le petit regard qui patiente
````

