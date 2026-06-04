import os
import shutil

tipos = {
    ".pdf": os.path.expanduser("~/Downloads/Documentos"),
    ".docx": os.path.expanduser("~/Downloads/Documentos"),
    ".txt": os.path.expanduser("~/Downloads/Documentos"),
    ".jpg": os.path.expanduser("~/Pictures"),
    ".jpeg": os.path.expanduser("~/Pictures"),
    ".png": os.path.expanduser("~/Pictures"),
    ".mp4": os.path.expanduser("~/Videos"),
    ".mov": os.path.expanduser("~/Videos"),
    ".mp3": os.path.expanduser("~/Music"),
    ".zip": os.path.expanduser("~/Downloads/Compactados"),
    ".rar": os.path.expanduser("~/Downloads/Compactados"),
    ".exe": os.path.expanduser("~/Downloads/Programas"),
}

pasta_downloads = os.path.expanduser("~/Downloads")

while True:
    resposta = input("Deseja organizar a pasta Downloads? (S/N): ")
    if resposta.lower() in ("s", "n"):
        break
    print("Digite apenas S ou N.")

if resposta.lower() != "s":
    print("Pasta Downloads não organizada.")
    input("Pressione Enter para fechar...")
    exit()

for nome_arquivo in os.listdir(pasta_downloads):
    caminho_completo = os.path.join(pasta_downloads, nome_arquivo)

    if os.path.isdir(caminho_completo):
        continue

    _, extensao = os.path.splitext(nome_arquivo)
    extensao = extensao.lower()

    if extensao in tipos:
        pasta_destino = tipos[extensao]
        os.makedirs(pasta_destino, exist_ok=True)
        shutil.move(caminho_completo, pasta_destino)
        print(f"Movido: {nome_arquivo} → {pasta_destino}")
    else:
        print(f"Ignorado: {nome_arquivo}")

print("\nOrganização concluída!")
input("\nAperte Enter para fechar...")