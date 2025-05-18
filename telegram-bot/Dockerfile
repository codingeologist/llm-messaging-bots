
FROM python:3.12-slim-bookworm

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY metrics.py metrics.py

COPY telegram_bot.py telegram_bot.py

CMD ["python3", "telegram_bot.py"]