import torch
import cv2
import time


def get_model():
    # wybieramy gdzie ma pobrać model i wagi :X
    torch.hub.set_dir('magazine/')
    # wczytanie modelu bez wyświetlania dodatkowych informacji
    model = torch.hub.load('ultralytics/yolov5', 'yolov5x', verbose=False)
    # jak jest możliwość wykonać na gpu ale niepotrzebne
    # bo pytorch robi to automatycznie ale chce mieć 5
    if torch.cuda.is_available():
        model = model.cuda()
    # tylko osoby
    model.classes = [0]
    return model


def analise_image(image, model, save_img: bool = False):
    # wczytanie zdjęcia
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    # konwersja z BGR na RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # rozpoczęcie mierzenia czasu
    start = time.time()

    # wrzucenie zdjęcia do modelu
    model_results = model(rgb_img, size=640)

    # zakończenie mierzenia czasu
    end = time.time()

    elapsed_time = end - start

    # opcjonalne zapisanie zdjęcia do folderu (do podglądu)
    if save_img:
        model_results.save(save_dir='results/run')

    # przekonwertowanie wyników na pandasowy dataframe
    df = model_results.pandas().xyxy[0]
    # jako że model wykrywa tylko ludzi liczba wierszy = liczba ludzi
    count = df.shape[0]
    # przekonwertowanie wyników na json
    results_json = df.to_json()

    results = {'total': count,
               'results': results_json,
               'elapsed_time': elapsed_time,
               'description': str(model_results)}
    return results
