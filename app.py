from flask import Flask, render_template

app = Flask(__name__)

# essa e a parte que tem os ddos dos produtos que aparece na pagina produto
produtos = [
    {
        "id": 1,
        "nome": "Camiseta Street",
        "imagem": "produto1.png",
        "preco": 79.90,
        "descricao": "Camiseta com estampa street style, feita com algodão premium. Ideal para looks urbanos."
    },
    {
        "id": 2,
        "nome": "Tênis Nike",
        "imagem": "produto2.png",
        "preco": 349.90,
        "descricao": "Tênis Nike com design esportivo, solado antiderrapante e amortecimento Air Max."
    },
    {
        "id": 3,
        "nome": "Camiseta Ferrari",
        "imagem": "produto3.png",
        "preco": 159.90,
        "descricao": "Camiseta oficial da Ferrari, com logo bordado e tecido tecnológico."
    },
    {
        "id": 4,
        "nome": "Boné Preto Nike",
        "imagem": "produto4.png",
        "preco": 89.90,
        "descricao": "Boné ajustável da Nike, perfeito para treinos e uso casual."
    },
    {
        "id": 5,
        "nome": "Tênis Airmax",
        "imagem": "produto5.png",
        "preco": 449.90,
        "descricao": "Tênis Nike Airmax, conforto extremo com visual moderno."
    },
    {
        "id": 6,
        "nome": "Luva da Nike",
        "imagem": "produto6.png",
        "preco": 99.90,
        "descricao": "Luva térmica Nike, ideal para esportes em dias frios."
    },
    {
        "id": 7,
        "nome": "Corrente de Ouro",
        "imagem": "produto7.png",
        "preco": 1299.90,
        "descricao": "Corrente banhada a ouro 18k, elegante e resistente."
    },
    {
        "id": 8,
        "nome": "Shorts Preto",
        "imagem": "produto8.png",
        "preco": 109.90,
        "descricao": "Shorts esportivo preto, leve e confortável para qualquer atividade física."
    }
]

# Página inicial
@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

# Página de produto
@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        return render_template('produto.html', produto=produto)
    return "Produto não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
