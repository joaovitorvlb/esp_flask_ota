# Para criar um ambiente virtual e executar
python3 -m venv .venv
source .venv/bin/activate
deactivate

# Salva na variavel de ambiente o nome da aplicação
export FLASK_APP=main.py

# instala os pacotes para a aplicação
pip install -r requeriments.txt

# comando que inicia a aplicação
flask run

# Cria as tabelas no mysql em um banco ja instanciado na aplicação
# Os dois ultimos comandos é usado para fazer algumas alterações que podem aparecer
flask db init      # É executado somente para ciar o versionamento de migração
flask db migrate
flask db upgrade

# Exemplo de inserção de dados no mysql usando flask shell
flask shell

>>> from main import db, Users, Products
>>> user = Users()
>>> user.nome = "Joao"
>>> user.cpf= "999.999.999.99"
>>> user.idade = 43
>>> prod = Products()
>>> prod.nome = "detergente"
>>> prod.peso = "200"
>>> prod.quantidade = 2000
>>> db.session.add(user)
>>> db.session.add(prod)
>>> db.session.commit()