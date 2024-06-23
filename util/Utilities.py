import io
import base64
import numpy as np

def apply_filter(audio):
    # Aplicar un filtro de suavizado (media móvil) al audio
    window_size = 100  # Tamaño de la ventana para la media móvil
    filtered_audio = np.convolve(audio, np.ones(window_size) / window_size, mode='same')
    return filtered_audio

def get_img_data(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode('utf-8')
    return img_data

