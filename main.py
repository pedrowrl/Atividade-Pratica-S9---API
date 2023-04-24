# Curso de Engenharia de Software - UniEVANGÉLICA 
# Disciplina de Programação Web 
# Dev: Pedro Wilson Rodrigues de Lima
# DATA 24/04/2023

from flask import Flask, jsonify, request

app = Flask(__name__)

# Criar uma lista dos personagens da série Os Simpsons
simpsons = [
    {"id": 1, "name": "Homer Simpson", "age": 39, "occupation": "Safety Inspector"},
    {"id": 2, "name": "Marge Simpson", "age": 36, "occupation": "Housewife"},
    {"id": 3, "name": "Bart Simpson", "age": 10, "occupation": "Student"},
    {"id": 4, "name": "Lisa Simpson", "age": 8, "occupation": "Student"},
    {"id": 5, "name": "Maggie Simpson", "age": 1, "occupation": "Baby"}
]

# Recuperar a lista dos personagens da série Os Simpsons
@app.route('/api/simpsons', methods=['GET'])
def get_simpsons():
    return jsonify(simpsons)

# Criar um novo personagem pra série Os Simpson
@app.route('/api/simpsons', methods=['POST'])
def create_simpson():
    new_simpson = {
        "id": request.json["id"],
        "name": request.json["name"],
        "age": request.json["age"],
        "occupation": request.json["occupation"]
    }
    simpsons.append(new_simpson)
    return jsonify(new_simpson), 201

# Recuperar informações de um personagem específico da série Os Simspons usando o ID
@app.route('/api/simpsons/<int:simpson_id>', methods=['GET'])
def get_simpson(simpson_id):
    for simpson in simpsons:
        if simpson["id"] == simpson_id:
            return jsonify(simpson)
    return jsonify({"message": "Simpson not found"}), 404

# Atualizar informações de um personagem específico da série Os Simpsons usando o ID
@app.route('/api/simpsons/<int:simpson_id>', methods=['PUT'])
def update_simpson(simpson_id):
    for simpson in simpsons:
        if simpson["id"] == simpson_id:
            simpson["name"] = request.json["name"]
            simpson["age"] = request.json["age"]
            simpson["occupation"] = request.json["occupation"]
            return jsonify(simpson)
    return jsonify({"message": "Simpson not found"}), 404

# Excluir um personagem específico da série Os Simpsons usando o ID
@app.route('/api/simpsons/<int:simpson_id>', methods=['DELETE'])
def delete_simpson(simpson_id):
    for simpson in simpsons:
        if simpson["id"] == simpson_id:
            simpsons.remove(simpson)
            return jsonify({"message": "Simpson deleted"})
    return jsonify({"message": "Simpson not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
