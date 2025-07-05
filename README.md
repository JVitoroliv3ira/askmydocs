# askmydocs

**askmydocs** é uma aplicação web open source que permite buscar e conversar com documentos em linguagem natural utilizando inteligência artificial (IA) com RAG (retrieval-augmented generation).

Seu objetivo é transformar documentos estáticos em experiências interativas e acessíveis — preservando a **privacidade**, **qualidade** e com foco em desenvolvedores que preferem soluções **self-hosted**.

---

## Propósito

O askmydocs foi criado para quem precisa:

- Buscar rapidamente trechos relevantes de documentos técnicos, jurídicos ou acadêmicos
- Fazer perguntas em linguagem natural e receber respostas baseadas em fontes reais
- Citar a origem dos dados para garantir rastreabilidade e confiança
- Ter controle total sobre os dados — sem depender de serviços externos ou contas

---

## Stack

- **Backend:** FastAPI (Python)
- **Banco de dados vetorial:** PostgreSQL + pgvector
- **Frontend:** React com TypeScript (Vite ou Next.js)
- **LLM:** OpenAI (GPT-3.5 / GPT-4), com suporte futuro a vLLM e modelos locais

---

## Componentes planejados

- Upload de documentos (`.pdf`, `.docx`, `.txt`, etc.)
- Extração e chunking dos textos
- Geração de embeddings e armazenamento vetorial
- Busca top-K dos trechos mais relevantes
- Montagem de prompt e chamada ao LLM
- Interface web com upload, chat e visualização com fonte citada

---

## Filosofia

- **Código aberto:** licenciado sob GPL-v3
- **Foco em desenvolvedores:** fácil de rodar, estender e contribuir
- **Independência:** sem vendor lock-in ou dependência de serviços fechados
