FROM python:3.8
LABEL maintainer="sachajw@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app/bubble-sort.py"]