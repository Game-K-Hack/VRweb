<h1 align="center">
    WEB VR
</h1>

<p align="center">
  <a href="#Description">Description</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Paramètrage">Paramètrage</a> •
  <a href="#Demo">Demo</a> •
  <a href="#Fonctionnement">Fonctionnement</a>
</p>


## Description

Web VR va permettre de voir en réalité virtuel tous ce que l'on desire sur internet: Vidéo, Google Earth, Google map, image, ... Cette algorithme Python va prendre une capture d'écran du navigateur afin de créer un décalage dans l'image pour pouvoir avoir cette dernière en VR.

## Installation

Pour que ce script fonctionne il faut avoir Python en version 3.9 *(ou une version supérieur)* et avoir installé les librairie suivante:

| Nom | Commande d'installation |
| ------ | ------ |
| Pillow | pip install Pillow |
| Numpy | pip install numpy |
| Selenium | pip install selenium |
| OpenCV | pip install opencv-python |
| Flask | pip install Flask

## Paramètrage

Pour paramètrer correctement la VR par rapport à l'appareil utilisé, il faut récuprer dans le téléphone la hauteur et la largeur de l'écran en pixel. Pour cela il faut ce rendre dans les paramètre de ce dernier puis chercher la rubrique **À propos du téléphone** et trouver la résolution. Une cette étape terminé il faut modifier dans le script les variable `width` et `height` avec vos propres valeurs. Dans notre cas la résolution du téléphone était 2160 x 1080 donc les variables était `width, height = (2160, 1080)`.
<br>
Pour que le streaming VR fonctionne, il faut que l'ordinateur soit sur le même réseaux que le téléphone. Pour pouvoir voir la page web, il faut mettre l'ip de l'ordinateur dans le navigateur du téléphone.

## Demo

Pour la démo, l'ordinateur à l'ip local suivante: `192.168.1.31`

### Google Map

Pour accéder à Google map en VR il faut se rendre sur l'URL `http://192.168.1.31:5000/map` et attendre que la page Google map soit entièrement chargé puis appuyer sur **Entré** dans le terminal et enfin aller sur l'URL `http://192.168.1.31:5000/live` pour voir en VR.

![](https://cdn.discordapp.com/attachments/1033521416726913125/1033521469424156672/Clipboard01.png)
*Google Map, Los Angeles, 2022*

### Google Earth

![](https://cdn.discordapp.com/attachments/1033521416726913125/1033521469868736623/Clipboard02.png)
*Google Earth, Terre*

![](https://cdn.discordapp.com/attachments/1033521416726913125/1033521470309159002/Clipboard03.png)
*Google Earth, Los Angeles, 03/01/2020*

## Fonctionnement

Ce programme créer un décalage dans l'image. Sur l'image suivante qui est une capture d'écran de Google Earth, on peut voir en rouge l'image pour l'oeil gauche, et en bleu l'image pour l'oeil droit.

![](https://cdn.discordapp.com/attachments/1033521416726913125/1033525988602150972/capture.png)
*Google Earth, Los Angeles, 03/01/2020*

