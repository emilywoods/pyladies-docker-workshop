FROM python:3.7

ADD app.py .
ADD setup.py .
ADD static static/
ADD templates templates/

RUN pip install -e .

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
