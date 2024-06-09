FROM python:3.9

RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./app/requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app/

CMD ["bash"]