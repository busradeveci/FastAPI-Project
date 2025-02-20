# FastAPI Project

Bu proje, FastAPI kullanılarak geliştirilen bir web uygulamasıdır. Hızlı, verimli ve modern API'ler oluşturmayı amaçlamaktadır.

## Özellikler
- FastAPI ile yüksek performanslı API geliştirme
- Asenkron işlemler desteği
- Otomatik API belgeleri (Swagger & ReDoc)
- Kolay genişletilebilir yapı

## Kurulum

### Gereksinimler
- Python 3.8+
- FastAPI
- Uvicorn

### Adımlar
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/Busradeveci/FastAPI-Project.git
   cd FastAPI-Project
   ```
2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. Uygulamayı başlatın:
   ```bash
   uvicorn main:app --reload
   ```

## API Kullanımı
Uygulama çalıştırıldığında, aşağıdaki URL'lerden API dokümantasyonuna erişebilirsiniz:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Katkıda Bulunma
Katkıda bulunmak için bir **fork** oluşturup değişikliklerinizi **pull request** olarak gönderebilirsiniz.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır.
