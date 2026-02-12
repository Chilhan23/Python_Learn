from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        
        try:
            if form_type == 'persegi':
                s = float(request.form['sisi'])
                results['persegi'] = s * s
                
            elif form_type == 'segitiga':
                a = float(request.form['alas'])
                t = float(request.form['tinggi'])
                results['segitiga'] = 0.5 * a * t
                
            elif form_type == 'bola':
                r = float(request.form['jari_jari'])
                results['bola'] = 4 * 3.14 * (r ** 2)
                
            elif form_type == 'bep':
                bt = float(request.form['biaya_tetap'])
                bv = float(request.form['biaya_variabel'])
                hj = float(request.form['harga_jual'])
                margin = hj - bv
                if margin <= 0:
                    results['bep_error'] = "Harga jual harus > biaya variabel!"
                else:
                    results['bep'] = bt / margin
                    
        except ValueError:
            results['error'] = "Input harus angka, Cok!"

    return render_template('index.html', res=results)

if __name__ == '__main__':
    app.run(debug=True)