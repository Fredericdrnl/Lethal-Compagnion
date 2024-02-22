<p  align="center">
    <img src = "https://imgs.search.brave.com/jDGyY8sdA9IxjuWF_geaKx-KLM-caxOKqkNuiDZJlIY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS5qZXV4dmlkZW8u/Y29tL21lZGlhcy1z/bS8xNzAxMTAvMTcw/MTA5ODk3OC0yNzE1/LWphcXVldHRlLWF2/YW50LmpwZw" title = "lethal logo" alt = "lethal logo">
<p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/Fredericdrnl/lethal-company-bot">
    <img src="https://img.shields.io/github/contributors/Fredericdrnl/lethal-company-bot">
</p>

> **Auteurs :** [Frédéric DOURNEL](https://github.com/Fredericdrnl), [Benjamin FOURNIER](https://github.com/Tabooret), [Tom VALLART](https://github.com/Tom6213)

### **1 Présentation du projet**

Ce projet représente la création d'un bot discord sur le jeu lethal company. Le but de ce jeu est de référencerer beaucoup d'information à propos des items, des monstres et des planètes du jeu. Nous avions comme contrainte de pouvoir conteneuriser les différentes parties de ce que fais le bot discord, c'est à dire l'API, la BDD et le bot discord.

### **2 Prérequis**

Presque tout le projet à été codée en **Python**. Nous avons utilisée la bibliothèque **Discord.py** pour créer le bot, **Flask** pour créer les routes API, **Requests** pour créer des requêtes API et **Psycogs2** pour intéragir avec la base de donnée qui par ailleur est une BDD **Postgresql**.

> Toutes les bibliothèques utilisée sont référencées dans le fichier requirements.py avec les versions.

<div align="center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"width="110" />
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg"width="110"/>
</div>

### **3 Commandes**
Commandes qui permet de :

> Les paramètres sont les noms anglais et il y a des underscores au lieu des espaces.

`- !monsters ▶️ Montre tous les monstres avec une description.`

`- !monster [MonsterName] ▶️ Affiche toutes les informations à propos d'un monstre passé en paramètre.`

`- !moons ▶️ Montre toutes les lunes avec leur difficulté.`

`- !moon [MoonName] ▶️ Affiche toutes les informations.`

`- !items ▶️ Montre tous les items avec une description.`

`- !item [ItemName] ▶️ Affiche toutes les informations à propos d'un objet.`

`- !storeItems ▶️ Montre tous les items achetable dans la boutique avec une description.`

`- !storeItem [StoreItemName] ▶️ Affiche toutes les informations à propos d"un objet de la boutique passé en paramètre.`


