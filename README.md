# 🚀 AI Ready Project Cleaner

Ferramenta em Python para gerar uma versão limpa do seu projeto antes de enviar para IA como Gemini, ChatGPT ou Claude.

---

## 🔥 Problema

Ao enviar projetos para IA, você acaba incluindo:

- node_modules (gigantesco)
- ambientes virtuais (venv)
- arquivos `.env` (RISCO 🔥)
- caches, logs e builds

Resultado:  
❌ IA lenta  
❌ análise ruim  
❌ risco de expor dados  

---

## ✅ Solução

Este script:

✔ Cria uma cópia limpa do projeto  
✔ Remove arquivos desnecessários  
✔ Mantém a estrutura original  
✔ Protege dados sensíveis  

---

## 📦 Como usar (FORMA SIMPLES)

### 👉 Opção 1 — Rodar dentro do projeto

1. Copie o arquivo `clean.py` para a raiz do seu projeto:

``` id="d4mfzi"
/meu-projeto
│
├── app/
├── backend/
├── frontend/
├── clean.py  👈 AQUI

Execute:

python clean.py
📁 Resultado

Será criada automaticamente uma pasta:

clean_project/

📌 Dentro dela estará a versão limpa do seu projeto.

⚙️ Como usar (FORMA PROFISSIONAL)
👉 Opção 2 — Passando caminhos

Você pode rodar o script de qualquer lugar passando:

python clean.py ORIGEM DESTINO
Exemplo:
python clean.py "C:\Projetos\MeuApp" "C:\Projetos\MeuApp_limpo"
📌 O que acontece:

ORIGEM → pasta do projeto original

DESTINO → onde será criada a versão limpa

Se a pasta destino já existir:

🔥 Ela será limpa automaticamente antes da cópia

🧠 Comportamento importante

❌ NUNCA apaga seu projeto original

✅ Sempre cria uma cópia separada

🔁 Se rodar novamente → sobrescreve o destino

🧹 O que é removido automaticamente
Pastas:

venv / .venv / env

node_modules

pycache

.git

.vscode / .idea

build / dist

Arquivos:

.env (todos)

.log, .tmp, .cache

.DS_Store, Thumbs.db

⚙️ Personalização

Edite no código:

FOLDERS_TO_IGNORE
FILES_TO_IGNORE
EXTENSIONS_TO_IGNORE
💡 Casos de uso

Enviar projeto para IA (Gemini / ChatGPT)

Revisão de código

Subir projeto limpo no GitHub

Compartilhar com clientes

🔥 Pro Tip

Use antes de pedir para IA:

"Analise esse projeto e sugira melhorias"

A resposta fica MUITO melhor.

⭐ Contribuição

Pull requests são bem-vindos!

📣 Autor

Se isso te ajudou, deixa uma ⭐ no repositório!