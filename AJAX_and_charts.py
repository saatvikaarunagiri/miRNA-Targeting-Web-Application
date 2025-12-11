from flask import Flask, render_template, request, jsonify
import pymysql
import json

application = Flask(__name__)
app = application
print(app.url_map)

def get_db_connection():
    try:
        conn = pymysql.connect(
            host='xxxxxxx',
            user='xxxxxxx',
            password='xxxxxxx',
            db='miRNA',
            port=xxxxxxx,
            charset='xxxxxxx'
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/')
def index():
    return render_template('saatvika_AJAX_and_charts.html')

@app.route('/histogram', methods=['GET'])
def histogram():
    gene_name = request.args.get('gene_name', '').strip()
    if not gene_name:
        return jsonify([])

    conn = get_db_connection()
    if not conn:
        return jsonify([])

    cursor = conn.cursor()

    if gene_name.lower().startswith("hsa-mir"):
        query = """
            SELECT t.score
            FROM targets t
            JOIN miRNA m ON t.mid = m.mid
            WHERE m.name = %s
        """
    else:
        query = """
            SELECT t.score
            FROM targets t
            JOIN gene g ON t.gid = g.gid
            WHERE g.name = %s
        """

    cursor.execute(query, (gene_name,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    scores = [float(row[0]) for row in results if row[0] is not None]
    return jsonify(scores)

@app.route('/gene_search', methods=['GET'])
def gene_search():
    seq = request.args.get('sequence', '').strip().upper()
    if not seq or not (7 <= len(seq) <= 9) or not all(base in 'ACGT' for base in seq):
        return jsonify([])

    conn = get_db_connection()
    if not conn:
        return jsonify([])

    cursor = conn.cursor()
    pattern = f"%{seq}%"
    query = """
        SELECT name, seq, chr, start, stop
        FROM gene
        WHERE UPPER(seq) LIKE %s
    """

    cursor.execute(query, (pattern,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    response = []
    for name, full_seq, chromosome, start, stop in results:
        idx = full_seq.find(seq)
        if idx != -1:
            start_idx = max(0, idx - 5)
            end_idx = min(len(full_seq), idx + len(seq) + 5)
            context = full_seq[start_idx:end_idx]
            response.append({
                'gene': name,
                'sequence': context,
                'chromosome': chromosome,
                'start': start,
                'stop': stop
            })

    response.sort(key=lambda x: x['gene'])
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
