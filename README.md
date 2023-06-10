# Dashboard Article Management API

API ini digunakan untuk menambahkan, mengubah, dan menghapus artikel untuk ditampilkan di dashboard.

Base URL: http://judahdasuki.pythonanywhere.com

## Endpoints

### POST /article/

Membuat artikel baru.

#### Parameter Permintaan

| Parameter  | Tipe Data | Deskripsi                                   |
|------------|-----------|---------------------------------------------|
| `title`    |  string   | 	Judul artikel baru                         |
| `content`  |  string   | 	Isi artikel baru                           |
| `category` |  string   | 	Kategori artikel baru                      |
| `status`   |  string   | 	Status artikel baru (publish/draft/ trash) |

#### Contoh Permintaan
```POST /article/?title=Judul+Artikel+Baru&content=Isi+Artikel+Baru&category=Kategori+A&status=draft```

#### Contoh Respon

```json
Status: 200 OK
Content-Type: application/json

{
  "message": "Artikel berhasil dibuat!"
}
```

### GET /articles/\<limit\>/\<offset\>

Mengambil semua artikel dengan batasan jumlah dan offset yang ditentukan.

#### Parameter Permintaan

| Parameter  | Tipe Data | Deskripsi                           |
|------------|-----------|-------------------------------------|
| `limit`    | integer   | Jumlah artikel yang akan ditampilkan |
| `offset`   | integer   | Offset untuk memulai penampilan      |

#### Contoh Permintaan
```GET /articles/10/0```

#### Contoh Respon

```json
Status: 200 OK
Content-Type: application/json

{
  "articles": [
    {
      "id": 1,
      "title": "Judul Artikel 1",
      "content": "Isi dari artikel 1",
      "category": "Kategori A",
      "created_date": "2023-06-01 10:00:00",
      "updated_date": "2023-06-02 15:30:00",
      "status": "publish"
    },
    {
      "id": 2,
      "title": "Judul Artikel 2",
      "content": "Isi dari artikel 2",
      "category": "Kategori B",
      "created_date": "2023-06-03 09:45:00",
      "updated_date": "2023-06-04 14:20:00",
      "status": "draft"
    },
    ...
  ]
}
```

### GET /article/\<id\>

Mengambil semua artikel dengan batasan jumlah dan offset yang ditentukan.

#### Parameter Permintaan

| Parameter  | Tipe Data | Deskripsi                           |
|------------|-----------|-------------------------------------|
| `id`       |  integer  | ID artikel yang ingin diambil       |

#### Contoh Permintaan
```GET /article/1```

#### Contoh Respon

```json
Status: 200 OK
Content-Type: application/json

{
  "article": {
    "id": 1,
    "title": "Judul Artikel 1",
    "content": "Isi dari artikel 1",
    "category": "Kategori A",
    "created_date": "2023-06-01 10:00:00",
    "updated_date": "2023-06-02 15:30:00",
    "status": "publish"
  }
}
```

### POST /article/\<id\>

Mengubah artikel berdasarkan ID.

#### Parameter Permintaan

| Parameter  | Tipe Data | Deskripsi                            |
|------------|-----------|--------------------------------------|
| `id`       |  integer  | 	ID artikel yang akan diubah         |
| `title`    |  string   | 	Judul artikel baru                  |
| `content`  |  string   | 	Isi artikel baru                    |
| `category` |  string   | 	Kategori artikel baru               |
| `status`   |  string   | 	Status artikel baru (publish/draft) |

#### Contoh Permintaan
```POST /article/1?title=Judul+Artikel+Baru&content=Isi+Artikel+Baru&category=Kategori+A&status=draft```

#### Contoh Respon

```json
Status: 200 OK
Content-Type: application/json

{
  "message": "Artikel berhasil diubah!"
}
```

### POST /article/\<id\>

Menghapus artikel berdasarkan ID.

#### Parameter Permintaan

| Parameter  | Tipe Data | Deskripsi                            |
|------------|-----------|--------------------------------------|
| `id`       |  integer  | 	ID artikel yang akan dihapus        |

#### Contoh Permintaan
```POST /article/1```

#### Contoh Respon

```json
Status: 200 OK
Content-Type: application/json

{
  "message": "Berhasil menghapus artikel"
}
```

### Kesalahan / Error
Jika terjadi kesalahan dalam permintaan, respon akan berisi pesan kesalahan (exception) yang sesuai.
<br><br>
## Ada yang ingin ditanya
Silahkan hubungi, judahjmdasuki@gmail.com (email) / 081387306360 (whatsapp) <br>
Teknologi : Python (Bahasa Pemrograman), pythonanywhere.com (Platform hosting)
