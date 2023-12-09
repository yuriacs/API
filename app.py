import pymongo

from fastapi import FastAPI

app = FastAPI()

# Conexão com o banco de dados
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cadastro_usuarios"]
collection = db["usuarios"]

# Rotas

@app.post("/api/v1/usuarios")
def cadastrar_usuario(
  nome: str, 
  sobrenome: str, 
  numero_matricula: str, 
  cpf: str, 
  rg: str, 
  data_nascimento: str, 
  email: str, 
  login: str, 
  senha: str):
  """
  Rota para cadastrar um usuário.
  
  Returns:
    Um objeto JSON com as informações do usuário cadastrado.
  """

  # Cria o documento do usuário
  usuario = {
    "nome": nome,
    "sobrenome": sobrenome,
    "numero_matricula": numero_matricula,
    "cpf": cpf,
    "rg": rg,
    "data_nascimento": data_nascimento,
    "email": email,
    "login": login,
    "senha": senha
  }

  # Insere o documento no banco de dados
  collection.insert_one(usuario)

  # Retorna as informações do usuário cadastrado
  return usuario

@app.get("/api/v1/usuarios")
def listar_usuarios():
  """
  Rota para listar todos os usuários.

  Returns:
    Uma lista de objetos JSON com as informações de todos os usuários.
  """

  # Seleciona todos os documentos da coleção
  usuarios = collection.find()

  # Retorna uma lista de objetos JSON com as informações dos usuários
  return usuarios

@app.get("/api/v1/usuarios/{login}")
def buscar_usuario_por_login(login: str):
  """
  Rota para buscar um usuário pelo login.

  Args:
    login: Login do usuário.

  Returns:
    Um objeto JSON com as informações do usuário encontrado.
  """

  # Seleciona o documento da coleção com o login informado
  usuario = collection.find_one({"login": login})

  # Retorna o objeto JSON com as informações do usuário encontrado
  return usuario

@app.put("/api/v1/usuarios/{login}")
def atualizar_usuario(
login: str,
nome: str, 
sobrenome: str, 
numero_matricula: str, 
cpf: str, 
rg: str, 
data_nascimento: str, 
email: str, 
senha: str):
  """
  Rota para atualizar as informações de um usuário.

  Args:
    login: Login do usuário.
    nome: Nome do usuário.
    sobrenome: Sobre
  """