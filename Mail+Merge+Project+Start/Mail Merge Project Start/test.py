import os

print("📍 Estoy ejecutando desde:", os.getcwd())

# Mostrar el contenido completo del proyecto
base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
print("📂 Carpeta madre del proyecto:", base_path)

input_path = os.path.join(base_path, "input", "Names")
print("🔍 Buscando archivos en:", input_path)

if os.path.exists(input_path):
    print("✅ Carpeta encontrada. Archivos:")
    print(os.listdir(input_path))
else:
    print("❌ La carpeta NO existe. Revisá el nombre exacto.")
