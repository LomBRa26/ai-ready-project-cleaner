import os
import shutil

# 🔥 Pastas que NÃO devem ser copiadas
FOLDERS_TO_IGNORE = [
    ".venv", "venv", "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".nuxt",
    ".idea",
    ".vscode",
    "htmlcov",
    ".git"
]

# 🔥 Arquivos específicos
FILES_TO_IGNORE = [
    ".coverage",
    "Thumbs.db",
    ".DS_Store"
]

# 🔥 Extensões
EXTENSIONS_TO_IGNORE = [
    ".log",
    ".tmp",
    ".cache"
]

def should_ignore(file_name):
    if file_name in FILES_TO_IGNORE:
        return True
    if any(file_name.endswith(ext) for ext in EXTENSIONS_TO_IGNORE):
        return True
    if file_name.startswith(".env"):
        return True
    return False

def clear_directory(path):
    """Remove tudo dentro da pasta sem apagar ela"""
    if not os.path.exists(path):
        return

    print(f"\n🧹 Limpando destino: {path}")

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"[REMOVIDO] Pasta: {item_path}")
            else:
                os.remove(item_path)
                print(f"[REMOVIDO] Arquivo: {item_path}")
        except Exception as e:
            print(f"[ERRO] {item_path} -> {e}")

def copy_clean_project(src, dst):
    clear_directory(dst)

    print(f"\n📦 Gerando versão limpa...")

    for root, dirs, files in os.walk(src):

        # 🔥 Evita copiar a própria pasta destino
        if os.path.abspath(root).startswith(os.path.abspath(dst)):
            continue

        # Remove pastas ignoradas
        dirs[:] = [d for d in dirs if d not in FOLDERS_TO_IGNORE]

        relative_path = os.path.relpath(root, src)
        target_dir = os.path.join(dst, relative_path)

        os.makedirs(target_dir, exist_ok=True)

        for file in files:
            if should_ignore(file):
                print(f"[IGNORADO] {os.path.join(root, file)}")
                continue

            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)

            try:
                shutil.copy2(src_file, dst_file)
                print(f"[COPIADO] {src_file}")
            except Exception as e:
                print(f"[ERRO] {src_file} -> {e}")

def main():
    source_path = os.getcwd()
    destination_path = os.path.join(source_path, "clean_project")

    print("🚀 AI Ready Project Cleaner")
    print(f"📂 Origem: {source_path}")
    print(f"📁 Destino: {destination_path}")

    os.makedirs(destination_path, exist_ok=True)

    copy_clean_project(source_path, destination_path)

    print("\n✅ Projeto limpo gerado com sucesso!")
    print("👉 Use a pasta 'clean_project' para enviar à IA")

if __name__ == "__main__":
    main()