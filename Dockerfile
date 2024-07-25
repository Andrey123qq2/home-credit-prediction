FROM python:3.10-slim-buster

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

ENV PYTHONPATH "${PYTHONPATH}:app/src/"

COPY . /app

RUN chmod +x /app

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

CMD ["./start.sh"]
