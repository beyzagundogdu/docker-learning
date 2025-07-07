# Taban imaj
FROM python:3.12-slim

# Calisma dizini
WORKDIR /app

# Gereksinimleri kopyala ve yukle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Uygulamayi kopyala
COPY . .

# Uygulamayi baslat
CMD ["python", "app.py"]
