# 🚀 AI Ready Project Cleaner

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-success)

Ferramenta em Python para gerar uma versão limpa do seu projeto antes de enviar para IA como Gemini, ChatGPT ou Claude.

---

## 🔥 Problema

Ao enviar projetos para IA, você acaba incluindo:

- node_modules (gigante)
- ambientes virtuais (venv)
- arquivos `.env` (RISCO 🔥)
- caches, logs e builds

Resultado:

- ❌ IA lenta  
- ❌ análise ruim  
- ❌ risco de expor dados  

---

## ✅ Solução

Este script:

- ✔ Cria uma cópia limpa do projeto  
- ✔ Remove arquivos desnecessários  
- ✔ Mantém a estrutura original  
- ✔ Protege dados sensíveis  

---

## 📦 Como usar (forma simples)

### 1. Coloque o script na raiz do projeto

Exemplo:

```
meu-projeto/
├── app/
├── backend/
├── frontend/
├── clean.py
```

---

### 2. Execute

```bash
python clean.py
```

---

### 📁 Resultado

Será criada automaticamente uma pasta:

```
clean_project/
```

Com a versão limpa do seu projeto.

---

## ⚙️ Como usar (modo avançado)

Você também pode passar caminhos manualmente:

```bash
python clean.py ORIGEM DESTINO
```

### Exemplo:

```bash
python clean.py "C:\Projetos\MeuApp" "C:\Projetos\MeuApp_limpo"
```

---

### 📌 Como funciona

- `ORIGEM` → seu projeto original  
- `DESTINO` → onde será criada a cópia limpa  

Se o destino já existir:

> 🔥 Ele será LIMPO automaticamente antes da cópia

---

## 🧠 Comportamento importante

- ❌ Nunca apaga seu projeto original  
- ✅ Sempre cria uma cópia separada  
- 🔁 Pode rodar várias vezes (sobrescreve o destino)  

---

## 🧹 O que é removido automaticamente

### Pastas:
- venv / .venv / env  
- node_modules  
- __pycache__  
- .git  
- .vscode / .idea  
- build / dist  

### Arquivos:
- `.env` (todos)  
- `.log`, `.tmp`, `.cache`  
- `.DS_Store`, `Thumbs.db`  

---

## ⚙️ Personalização

Edite no código:

- `FOLDERS_TO_IGNORE`
- `FILES_TO_IGNORE`
- `EXTENSIONS_TO_IGNORE`

---

## 💡 Casos de uso

- Enviar projeto para IA (Gemini / ChatGPT)  
- Revisão de código  
- Subir projeto limpo no GitHub  
- Compartilhar com clientes  

---

## 🔥 Pro Tip

Antes de usar IA:

> "Analise esse projeto e sugira melhorias"

Com o projeto limpo, a resposta melhora MUITO.

---

## ⭐ Contribuição

Pull requests são bem-vindos!

---

## 📣 Autor

Se isso te ajudou, deixa uma ⭐ no repositório!