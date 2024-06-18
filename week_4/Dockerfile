FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install --upgrade pip
WORKDIR /app

COPY [ "requirements.txt", "requirements.txt" ]
RUN pip install -r requirements.txt


COPY [ "score.py", "score.py" ]
RUN chmod +x score.py