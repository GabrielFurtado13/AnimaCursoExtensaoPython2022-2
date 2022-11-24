from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

gabriel = Pessoa(1, "Gabriel Furtado")
print(gabriel)

print(gabriel.nome)

print("DAQUI PRA FRENTE É ACESSO AO BANCO:")

db = Database()

pessoaDAO = PessoaDAO(db.conexao, db.cursor)

pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

novo = Pessoa(0, "Denzel Washington")

novo = pessoaDAO.save(novo)

pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)