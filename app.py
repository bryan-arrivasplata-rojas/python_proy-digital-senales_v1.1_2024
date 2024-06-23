import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pyngrok import ngrok
import ssl
from util.Information import generate_images
load_dotenv()


ssl._create_default_https_context = ssl._create_unverified_context
ngrok.set_auth_token(os.getenv('SECRET_KEY_NGROK'))

# Variables que controlan la visibilidad y la información de los nombres
show_info = True
c_name = "C_NAME"
p_names = ["P_NAME"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        file_path = 'static/sound/audio.mp3'
        images = generate_images(file_path)
        return render_template('index.html',**images, show_info=show_info, c_name=c_name, p_names=p_names)
    if request.method == 'POST':
        audio_file = request.files['audio']
        audio_path = 'static/sound/temp_audio.mp3'
        audio_file.save(audio_path)
        images = generate_images(audio_path)
        #os.remove(audio_path)
        return jsonify(images)
        

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    # Obtener la URL pública generada por Ngrok
    public_url_str = str(public_url)
    print('URL pública de Ngrok:', public_url_str)
    # Run Flask application
    app.run()
