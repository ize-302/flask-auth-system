FROM python:3-alpine
 
WORKDIR /app
 
COPY requirements.txt .

RUN pip install -r requirements.txt
 
COPY app.py app.py
 
CMD ["gunicorn", "app:app"]