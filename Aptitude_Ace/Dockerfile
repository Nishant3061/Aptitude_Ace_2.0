FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod  -R 777 /usr/src/app

EXPOSE 8000

ENTRYPOINT [ "python",  "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
