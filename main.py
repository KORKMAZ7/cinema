from flask import Flask, request, jsonify

app = Flask(__name__)

filmler = {
    "1": {"ad": "Film 1", "fiyat": 10, "koltuklar": 40, "seanslar": ["10:00", "13:00", "16:00"]},
    "2": {"ad": "Film 2", "fiyat": 8, "koltuklar": 40, "seanslar": ["11:00", "14:00", "17:00"]},
    "3": {"ad": "Film 3", "fiyat": 12, "koltuklar": 40, "seanslar": ["12:00", "15:00", "18:00"]}
}

@app.route('/filmler', methods=['GET'])
def filmleri_getir():
    return jsonify(filmler)

@app.route('/bilet-al', methods=['POST'])
def bilet_al():
    data = request.get_json()
    secilen_film = data.get('film_id')
    secilen_seans = data.get('seans')
    bilet_adedi = data.get('bilet_adedi')

    if secilen_film and secilen_seans and bilet_adedi > 0:
        # Bilet alma işlemleri burada gerçekleştirilebilir.
        toplam_fiyat = filmler[secilen_film]["fiyat"] * bilet_adedi
        mesaj = f"Film: {filmler[secilen_film]['ad']}, Seans: {secilen_seans}, Bilet Sayısı: {bilet_adedi}, Toplam Tutar: {toplam_fiyat} TL"
        return jsonify({'success': True, 'message': mesaj}), 200
    else:
        return jsonify({'success': False, 'message': 'Geçersiz istek'}), 400

if __name__ == '__main__':
    app.run(debug=True)
