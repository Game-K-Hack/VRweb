<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/WebVR.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.2" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=unstable&color=red" alt="Version - Unstable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
  <a href="https://www.paypal.com/paypalme/gamekdonate">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate" />
  </a>
</div>

<h4 align="center">This program makes internet in virtual reality</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#installation">Installation</a> •
  <a href="#setting">Setting</a> •
  <a href="#demo">Demo</a> •
  <a href="#functioning">Functioning</a>
</p>

<br>
<br>

## Description

Web VR will allow you to see in virtual reality everything you want on the internet: Video, Google Earth, Google map, image, ... This Python algorithm will take a screenshot of the browser in order to create a shift in the image to be able to have the latter in VR.

## Installation

For this script to work, you must have Python in version 3.9 *(or a higher version)* and have installed the following libraries:

| Name | Installation command |
| ------ | ------ |
| Pillow | `pip install Pillow` |
| Numpy | `pip install numpy` |
| Selenium | `pip install selenium` |
| OpenCV | `pip install opencv-python` |
| Flask | `pip install Flask` |

## Setting

To correctly configure the VR in relation to the device used, the height and width of the screen in pixels must be retrieved from the phone. To do this, you have to go to the settings of the latter then look for the section **about the phone** and find the resolution. Once this step is complete, modify the `width` and `height` variables in the script with your own values. In our case the resolution of the phone was 2160 x 1080 so the variables were `width, height = (2160, 1080)`.
<br>
For VR streaming to work, the computer must be on the same network as the phone. To be able to see the web page, you must put the computer's IP in the phone's browser.

## Demo

For the demo, the computer has the following local IP: `192.168.1.31`

### Google Map

To access Google map in VR you have to go to the URL `http://192.168.1.31:5000/map` and wait for the Google map page to be fully loaded then press **Enter** in the terminal and finally go to the URL `http://192.168.1.31:5000/live` to see in VR.

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard01.png)
*Google Map, Los Angeles, 2022*

### Google Earth

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard02.png)
*Google Earth, Terre*

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/Clipboard03.png)
*Google Earth, Los Angeles, 03/01/2020*

## Functioning

Virtual reality headsets are based on our physiology, presenting images slightly shifted from one eye to the other in order to reproduce binocular vision (in reality, our eyes indeed capture two different images that our brain combines in order to create a unique three-dimensional image). This program therefore designs two images slightly offset from each other from a single image, so that the brain can combine them to make it believe in a 3-dimensional reality. On the following image which is a screenshot of Google Earth, we can see in red the image for the left eye, and in blue the image for the right eye.

![](https://raw.githubusercontent.com/Game-K-Hack/VRweb/main/images/screenshot.png)
*Google Earth, Los Angeles, 03/01/2020*
