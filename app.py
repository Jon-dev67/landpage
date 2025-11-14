from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dados dos produtos - substitua com seus links reais
    produtos = [
        {
            'nome': 'Suplemento Emagrecedor Natural',
            'descricao': 'psyllium 100% Original 120 capsulas psyllium Fibra Solúvel Fibra Alimentar.',
            'imagem': 'static/images/psyllium.webp',
            'link': 'https://s.shopee.com.br/5L44DE8u9h'
        },
        {
            'nome': 'Psyllium 60 Cápsulas',
            'descricao': 'Flora Viva - Psyllium 60 Cápsulas – Fibra Natural, Bem-Estar Digestivo.',
            'imagem': 'static/images/psyllium61.webp',
            'link': 'https://s.shopee.com.br/2LQSdIDIZM'
        },
        {
            'nome': 'QPS spirulina C/60 CÁPS 500MG Envio Imediato',
            'descricao': 'Inibe o apetite e impede o acúmulo de gordura corporal.',
            'imagem': 'static/images/quitosana.webp',
            'link': 'https://s.shopee.com.br/VyoTH8LQBh'
        },
        {
            'nome': 'PSYLLIUM 100% PURO',
            'descricao': 'PSYLLIUM 100% PURO 500 Mg |Original| Flora Viva.',
            'imagem': 'static/images/produto3.webp',
            'link': 'https://s.shopee.com.br/7AViQ9BXjZ'
        }
    ]
    
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)