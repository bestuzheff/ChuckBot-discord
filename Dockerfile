FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY discord-bot.py discord-bot.py
COPY ChuckText.txt ChuckText.txt
COPY .env .env

CMD [ "python3", "discord-bot.py"]