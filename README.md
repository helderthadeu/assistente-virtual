# 🛡️ API de Modelagem de Ameaças STRIDE com Azure OpenAI

API desenvolvida com FastAPI para gerar modelos de ameaças usando o framework STRIDE e o Azure OpenAI, com base em texto descritivo e imagem (diagrama de arquitetura).

## 🚀 Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Crie um arquivo `.env` com:
```env
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_VERSION=...
AZURE_OPENAI_DEPLOYMENT_NAME=...
```

3. Rode a aplicação:
```bash
uvicorn main:app --reload
```

## 📥 Endpoint `/analisar_ameacas`

- **Método:** `POST`
- **Tipo:** `multipart/form-data`
- **Campos:**
  - `imagem`: diagrama da aplicação
  - `tipo_aplicacao`, `autenticacao`, `acesso_internet`, `dados_sensiveis`, `descricao_aplicacao`: texto

**Resposta:** JSON com modelo de ameaças e sugestões de melhoria.

## 🧾 Licença

MIT
