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
        },
        {
            'nome': 'Tradicional Funcional Fit - Envio Imediato + Brinde Sem Sabor',
            'descricao': '''Benefícios e Diferenciais:
- Suporte Metabólico: Auxilia na manutenção de um metabolismo eficiente, fundamental para o equilíbrio energético
- Gestão de Porções: Formulado com uma combinação especial de ervas, este suplemento promove a sensação de saciedade, auxiliando você no controle de porções e na manutenção do peso.
- Performance e Leveza: Contribui para o seu bem-estar geral, oferecendo mais energia e disposição para suas atividades diárias.
- Equilíbrio Hídrico: Ingredientes que dão suporte ao equilíbrio hídrico do corpo.
- Fórmula Limpa: Produto livre de glúten..''',
            'imagem': 'static/images/fit1.webp',
            'link': 'https://mercadolivre.com/sec/2AQNvHn'
        },
        {
            'nome': '1 Pote Fitliv / Fit Liv Sem Sabor',
            'descricao': '''Aviso legal
• Idade mínima recomendada: 19 anos.
• Consumir junto com alimentos para facilitar sua assimilação.
• Este produto é um suplemento dietético, não um medicamento. 
•Suplementa dietas insuficientes. Consulte o seu médico e/ou farmacêutico..''',
            'imagem': 'static/images/fitliv.webp',
            'link': 'https://mercadolivre.com/sec/2tY1jau'
        },
        {
            'nome': 'Moreslim 1 Pote - Emagrecedor Natural Psyllium L-triptofan Sem Sabor',
            'descricao': '''Diferencias:
 
1. QUATRO cápsulas ao dia garantem total eficácia que produtos de duas capsulas não oferecem;
2. Sensação de saciedade e controle da compulsividade alimentar;
3. Contém triptofano para controlar ansiedade, maior culpada da alimentação excessiva;
4. Único composto com os 5 principais componentes naturais de ação emagrecedora;
5. Composto 100% natural, sem contraindicação e sem efeito colateral;
6. Testado e aprovado pela Anvisa (Agência de Vigilância Sanitária).''',
            'imagem': 'static/images/moreslin.webp',
            'link': 'https://mercadolivre.com/sec/2jdfpnN'
        },
    ]
    
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)