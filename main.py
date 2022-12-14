import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from magazine.model import get_model, get_results, save_analised

app = FastAPI()
model = get_model()


@app.post('/')
async def root(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    return get_results(file.file, model)


@app.post('/total')
async def total(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    count = get_results(file.file, model)['total']
    return {'total': count}


@app.post('/time')
async def time(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    result = get_results(file.file, model)
    elapsed = result['elapsed_time']
    description = result['description']
    return {'elapsed_time': elapsed, 'description': description}


@app.post('/boxes')
async def time(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")
    data = get_results(file.file, model)['results']
    return data


@app.post('/img')
async def img(file: UploadFile):
    # sprawdzamy czy to zdjęcie .jpg
    if file.content_type != "image/jpeg":
        raise HTTPException(400, detail="Invalid file type")

    file_path = save_analised(file.file, model)

    # zwracamy przeanalizowane zdjęcie
    return FileResponse(file_path)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
