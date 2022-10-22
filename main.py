import os
import cv2
import numpy

from PIL import Image
from datetime import datetime
from selenium import webdriver
from flask import Flask, render_template, Response
from webdriver_manager.firefox import GeckoDriverManager



pixelGap = 79.29
width, height = (2160, 1080)



app = Flask(__name__)
pathTemp = os.environ['TEMP']

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://google.com")



def gen_frames():
    imOld = None

    while True:
        start_time = datetime.now()
        # Get screenshot of web selenium
        driver.save_screenshot(rf"{pathTemp}/screenshot.png")
        # Open image with PIL library
        im = Image.open(rf"{pathTemp}/screenshot.png")
        # If the last image is different compared to before last
        if imOld != im:
            imOld = im
            # Get size of screenshot
            w, h = im.size
            # Calculation of the points of the image to recover
            left = (w/2)-h/2
            top = 0
            right = (w/2)+h/2
            bottom = h
            # Recovery of images (right and left) according to the calculated points
            im1 = im.crop((left-pixelGap, top, right-pixelGap, bottom))
            im2 = im.crop((left+pixelGap, top, right+pixelGap, bottom))
            # Create a new empty image
            im3 = Image.new('RGB', (width, height))
            # Add left image on new image
            im1 = im1.resize((round(width/2), round(width/2)))
            im3.paste(im1, (0, 0))
            # Add right image on new image
            im2 = im2.resize((round(width/2), round(width/2)))
            im3.paste(im2, (round(width/2), 0))

        ret, buffer = cv2.imencode('.jpg', cv2.cvtColor(numpy.array(im3), cv2.COLOR_RGB2BGR))
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        end_time = datetime.now()
        print('\rExecution time: {}'.format(end_time - start_time), end="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return "OK"

@app.route('/live')
def live():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/map')
def googleMap():
    driver.get('https://www.google.fr/maps/@34.0454224,-118.2542243,775a,35y,39.22t/data=!3m1!1e3')
    input("Press enter to start JS remover...")
    driver.execute_script("""try {document.querySelector('div[id="assistive-chips"]').remove()} catch {};try {document.querySelector('div[id="omnibox-container"]').remove()} catch {};try {document.querySelector('div[id="vasquette"]').remove()} catch {};try {document.querySelector('div[class="app-viewcard-strip ZiieLd"]').remove()} catch {};try {document.querySelector('div[class="scene-footer-container Hk4XGb"]').remove()} catch {};try {document.querySelector('div[id="content-container"] div[id="scene"] div[id="watermark"]').remove()} catch {};""")
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=False)
