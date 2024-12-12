from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan data siswa di dalam list
data_siswa = []

@app.route('/')
def form_nilai():
    return render_template('form_nilai.html')

@app.route('/submit', methods=['POST'])
def submit_nilai():
    # Mengambil data dari form
    nama = request.form.get('nama')
    matematika = request.form.get('matematika')
    fisika = request.form.get('fisika')
    kimia = request.form.get('kimia')

    # Menambahkan data ke dalam list
    data_siswa.append({
        'nama': nama,
        'matematika': matematika,
        'fisika': fisika,
        'kimia': kimia
    })

    # Redirect ke halaman daftar nilai
    return redirect(url_for('daftar_nilai'))

@app.route('/daftar')
def daftar_nilai():
    return render_template('daftar_nilai.html', data_siswa=data_siswa)

if __name__ == '__main__':
    app.run(debug=True)
