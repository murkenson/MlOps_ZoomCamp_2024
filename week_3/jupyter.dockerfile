FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install jupyter

COPY . /app

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]