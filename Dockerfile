FROM some python 3.6 image

WORKDIR /app

COPY . .

CMD [ "python3.6", "src/main.py"]