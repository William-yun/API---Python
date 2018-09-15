from flask import Flask
from flask import jsonify
from flask import request
import uuid

App = Flask(__name__)

Resposta = {"Status":"", "Dados":"", "Mensagem":"", "Ativo":""}
Alunos = []

@App.route("/alunos", methods=["GET"])
def listadealunos():
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Lista de alunos"
    Resposta["Ativo"] = "Ativo"
    Resposta["Dados"] = Alunos
    return jsonify(Resposta)

@App.route("/alunos/cadastrar", methods=["POST"])
def Cadastrodealuno():
    Dados = request.get_json()
    Id = str(uuid.uuid1())
    Nome = Dados["Nome"]
    Ra = Dados["Ra"]
    Ativo = Ativo["Ativo"]
    Alunos.append({"Id":Id, "Nome":Nome, "Ra":Ra, "Ativo":Ativo})
    
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Aluno cadastrado."
    Resposta["Ativo"] = "Ativo"
    Resposta["Dados"] = Alunos
    return jsonify(Resposta)

@App.route("/alunos/excluir/<Id>", methods=["DELETE"])
def ExcluirAluno(Id):

    i = None
    for i in Alunos:
        if i["Id"] == Id:
            Alunos.remove(i)
        else:
            i = None

    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Aluno Excluído"
    Resposta["Dados"] = i

    return jsonify(Resposta)

@App.route("/alunos/atualizar", methods=["PUT"])
def AtualizarAluno():
    Dados = request.get_json()
    
    for i in Alunos:
        if i["Id"] == Dados["Id"]:
            i["Nome"] = Dados["Nome"]
            i["Ra"] = Dados["Ra"]
            i["Ativo"] = Dados["Ativo"]
            break
    
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Aluno atualizado."
    Resposta["Dados"] = i

    return jsonify(Resposta)

if __name__ == "__main__":
    App.run(port=80)
