FROM python:3.6

# Defining work directory
WORKDIR /usr/app

# Copying requirements
COPY ./requirements.txt ./

# Installing requirements
RUN pip install -r requirements.txt

# Copying all files
COPY ./ ./

CMD ["python3", "discord_bot.py"]