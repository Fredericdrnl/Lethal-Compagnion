<p  align="center">
    <img src = "https://imgs.search.brave.com/jDGyY8sdA9IxjuWF_geaKx-KLM-caxOKqkNuiDZJlIY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS5qZXV4dmlkZW8u/Y29tL21lZGlhcy1z/bS8xNzAxMTAvMTcw/MTA5ODk3OC0yNzE1/LWphcXVldHRlLWF2/YW50LmpwZw" title = "lethal logo" alt = "lethal logo">
<p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/Fredericdrnl/lethal-company-bot">
    <img src="https://img.shields.io/github/contributors/Fredericdrnl/lethal-company-bot">
</p>

> **Auteurs :** [Frédéric DOURNEL](https://github.com/Fredericdrnl), [Benjamin FOURNIER](https://github.com/Tabooret), [Tom VALLART](https://github.com/Tom6213)

# Développement du Bot Discord pour Lethal Company

# **Sommaire 📃**

- **1 Introduction**
    - 1.1 Le thème choisi
        - 1.1.1 Pourquoi ce sujet
        - 1.1.2 L'origine des données
    - 1.2 Travail en groupe 
    - 1.3 Prérequis
- **2 Développement et Implémentation**
    - 2.2 Planification du projet
    - 2.3 Rencontres de problèmes
- **3 Ressenti du Projet**
    - 3.1 Dans l'ensemble
        - 3.1.1 Ressenti de Benjamin
        - 3.1.2 Ressenti de Frédéric
        - 3.1.3 Ressenti de Tom
- **4 Conclusion**
- **5 Mode d'emploi**


## 1 - Introduction

Ce rapport vise à documenter le développement du bot Discord pour Lethal Company ainsi que notre ressenti tout au long du projet. Notre objectif était de créer un bot Discord fonctionnel pour faciliter la gestion des tâches et optimiser les parties de Lethal Company

Le but de ce Bot Discord est de référencer beaucoup d'information à propos des items, des monstres et des planètes du jeu. Nous avions comme contrainte de pouvoir conteneuriser les différentes parties de ce que fais le bot discord, c'est à dire l'API, la BDD et le bot discord.

L'archive de notre code est disponible sur GitHub.

### 1.1 - Le thème choisi

#### 1.1.1 - Pourquoi ce sujet

Nous avons choisi de faire un bot Discord sur Lethal Company car il s'agit de deux choses que nous apprécions et utilisons. Ce bot Discord pourrait aussi être utilisé par d'autres personnes si des informations en jeu sont nécessaire rapidement 

### 1.1.2 - L'origine des données

En ce qui concerne les données, nous avons écrit à la main toutes les données qui y sont présentes en utilisant les différents wiki qui sont à notre disposition sur Internet.
Ces données que nous avons récupérées comme le nom des monstres, des objets, leur coût... à été organisé dans différents tuples afin d'alimenter la base de données de notre bot Discord

## 1.2 - Travail en groupe

Pour ce projet, nous sommes en groupe de 3, Dournel Frédéric, Vallart Tom, Fournier Benjamin.
Nous avons utilisé différents types de communications et partage de données afin de rendre le projet à temps et fonctionnel comme Discord, GitHub, l'extension LiveShare de Visual StudioCode a été utilisé lors de la création de la base de données afin de la terminer au plus vite.
Nous avons beaucoup travaillé en présentiel lors des heures de travail prévu à cet effet.
Lors de ce projet chaque personne du groupe a pu effectuer une tâche 

### 1.3 - Prérequis

Presque tout le projet à été codée en **Python**. Nous avons utilisée la bibliothèque **Discord.py** pour créer le bot, **Flask** pour créer les routes API, **Requests** pour créer des requêtes API et **Psycogs2** pour intéragir avec la base de donnée qui par ailleur est une BDD **Postgresql**.

> Toutes les bibliothèques utilisée sont référencées dans le fichier requirements.py avec les versions.

<div align="center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"width="110" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg"width="110"/>
</div>


## 2 - Développement et Implémentation

### 2.1 - Planification du projet

Le projet a débuté par une phase de planification détaillée, au cours de laquelle nous avons défini les fonctionnalités principales du bot, donner les différentes taches à chacun. Nous avons utilisé principalement Python et la bibliothèque Discord.py pour le développement, en nous assurant d'utiliser des pratiques de codage propres et d'optimiser les performances du bot.

### 2.2 - Rencontres de problèmes

Le processus de développement s'est globalement bien déroulé. Cependant, nous avons rencontré quelques obstacles techniques, notamment des problèmes de latence et des erreurs de connexion avec l'API Discord, le problème d'API venait principalement du manque de connaissance sur la création d'une API, ce fut notre première création d'API, ces problèmes ont retardé légèrement notre progression.

## 3 - Ressenti du Projet

### 3.1 - Dans l'ensemble

Le projet que nous avons choisi, nous correspondait, il s'agissait pour nous de quelque chose que nous voulons réussir.
Le manque de connaissance sur certaines méthodes concernant le développement du bot Discord ou l'utilisation de Docker a parfois ralenti notre travail mais au vu de notre projet nous voulons tout de même le terminer. 

Nous avons également rencontré des problèmes imprévus qui ont mis à l'épreuve notre patience et nos compétences techniques. Les périodes où nous avons un problème que personne arrive à corriger pouvait mettre un certain frein à l'avancée du projet.

#### 3.1.1 - Ressenti de Benjamin

Personnellement, le projet de base était un bot Discord quelque chose que je n'ai jamais fait, j'ai du apprendre 2,3 choses auprès de Frédéric qui connaissait un peu plus le sujet, j'ai appris plusieurs façon de travailler sur GitHub avec la création de branches et le suivi d'une convention de commit. Concernant la motivation, il s'agissait d'un jeu que j'ai joué et quelque chose qui pourrait être utile j'ai donc voulu réussir et terminer ce projet.

#### 3.1.2 - Ressenti de Frédéric

#### 3.1.3 - Ressenti de Tom

N'ayant fait qu'un bot discord auparavant, avec des fonctionnalités basiques, ce projet était assez nouveau pour moi. J'ai un peu géré le routage puis je me suis concentré sur la BDD et la conteneurisation. Le mode de fonctionnement avec Github est quelque chose que je ne fais pas si souvent que ça et tout n'est pas encore tout à fait naturel et compréhensible pour moi. Cependant je trouve que ça rend le projet plus simple à gérer et ça nous permet de collaborer plus facilement.

## 4 - Conclusion

En fin de compte, malgré les difficultés rencontrées, je suis fier du travail accompli sur le bot Discord pour Lethal Company. Nous avons réussi à livrer un produit **fonctionnel** et qui nous plaît à nous joueur de lethal company. Peut-être que ce bot sera utilisé par d'autres personnes si elle le souhaite avoir des détails rapidement en jeu

Bien sûr, il reste toujours des améliorations possibles et des fonctionnalités supplémentaires à envisager pour enrichir davantage le bot. 

## 5 - Mode d'emploi

Le bot que nous avons développé s'utilise à partir de Discord, les commandes peuvent être entrée dans un channel de discussion.
Le bot Discord permet avec une commande d'avoir les informations sur ce que l'on veut comme tous les monstres ou seulement un.

> Les paramètres sont les noms anglais et il y a des underscores au lieu des espaces.

`- !monsters ▶️ Montre tous les monstres avec une description.`

`- !monster [MonsterName] ▶️ Affiche toutes les informations à propos d'un monstre passé en paramètre.`<br>
    `-Par exemple : !monster forest_keeper`
    <div align="center">
    <img src = "https://imgs.search.brave.com/17C5XfA_3tgJcADNz_kq2SlhWNsfZpMaSu0aPEXk93I/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/cGNpbnZhc2lvbi5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MjMvMTEvTGV0aGFs/LUNvbXBhbnktRm9y/ZXN0LUtlZXBlci1G/ZWF0dXJlZC1JbWFn/ZS5qcGc_dz03NTAm/cmVzaXplPTEyMDAs/Njc1" title = "geant" alt = "geant" width = 200>
    </div>

`- !moons ▶️ Montre toutes les lunes avec leur difficulté.`

`- !moon [MoonName] ▶️ Affiche toutes les informations.`
    `-Par exemple : !moon 8-Titan `
    <div align="center">
    <img src = "https://imgs.search.brave.com/6Ri0nq_SU96qMnM0HXCwOjZFs4mLAH1rQ1Ypf96BFbY/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wcm9n/YW1lZ3VpZGVzLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/My8xMS9GZWF0dXJl/ZC1MZXRoYWwtQ29t/cGFueS1ob3ctdG8t/aGVhbC5qcGc_Zml0/PTkwMCw1MDY" title = "moons" alt = "moons" width = 200>
    </div>


`- !items ▶️ Montre tous les items avec une description.`

`- !item [ItemName] ▶️ Affiche toutes les informations à propos d'un objet.`
    `-Par exemple : !item V-Type_Engine`
    <div align="center">
    <img src = 'https://static.miraheze.org/lethalwiki/6/61/VType.png' title = "batterie" alt = "batterie" width = 150>
    </div>

`- !storeItems ▶️ Montre tous les items achetable dans la boutique avec une description.`

`- !storeItem [StoreItemName] ▶️ Affiche toutes les informations à propos d"un objet de la boutique passé en paramètre.`
    `-Par exemple : !storeItem boombox`
    <div align="center">
    <img src = "https://imgs.search.brave.com/WULsMc8Vquumbch-q4kgNFdEO4_z1Nnqv-BUizFb5S4/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vZ2FtZXJ0/YWd6ZXJvLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMy8x/MS9MZXRoYWwtQ29t/cGFueS1Cb29tYm94/LndlYnA_cmVzaXpl/PTEwMjQsNjgyJnNz/bD0x" title = "boombox" alt = "boombox" width = 200 >
    </div>
