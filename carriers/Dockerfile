# Dockerfile
FROM python:3.6
WORKDIR /carrier
COPY djangodocker djangodocker
COPY manage.py requirements.txt /carrier/
RUN pip install -r requirements.txt && \
        python manage.py collectstatic --noinput

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]