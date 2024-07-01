from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# 假设/content目录下的图片已经被压缩到1MB以下
CONTENT_DIR = '/content'

@app.route('/')
def index():
    files = os.listdir(CONTENT_DIR)
    images = f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    return render_template('/content/sum_app/templates/sum.html', images=images)

@app.route('/content/<filename>')
def serve_image(filename):
    return send_from_directory(CONTENT_DIR, filename)

if __name__ == '__main__':
    app.run(port=5670)
