# Docker Temel Komutlar ve Notlar

## Docker Nedir?
Uygulamalari ve bagimliliklari **container** adi verilen kutulara paketleyen bir platformdur.
Bu sayede uygulamalar her ortamda ayni sekilde calisir.

## Temel Kavramlar

| Kavram      | Anlami              |
|-------------|---------------------|
| **Image**   | Uygulamanin paketlemis hali  |
| **Container** | Calisan image (uygulama kutusu) |
| **Dockerfile** | Image olusturmak icin tarif dosyasi  |
| **Docker Hub** | Imajlarin paylasildigi resmi depo  |

## Onemli Docker Komutlari

### Imajlari Listeleme
```bash
docker images
```

### Calisan Containerleri Listeleme
```bash
docker ps
```

### Tum Containerleri Listeleme (Duranlar Dahil)
```bash
docker ps -a
```

### Container Calistirma
```bash
docker run -it ubuntu bash
```

### Container Durdurma
```bash
docker stop <cantainer_id>
```

### Container Silme
```bash
docker rm <container_id> 
```

### Imaj Silme
```bash
docker rmi <image_id>
```

### Container Loglarini Goruntuleme
```bash
docker logs <container_id> 
```

### Docker Sistem Temizligi
```bash
docker system prune
```
> Kullanilmayan her seyi temizler.


### Mini Not:
. Container & Image ID'leri tam yazilmak zorunda degildir, ilk birkac harf yeterlidir.
. Cikmak icin: exit

### Ilk Container Testi 
```bash
docker run hello-world
```

