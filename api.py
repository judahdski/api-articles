from flask import *
import json, time
import mysql.connector
from dbconfig import DB_CONFIG

app = Flask(__name__)

# Fungsi untuk mendapatkan koneksi ke database
def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn


# /article/ ['POST']
# Create article
@app.route('/article/', methods=['POST'])
def create_article():
    try:
        # Open connection to db
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ambil data dari argument
        title = str(request.args.get('title'))
        content = str(request.args.get('content'))
        category = str(request.args.get('category'))
        created_date = time.time()
        updated_date = time.time()
        status = str(request.args.get('status'))

        # Buat query untuk tambah data ke db
        query = 'INSERT INTO `posts`(`id`, `title`, `content`, `category`, `created_date`, `updated_date`, `status`) VALUES ('',%s,%s,%s,%s,%s,%s)'
        cursor.execute(query, (title, content, category, created_date, updated_date, status))
        conn.commit()

        # Close connection from db
        cursor.close()
        conn.close()

        return jsonify({'message': 'Artikel berhasil dibuat'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# /article/<limit>/<offset>
# Get all articles
@app.route("/articles/<int:limit>/<int:offset>", methods=["GET"])
def get_all_articles(limit, offset):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query untuk mengambil semua data dari tabel posts
        query = "SELECT * FROM posts"
        cursor.execute(query)
        result = cursor.fetchall()

        # Format hasil query menjadi format JSON
        articles = []
        for row in result:
            article = {
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "category": row[3],
                "created_date": row[4],
                "updated_date": row[5],
                "status": row[6],
            }
            articles.append(article)

        # Menutup kursor dan koneksi setelah selesai
        cursor.close()
        conn.close()

        limited_articles = articles[offset : offset + limit]

        return jsonify({"articles": limited_articles})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# /article/<id>
# Get one article
@app.route("/article/<int:id>", methods=["GET"])
def get_one_article(id):
    try:
        # Open koneksi ke db
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query untuk ambil 1 data di table posts
        query = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(query)
        result = cursor.fetchall()

        # Ubah result menjadi bentuk json
        articles = []
        for row in result:
            article = {
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "category": row[3],
                "created_date": row[4],
                "updated_date": row[5],
                "status": row[6],
            }
            articles.append(article)

        # Tutup koneksi di db
        cursor.close()
        conn.close()

        return jsonify({"article": articles})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# /article/<id>
# Update the article
@app.route("/article/<int:id>/", methods=["POST", "PUT", "PATCH"])
def update_article(id):
    try:
        # Open koneksi ke db
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ambil data artikel dari argument
        title = str(request.args.get('title'))
        content = str(request.args.get('content'))
        category = str(request.args.get('category'))
        updated_date = time.time()
        status = str(request.args.get('status'))

        # Query update artikel di db
        query = 'UPDATE `posts` SET `title`=%s,`content`=%s,`category`=%s,`updated_date`=%s,`status`=%s WHERE id = %s'
        cursor.execute(query, (title, content, category, updated_date, status, id))
        conn.commit()

        # Close koneksi dari db
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# /article/<id>
# Delete the article
@app.route("/article/<int:id>", methods=["POST", "DELETE"])
def delete_article(id):
    try:
        # Open koneksi db
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query untuk hapus data di db
        query = f'DELETE FROM `posts` WHERE id = {id}'
        cursor.execute(query)
        conn.commit()

        # Close koneksi db
        cursor.close()
        conn.close()

        return jsonify({'message': 'Berhasil menghapus artikel'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


if __name__ == "__main__":
    app.run()
