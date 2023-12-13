FROM python:3-alpine
 
WORKDIR /app
 
COPY requirements.txt .

RUN pip install -r requirements.txt
 
COPY app.py app.py

EXPOSE 3000
 
CMD ["gunicorn", "--bind", ":3000", "app:app"]
