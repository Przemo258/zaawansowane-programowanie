import uvicorn
import os
from fastapi import FastAPI, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from magazine.model import get_model, analise_image

app = FastAPI()
model = get_model()


@app.post('/')
async def root(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    return analise_image(file.file, model)


@app.post('/total')
async def total(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    count = analise_image(file.file, model)['total']
    return {'total': count}


@app.post('/time')
async def time(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    result = analise_image(file.file, model)
    elapsed = result['elapsed_time']
    description = result['description']
    return {'elapsed_time': elapsed, 'description': description}


@app.post('/boxes')
async def time(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    data = analise_image(file.file, model)['results']
    return data


def cleanup_files():
    # wchodzimy do folderu i usuwamy zdjęcie i folder w którym sie znajduje
    os.chdir('results/run')
    os.remove('image0.jpg')
    os.chdir('../')
    os.rmdir('run')
    os.chdir('../')


@app.post('/img')
async def img(file: UploadFile, background_tasks: BackgroundTasks):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")

    # po wyświetleniu zdjęcia zostanie ono usunięte
    background_tasks.add_task(cleanup_files)
    _ = analise_image(file.file, model, save_img=True)

    # zwracamy przeanalizowane zdjęcie
    response = FileResponse('results/run/image0.jpg')
    return response


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
