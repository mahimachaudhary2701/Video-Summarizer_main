from flask import Flask, request, redirect, url_for, render_template, flash, send_file
import os
from werkzeug.utils import secure_filename
from models import basic
import json

UPLOAD_FOLDER = 'static/video/input/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500*1024*1024  # upload limit 500MB
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numbers_array = request.form.get('numbers')
        numbers_array = json.loads(numbers_array)

        # Get the uploaded video file
        video_file = request.files['video']

        # Save the video file to the uploads folder
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
        video_file.save(video_path)

        # model 
        basic.main(video_path, numbers_array)
    
        return redirect(url_for('final', filename=video_file.filename)) #Problem
    return render_template('index.html')


@app.route('/final/<filename>')
def final(filename):
    return render_template('video-out.html', filename=filename)


@app.route('/download')
def download():
    return send_file('static/video/output/output.mp4', as_attachment=True, attachment_filename='processed-video.mp4', cache_timeout=0)



if __name__ == '__main__':
    app.run(debug=True)
