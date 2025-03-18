import json

# Archivo donde se guardarán los usuarios y notas
USERS_FILE = "users.json"
NOTES_FILE = "notes.json"

# Función para cargar datos desde un archivo JSON
def load_data(file, default_data):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_data

# Función para guardar datos en un archivo JSON
def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

 
# Función para registrar usuarios
def register():
    users = load_data(USERS_FILE, {})
    username = input("Ingrese un nombre de usuario: ")
    if username in users:
        print("El usuario ya existe.")
        return
    password = input("Ingrese una contraseña: ")
    role = input("Ingrese el rol (profesor/estudiante): ")
    if role not in ["profesor", "estudiante"]:
        print("Rol inválido.")
        return
    users[username] = {"password": password, "role": role}
    save_data(USERS_FILE, users)
    print("Usuario registrado exitosamente.")  


# Función para iniciar sesión
def login():
    users = load_data(USERS_FILE, {})
    username = input("Usuario: ")
    password = input("Contraseña: ")
    if username in users and users[username]["password"] == password:
        print(f"Bienvenido {username} ({users[username]['role']})")
        return username, users[username]["role"]
    print("Credenciales incorrectas.")
    return None, None   


# Función para agregar notas (solo profesores)
def add_note():
    notes = load_data(NOTES_FILE, {})
    student = input("Ingrese el nombre del estudiante: ")
    note = float(input("Ingrese la nota: "))
    if student not in notes:
        notes[student] = []
    notes[student].append(note)
    save_data(NOTES_FILE, notes)
    print("Nota agregada correctamente.")

# Función para ver notas y promedio
def view_notes():
    notes = load_data(NOTES_FILE, {})
    student = input("Ingrese su nombre de usuario: ")
    if student in notes:
        student_notes = notes[student]
        print(f"Notas: {student_notes}")
        print(f"Promedio: {sum(student_notes) / len(student_notes):.2f}")
    else:
        print("No hay notas registradas para este usuario.")