# Projetos Práticos de Engenharia de Dados

## 📋 Sobre

Esta pasta contém **projetos práticos completos** que demonstram conceitos avançados de engenharia de dados. Cada projeto é independente e pode ser estudado separadamente, mas seguem uma progressão lógica de complexidade e conceitos.

## 🎯 Objetivos de Aprendizado

Ao completar estes projetos, você será capaz de:

- Estruturar projetos de dados profissionais seguindo boas práticas
- Processar grandes volumes de dados eficientemente
- Construir APIs REST completas para aplicações de dados
- Implementar pipelines de qualidade de dados
- Realizar análises avançadas com SQL
- Construir pipelines de web scraping e extração de dados
- Modelar dados em ambientes cloud (Databricks)
- Criar agentes de IA para análise de dados

## 📁 Projetos Disponíveis

### Data Project Foundations
**Objetivo**: Aprender a estruturar projetos de dados profissionais com boas práticas, testes, documentação e CI/CD.

**Conceitos**: ETL pipelines, estruturação de projetos, pytest, mkdocs, Poetry, Git/GitHub

**Tecnologias**: Python, Pandas, pytest, mkdocs, Poetry

---

### Python Big Data Processing
**Objetivo**: Processar eficientemente 1 bilhão de linhas de dados comparando diferentes abordagens (Python puro, Pandas, Dask, Polars, DuckDB).

**Conceitos**: Big Data, processamento em memória, otimização de performance, streaming de dados

**Tecnologias**: Python, Pandas, Dask, Polars, DuckDB

---

### CRUD API Data Application
**Objetivo**: Construir uma aplicação completa com backend (FastAPI), frontend (Streamlit) e banco de dados (PostgreSQL).

**Conceitos**: APIs REST, ORM (SQLAlchemy), CRUD operations, Docker, arquitetura de aplicações

**Tecnologias**: FastAPI, Streamlit, PostgreSQL, SQLAlchemy, Pydantic, Docker

---

### Data Quality Engineering
**Objetivo**: Implementar pipelines de qualidade de dados com validação de schemas, contratos de dados e tratamento de erros.

**Conceitos**: Data Quality, Schema validation, Data contracts, Data profiling

**Tecnologias**: DuckDB, Python, Pydantic, Pandera

---

### SQL Advanced Analytics
**Objetivo**: Realizar análises avançadas de dados usando SQL com o banco de dados Northwind.

**Conceitos**: SQL avançado, Window Functions, CTEs, Views, Stored Procedures, análise de receitas, segmentação de clientes

**Tecnologias**: PostgreSQL, SQL

---

### Web Scraping NoSQL Pipelines
**Objetivo**: Construir pipelines de web scraping com armazenamento em bancos NoSQL (Redis e MongoDB).

**Conceitos**: Web Scraping, NoSQL databases, Caching, Message queues

**Tecnologias**: Python, BeautifulSoup, Scrapy, Redis, MongoDB

---

### PDF Data Extraction
**Objetivo**: Extrair dados de arquivos PDF armazenados no S3 usando triggers do SQS.

**Conceitos**: Extração de dados não-estruturados, Cloud services (AWS), Event-driven architecture

**Tecnologias**: Python, camelot-py, PyPDF2, AWS S3, AWS SQS, PostgreSQL

---

### Databricks Data Modeling
**Objetivo**: Modelar dados seguindo o padrão Bronze-Silver-Gold no Databricks com Delta Lake.

**Conceitos**: Data Lakehouse, Delta Lake, SCD Type 2, Dimensional modeling, Incremental processing

**Tecnologias**: Databricks, Delta Lake, Spark SQL, Unity Catalog

---

### Databricks AI Project
**Objetivo**: Construir agentes de IA para análise de dados usando LangChain, Vector Search e LLMs.

**Conceitos**: RAG (Retrieval Augmented Generation), Vector Search, LLMs, Text-to-SQL, MLflow

**Tecnologias**: Databricks, LangChain, Vector Search, OpenAI, MLflow, Streamlit

## 📦 Pré-requisitos Gerais

- Python 3.11+ instalado
- Git e GitHub configurados
- Conhecimento básico de Python
- Conhecimento básico de SQL (para projetos que utilizam)
- Docker instalado (para projetos que utilizam containers)

## 🔗 Conexões com a Formação

- **Antes de começar**: Complete os fundamentos em `02-fundamentos-dados/`
- **Durante os projetos**: Consulte `03-python-avancado-para-dados/` para aprofundar Python
- **Para SQL**: Use `04-sql-analytics-dbt-core/` como referência
- **Para orquestração**: Veja `04-workflow-orchestration-deploy-airflow/` após projeto 01

## 📖 Recursos Adicionais

- Cada projeto possui documentação detalhada em seu próprio README
- Vídeos das aulas disponíveis na plataforma Alpaclass
- Suporte através do grupo do WhatsApp da formação