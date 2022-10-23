<h1 align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/WebVR.png" width=75 />
    <br>
    WEB VR
</h1>

<p align="center">
  <a href="#Description">Description</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Paramétrage">Paramétrage</a> •
  <a href="#Demo">Demo</a> •
  <a href="#Fonctionnement">Fonctionnement</a>
</p>

<br>
<br>
<br>

## Description

Web VR va permettre de voir en réalité virtuel tous ce que l'ont desire sur internet: Vidéo, Google Earth, Google map, image, ... Cet algorithme Python va prendre une capture d'écran du navigateur afin de créer un décalage dans l'image pour pouvoir avoir cette dernière en VR.

## Installation

Pour que ce script fonctionne il faut avoir Python en version 3.9 *(ou une version supérieure)* et avoir installé les librairies suivantes:

| Nom | Commande d'installation |
| ------ | ------ |
| Pillow | pip install Pillow |
| Numpy | pip install numpy |
| Selenium | pip install selenium |
| OpenCV | pip install opencv-python |
| Flask | pip install Flask

## Paramétrage

Pour paramétrer correctement la VR par rapport à l'appareil utilisé, il faut récupérer dans le téléphone la hauteur et la largeur de l'écran en pixel. Pour cela il faut se rendre dans les paramètres de ce dernier puis chercher la rubrique **à propos du téléphone** et trouver la résolution. Une fois cette étape terminée il faut modifier dans le script les variables `width` et `height` avec vos propres valeurs. Dans notre cas la résolution du téléphone étaient 2160 x 1080 donc les variables était `width, height = (2160, 1080)`.
<br>
Pour que le streaming VR fonctionne, il faut que l'ordinateur soit sur le même réseau que le téléphone. Pour pouvoir voir la page web, il faut mettre l'IP de l'ordinateur dans le navigateur du téléphone.

## Demo

Pour la démo, l'ordinateur a l'IP local suivante: `192.168.1.31`

### Google Map

Pour accéder à Google map en VR il faut se rendre sur l'URL `http://192.168.1.31:5000/map` et attendre que la page Google map soit entièrement chargé puis appuyer sur **Entré** dans le terminal et enfin aller sur l'URL `http://192.168.1.31:5000/live` pour voir en VR.

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard01.png)
*Google Map, Los Angeles, 2022*

### Google Earth

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard02.png)
*Google Earth, Terre*

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard03.png)
*Google Earth, Los Angeles, 03/01/2020*

## Fonctionnement

Les casques de réalité virtuelle se basent sur notre physiologie, en présentant des images légèrement décalées d'un œil à l'autre afin de reproduire une vision binoculaire (dans la réalité, nos yeux captent en effet deux images différentes que notre cerveau combine afin de créer une image unique tridimensionnelle). Ce programme conçoit donc deux images légèrement décalées l'une de l'autre à partir d'une seule et même image, afin que le cerveau puisse combiner ces dernières pour lui faire croire une réalité en 3 dimensions. Sur l'image suivante qui est une capture d'écran de Google Earth, on peut voir en rouge l'image pour l'oeil gauche, et en bleu l'image pour l'oeil droit.

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/screenshot.png)
*Google Earth, Los Angeles, 03/01/2020*
