# Algorithmes d'investissement AlgoInvest&Trade
[![Python](https://badgen.net/badge/Python/3.8/blue)](https://www.python.org/)
[![Pipenv](https://badgen.net/badge/Pipenv/11.9/blue)](https://pypi.org/project/pipenv/)

## Description
Ce programme permet d'effectuer une sélection d'actions ayant le meilleur rendemment en fonction d'un budget.

Les données initiales sont dans ```datasets/```, les résultats obtenus s'affichent dans ```results/```.

Deux algorithmes distincts permettent d'effectuer la sélection d'actions :

- ```bruteforce.py``` qui effectue la meilleure sélection possible sur un petit set de données, au détriment du temps d'exécution.
- ```optimized.py``` qui effectue une sélection en optimisant au mieux le temps d'exécution. La sélection est effectuée sur chaque set de données présent.

## Installation
Ce projet utilise l'environnement virtuel pipenv.
```bash
pip3 install pipenv # Si pipenv n'est pas encore installé
```
On récupère le code depuis Github :
```bash
git clone https://github.com/rducrot/algo
```

Depuis le dossier du programme :
```bash
pipenv install # Installer les dépendances du projet
pipenv shell # Activer l'environnement virtuel
```
*Si la commande ```pipenv install``` retourne une erreur, s'assurer de bien utiliser la version 3.8 de Python et que le paquet ```python3.8-distutils``` est bien installé.* 

## Exécution

Depuis l'environnement virtuel, exécuter chacun des algorithmes :
```bash
python3 bruteforce.py
```

```bash
python3 optimized.py
```