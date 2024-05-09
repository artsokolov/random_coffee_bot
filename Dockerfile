FROM python:3.9

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./entrypoint.sh /src/entrypoint.sh

RUN chmod +x /src/entrypoint.sh

COPY ./app /src/app

ENTRYPOINT ["/entrypoint.sh"]