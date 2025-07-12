# askmydocs

![Status](https://img.shields.io/badge/status-PoC-yellow)
![License](https://img.shields.io/badge/license-GPLv3-blue)

**askmydocs** é uma aplicação web open source que permite **buscar e conversar com documentos** em linguagem natural usando **IA com RAG** (retrieval-augmented generation).

O objetivo é transformar documentos estáticos em experiências interativas — com foco em **qualidade**, **privacidade** e **autonomia para desenvolvedores self-hosted**.

---

## Propósito

O askmydocs foi feito para quem precisa:

- Encontrar rapidamente trechos relevantes de documentos técnicos, jurídicos ou acadêmicos  
- Fazer perguntas em linguagem natural com respostas baseadas em **fontes reais**
- Obter respostas com **citação da origem**, garantindo rastreabilidade e confiança  
- Rodar tudo **localmente**, sem depender de serviços externos ou login em nuvem

---

## Stack Tecnológica

- **Backend:** FastAPI (Python)
- **Frontend:** React
- **Armazenamento vetorial:** Qdrant
- **LLM:** OpenAI (GPT-3.5 / GPT-4) por enquanto — será possível usar **qualquer LLM** (ex: Ollama, vLLM, modelos locais, etc.)

---

## Componentes

- [x] Upload e leitura de documentos (atualmente apenas `.pdf`)
- [x] Chunking inteligente dos textos com overlap
- [x] Geração de embeddings com Sentence Transformers
- [x] Armazenamento vetorial local com FAISS ou Qdrant
- [x] Recuperação top-K dos trechos mais relevantes
- [x] Geração de resposta com IA baseada no contexto
- [ ] Interface web com upload, chat e visualização com fonte citada

---

## Filosofia

- **100% open source:** Licenciado sob GPL-v3
- **Foco em desenvolvedores:** Fácil de rodar, entender e estender
- **Privacidade em primeiro lugar:** Nenhum dado é enviado para terceiros sem consentimento
- **Flexível:** Arquitetura preparada para plugar qualquer LLM, local ou na nuvem
