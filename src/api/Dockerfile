FROM python:3

ENTRYPOINT [ “python” ]
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY /requirements.txt .
RUN echo $DB_NAME
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python3", "router.py" ]