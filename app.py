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
            'link': 'https://s.shopee.com.br/12ZEX7oT'
        },
        {
            'nome': 'PSYLLIUM 100% PURO',
            'descricao': 'PSYLLIUM 100% PURO 500 Mg |Original| Flora Viva.',
            'imagem': 'static/images/produto3.webp',
            'link': 'https://s.shopee.com.br/7AViQ9BXjZ'
        },
        {
            'nome': 'Creme Seca Barriga Redutor de Medidas Seca Barriguinha 250g Muriel',
            'descricao': '''Ingredientes ativos: cafeína, centella asiática, extrato de chá verde, retinol e óleo de rosa mosqueta.
Benefícios: promove hidratação profunda, firmeza e melhora na textura da pele, iluminando e combatendo a flacidez.
Sustentabilidade: produto vegano, não testado em animais e com embalagem reciclável.
Testado dermatologicamente: seguro para uso contínuo e indicado para todos os tipos de pele..''',
            'imagem': 'static/images/seca_barriga.webp',
            'link': 'https://s.shopee.com.br/1LXyf5X7pt'
        }
    ]
    
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)