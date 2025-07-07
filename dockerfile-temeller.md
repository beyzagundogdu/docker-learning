# Dockerfile Temelleri ve Imaj Olusturma

## Dockerfile Nedir?
Docker imaji olusturmak icin kullanilan tarif (recipe) dosyasidir.
Icinde hangi taban imajin kullanilacagi, hangi komutlarin calistirilacagi ve container baslatilinca ne yapilacagi belirtilir. 

## Sik Kullanilan Dockerfile Komutlari

| Komut    | Aciklama    |
|----------|-------------|
| `FROM`   | Hangi taban imajdan baslatilacagini belirtir (zorunlu).  |
| `WORKDIR` | Imaj icinde calisilacak dizini belirler.   |
| `COPY`   | Disaridaki dosyalari imaj icine kopyalar.   |
| `RUN`    | Imaj olustururken calistirilacak komutlar.  |
| `CMD`    | Container baslatilinca calisacak komut (sadece bir tane olabilir).  |


## Ornek Dockerfile
```dockerfile
# Taban imaj
FROM ubuntu

# Calisma dizini
WORKDIR /app

# Build sirasinda calisacak komut
RUN echo "Merhaba Docker!"

# Container calistirildiginda calisacak komut 
CMD ["echo", "Container calisti!"] 
