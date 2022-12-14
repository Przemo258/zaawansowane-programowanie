import torch
import cv2
import time
import uuid


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


def analise_image(image, model):
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

    # przekonwertowanie wyników na pandasowy dataframe
    df = model_results.pandas().xyxy[0]

    return df, img, elapsed_time, model_results


def get_results(img, model):
    # wykonanie analizy
    df, _, elapsed_time, model_results = analise_image(img, model)
    # jako że model wykrywa tylko ludzi liczba wierszy = liczba ludzi
    count = df.shape[0]
    # przekonwertowanie wyników na json
    results_json = df.to_json()

    results = {'total': count,
               'results': results_json,
               'elapsed_time': elapsed_time,
               'description': str(model_results)}

    return results


def save_analised(image, model):
    # wykonanie analizy
    results = analise_image(image, model)
    df, img = results[0], results[1]

    color = [0, 0, 255]

    # narysowanie prostokątów na zdjęciu dla każdej wykrytej osoby
    for index, row in df.iterrows():
        xmin, xmax = int(row['xmin']), int(row['xmax'])
        ymin, ymax = int(row['ymin']), int(row['ymax'])

        img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 20)

    # zapisanie pliku z unikalną nazwą
    file_path = f'results/{uuid.uuid4()}.jpg'
    cv2.imwrite(file_path, img)

    return file_path
