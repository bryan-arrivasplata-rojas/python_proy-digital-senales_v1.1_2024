import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from pydub import AudioSegment
from pydub.utils import get_array_type
from util.Utilities import apply_filter

def forma_onda(file_path):
    audio, sr = librosa.load(file_path)
    waveform_fig = plt.figure(figsize=(12, 4))
    librosa.display.waveshow(audio, sr=sr, color='blue')
    plt.title('Forma de onda')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (unidad digital)')
    return waveform_fig
    
def spectrograma(file_path):
    audio, sr = librosa.load(file_path)
    D = librosa.stft(audio)
    spectrogram_fig = plt.figure(figsize=(12, 4))
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    return spectrogram_fig

def butterworth(file_path, cutoff_freq=1000, order=4, filter_type='low'):
    audio, sr = librosa.load(file_path)
    
    # Diseñar el filtro Butterworth
    nyquist = 0.5 * sr
    normal_cutoff = cutoff_freq / nyquist
    b, a = signal.butter(order, normal_cutoff, btype=filter_type, analog=False)
    
    # Aplicar el filtro
    filtered_audio = signal.filtfilt(b, a, audio)
    
    # Generar la gráfica de la forma de onda filtrada
    butterworth_fig = plt.figure(figsize=(12, 4))
    librosa.display.waveshow(filtered_audio, sr=sr, color='red')
    plt.title('Forma de onda filtrada (Butterworth)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (unidad digital)')
    
    return butterworth_fig

def fir(file_path, filter_type, cutoff_freq=1000, numtaps=101):
    # Cargar el audio
    audio, sr = librosa.load(file_path)
    
    # Diseñar el filtro FIR
    nyquist = 0.5 * sr
    normal_cutoff = cutoff_freq / nyquist
    if filter_type == 'low':
        fir_coeff = signal.firwin(numtaps, normal_cutoff, pass_zero='lowpass')
    elif filter_type == 'high':
        fir_coeff = signal.firwin(numtaps, normal_cutoff, pass_zero='highpass')
    elif filter_type == 'band':
        # Aquí normal_cutoff debe ser una tupla con dos elementos
        low_cutoff_freq = 500  # Frecuencia de corte inferior en Hz
        high_cutoff_freq = 1500  # Frecuencia de corte superior en Hz
        normal_cutoff = (low_cutoff_freq / nyquist, high_cutoff_freq / nyquist)
        fir_coeff = signal.firwin(numtaps, normal_cutoff, pass_zero='bandpass')
    else:
        raise ValueError("filter_type must be 'low', 'high', or 'band'")
    
    # Aplicar el filtro
    filtered_audio = signal.lfilter(fir_coeff, 1.0, audio)
    
    # Generar la gráfica de la forma de onda filtrada
    fir_fig = plt.figure(figsize=(12, 4))
    librosa.display.waveshow(filtered_audio, sr=sr, color='green')
    plt.title('Forma de onda filtrada (FIR) - '+filter_type)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (unidad digital)')
    
    return fir_fig

def rainbow_filter(file_path):
    # Cargar el audio
    audio, sr = librosa.load(file_path)
    
    # Calcular el espectrograma del audio
    D = np.abs(librosa.stft(audio))
    
    # Crear una nueva figura y un eje
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Aplicar un mapa de colores de arco iris al espectrograma
    rainbow_spec = librosa.display.specshow(D, sr=sr, cmap='rainbow', ax=ax)
    
    # Configurar el título y las etiquetas de los ejes
    ax.set_title('Espectrograma con filtro de arco iris')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Frecuencia (Hz)')

    return fig

def hot_filter(file_path):
    # Cargar el audio
    audio, sr = librosa.load(file_path)
    
    # Calcular el espectrograma del audio
    D = np.abs(librosa.stft(audio))
    
    # Crear una nueva figura y un eje
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Aplicar un mapa de colores "hot" al espectrograma
    hot_spec = librosa.display.specshow(D, sr=sr, cmap='hot', ax=ax)
    
    # Configurar el título y las etiquetas de los ejes
    ax.set_title('Espectrograma con filtro "hot"')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Frecuencia (Hz)')
    
    return fig

def sine_cosine_wave_filter(file_path, modulation_type, modulation_frequency=5):
    # Cargar el audio
    audio, sr = librosa.load(file_path)
    
    # Crear una onda moduladora seno o coseno
    t = np.arange(len(audio)) / sr
    if modulation_type == 'sine':
        modulating_wave = np.sin(2 * np.pi * modulation_frequency * t)
    elif modulation_type == 'cosine':
        modulating_wave = np.cos(2 * np.pi * modulation_frequency * t)
    else:
        raise ValueError("modulation_type must be 'sine' or 'cosine'")
    
    # Aplicar modulación de amplitud
    modulated_audio = audio * modulating_wave
    
    # Graficar la forma de onda original y la modulada
    fig = plt.figure(figsize=(12, 6))
    plt.plot(t, audio, label='Original')
    plt.plot(t, modulated_audio, label='Modulada')
    plt.title('Forma de onda con modulación de amplitud ' + modulation_type)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    
    return plt