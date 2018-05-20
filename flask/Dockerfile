FROM python:alpine

EXPOSE 5000

WORKDIR app

COPY ./web /app/

RUN apk update && apk upgrade &&\
 apk add postgresql=9.5.12-r0 &&\
 apk add postgresql-libs &&\
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY ./wait-for-postgresql.sh /

RUN chmod u+x /wait-for-postgresql.sh

ENTRYPOINT ["sh", "/wait-for-postgresql.sh"]

CMD ["python3", "app.py"]
