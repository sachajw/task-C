FROM python:3-slim
LABEL maintainer="sachajw@gmail.com"

COPY . /app

WORKDIR /app

ENV MAX_SIZE=10000

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app/bubble-sort.py"]
