FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip --root-user-action=ignore && \
    pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

CMD ['uvicorn', 'app.main:app', '--host', '0.0.0.0','--port', '8000']