FROM python:3.6

WORKDIR /usr/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD ["python3", "competition_bot.py"]