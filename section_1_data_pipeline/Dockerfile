# syntax=docker/dockerfile:1

FROM python:3.6

WORKDIR /app

COPY ./requirements.txt requirements.txt

# Install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r requirements.dev \
    && pip install --no-cache-dir -r requirements.prod \
    && pip list

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]