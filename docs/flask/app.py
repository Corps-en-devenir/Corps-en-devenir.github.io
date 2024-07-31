from flask import Flask, render_template
import os
from pathlib import Path
import random

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = Path(__file__).parent.parent / 'images' / 'photos'
    images = [img for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    selected_images = random.sample(images, 4) if len(images) >= 4 else images
    return render_template('index.html', images=selected_images)

if __name__ == '__main__':
    app.run(debug=True)

