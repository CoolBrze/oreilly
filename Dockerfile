FROM python:3.9-slim-bullseye

EXPOSE 8000

WORKDIR /
COPY ./api /
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
