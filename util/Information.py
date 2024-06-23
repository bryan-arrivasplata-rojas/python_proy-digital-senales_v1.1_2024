from util.Graficas import forma_onda,spectrograma,butterworth,fir,rainbow_filter,hot_filter,sine_cosine_wave_filter
from util.Utilities import get_img_data

def generate_images(file_path):
    return {
        'waveform_img': get_img_data(forma_onda(file_path)),
        'spectrogram_img': get_img_data(spectrograma(file_path)),
        'butterworth_img': get_img_data(butterworth(file_path)),
        'fir_img_low': get_img_data(fir(file_path, 'low')),
        'fir_img_high': get_img_data(fir(file_path, 'high')),
        'fir_img_band': get_img_data(fir(file_path, 'band')),
        'rainbow_img': get_img_data(rainbow_filter(file_path)),
        'hot_img': get_img_data(hot_filter(file_path)),
        'sine_img': get_img_data(sine_cosine_wave_filter(file_path, 'sine')),
        'cosine_img': get_img_data(sine_cosine_wave_filter(file_path, 'cosine'))
    }