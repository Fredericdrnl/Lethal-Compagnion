FROM python:3

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python3", "router.py" ]