# Node.js Mini Docker Projesi

Bu proje temel bir Node.js web app'inin Docker container icinde nasil calistirildigini ogrenmek icin hazirlanmistir.

## Proje Amaci

- Node.js kullanarak basit bir web uygulamasi gelistirmek. 
- Uygulamayi Dockerfile ile dockerize etmek.
- Docker container icinde calisan uygulamaya tarayici uzerinden erisimek.

## Kullanilan Teknolojiler

- Node.js(express.js) 
- Docker 
- Dockerfile

## Uygulama Ozeti

- /hello endpointine istek atildiginda 'Merhaba, Node.js!' mesjaini dondurur.
- Uygulama 3000 portunda calisir.

## Proje Dosya Yapisi

```
docker-nodejs-mini-app/
|
|-----app.js       ->uygulama dosyasi
|-----package.json ->proje bagimliliklari ve scriptler
|-----Dockerfile   ->docker icin tarif dosyasi

```

## Calistirma Adimlari
### Proje Bagimliliklarini Kur 
```bash
npm install

```
### Docker Imaji Olustur
```bash
docker build -t nodejs-mini-app .
```
### Container'i Calistir
```bash
docker run -r 3000:3000 nodejs-mini-app
```

### Tarayiciyi Uzerinden Test
```bash
http://localhost:3000/hello
```


