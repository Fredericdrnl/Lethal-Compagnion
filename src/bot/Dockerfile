FROM python:3.9.10

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]