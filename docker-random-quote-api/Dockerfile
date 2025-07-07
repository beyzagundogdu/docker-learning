FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

# -w 4 = 4worker(coklu islem)
# -b 0.0.0.0:5000 = her yerden erisim(binding ayari), gunicornun hangi adres ve portta dinleyecegini ayarliyorsun.
# app:app = uygulama yolu, formati <dosya_adi>:<uygulama_ismi>
