FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y curl 

WORKDIR /app

RUN mkdir server

COPY ./server /app/server

COPY ./config/server/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PORT=8000

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
