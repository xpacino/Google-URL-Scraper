![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png)

# Google URL Scraper (Oxylabs API)

Bu Python scripti, **Oxylabs Realtime API** kullanarak Google arama sonuçlarından URL’leri toplamanıza olanak tanır. Çekilen URL’ler JSON dosyasına kaydedilir ve ekranda sadece toplam kaç URL çekildiği gösterilir. Script Python 3.8.x’in tüm sürümleri ile çalışacak şekilde tasarlanmıştır.

---

## Özellikler

- Belirli anahtar kelimeler için Google arama sonuçlarını çekme.
- Kaç sayfa sonuç çekileceğini belirleme.
- Aramayı belirli bir ülkeye göre lokalize etme.
- Çekilen URL’leri JSON dosyasına kaydetme.
- Çekilen URL sayısını ekrana yazdırma.

---

## Kullanım ve Api
![python3 scraper.py](https://img001.prntscr.com/file/img001/2htuRtydSDqEItN2y1txHw.png)  

Oxylabs API Basic Auth kullanır. Kullanıcı adı ve API anahtarınızı alıp request’e eklemeniz gerekir. Ücretsiz olarak deneme sürümü alıp api deneyebilirsiniz.

| Parametre     | Tip      | Açıklama                                |
| :------------ | :------- | :-------------------------------------- |
| `OX_API_USER` | `string` | **Gerekli**. Oxylabs kullanıcı adınız   |
| `OX_API_KEY`  | `string` | **Gerekli**. Oxylabs API anahtarınız    |
| `OX_API_URL`  | `string` | **Gerekli**. API endpoint URL’si        |

Örnek:
| Python Değişkeni | Atanan Değer                                    |
| :--------------- | :---------------------------------------------- |
| `OX_API_USER`    | `"USERNAME_645F3"`                              |
| `OX_API_KEY`     | `"APİ_KEY"`                               |
| `OX_API_URL`     | `"https://realtime.oxylabs.io/v1/queries"`      |


## Gereksinimler

- **Python 3.8.x veya üstü**
- `requests` kütüphanesi  
- `Windows & Linux & MacOS`
  
Kütüphaneyi yüklemek için:

- `pip3 install requests`





## Developer

- [@xpacino](https://www.github.com/xpacino) 

## Destek

TRX TV233GGoCdokwmeuSjmMk4kGCPGdxX1iVD
![Logo](https://img001.prntscr.com/file/img001/ewmcRxGXQriBcA69B6yWuQ.png)
  
