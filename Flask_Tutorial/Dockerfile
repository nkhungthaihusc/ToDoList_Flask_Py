FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r modules.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
    