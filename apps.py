from flask import Flask, jsonify, request
import json

app = Flask(__name__) 

users=[
    {
        "Username": "Admin",
        "Age": "25"
    },
    {
        "Username": "Hernan",
        "Age":"30"
    }
]
#leer usuarios
@app.route('/users',methods=["GET"])
def getUsers():
    return jsonify(users),200

@app.route('/users/<string:username>',methods=["GET"])
def getNombre(username):
    resultado = next((user for user in users if user["Username"]==username), None)
    if resultado is not None:
        return jsonify(resultado)
    else:
        return "No se encuentra el usuario"

#crear usuario

@app.route('/users',methods=["POST"])
def addUser():
    body=json.loads(request.data)

    userName= body["Username"]
    age= body["Age"]
    
    newUser = {
        "Username": userName,
        "Age": age
    }

    users.append(newUser)
    return "Se ha creado el usuario"


#borrar usuario

@app.route('/users/<string:username>',methods=["DELETE"])
def deleteUser(username):
    userFound=None
    for index, user in enumerate(users):
        if user["Username"]==username:
            userFound=user
            users.pop(index)

    if userFound is not None:
        return "Usuario eliminado"
    else:
        return "Usuario no encontrado"

#actualizar usuario

@app.route('/user/<string:username>',methods=["PUT"])
def updateUser(username):
    body = json.loads(request.data)

    newUsername = body["Username"]
    newAge = body["Age"]
    userUpdated = None

    updatedUser = {
        "Username": newUsername,
        "Age": newAge
    }

    for index, user in enumerate(users):
        if user["Username"] == username:
            userUpdated = updatedUser
            users[index] = updatedUser
            

    if userUpdated is not None:
        return "Usuario Actualizado"
    else:
        return "El usuario no fue encontrado" 




if __name__ == "__main__":
    app.run()
