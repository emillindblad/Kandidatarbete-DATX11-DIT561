FROM python:3.8-slim

WORKDIR /app
COPY /src /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLAG=flag{default_flag}


CMD /bin/sh -c "echo \"${FLAG}\" > /app/flag.txt && flask run"
