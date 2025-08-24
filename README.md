# 🤖 AutoU-MailAI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Sistema Inteligente de Classificação e Resposta Automática de Emails**

*Transforme sua gestão de emails com IA avançada e interface intuitiva*

[🚀 Demo](#-demonstração) • [📖 Documentação](#-documentação) • [⚡ Instalação](#-instalação-rápida) • [🤝 Contribuir](#-contribuição)

</div>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias-utilizadas)
- [Instalação Rápida](#-instalação-rápida)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [API Documentation](#-api-documentation)
- [Configuração Avançada](#-configuração-avançada)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🎯 Sobre o Projeto

**AutoU-MailAI** é um sistema inteligente de classificação de emails que utiliza técnicas avançadas de Processamento de Linguagem Natural (NLP) para categorizar automaticamente emails como **Produtivos** ou **Improdutivos**, além de gerar respostas automáticas contextualizadas.

### 🎯 Objetivo

Automatizar a triagem de emails corporativos, aumentando a produtividade e reduzindo o tempo gasto com emails irrelevantes.

### 🏆 Diferenciais

- **🧠 IA Própria**: Algoritmo de classificação desenvolvido internamente
- **📊 Analytics**: Dashboard com métricas detalhadas de performance
- **🔄 Aprendizado**: Sistema evolui com base no histórico de classificações
- **🌐 Interface Moderna**: Design responsivo e intuitivo
- **📁 Multi-formato**: Suporte a .txt, .pdf e entrada direta de texto

## ✨ Funcionalidades

### 🔍 Classificação Inteligente
- Análise semântica avançada de conteúdo
- Detecção de sentimento (positivo, negativo, neutro)
- Identificação de palavras-chave contextuais
- Score de confiança para cada classificação

### 🤖 Resposta Automática
- Geração de respostas contextualizadas
- Templates personalizáveis por categoria
- Análise de tom e formalidade
- Sugestões de ação baseadas no conteúdo

### 📊 Dashboard Analytics
- Estatísticas em tempo real
- Histórico completo de classificações
- Métricas de precisão e recall
- Exportação de relatórios

### 🛠️ Recursos Técnicos
- Base de dados SQLite integrada
- API RESTful para integrações
- Sistema de logs detalhado
- Configuração flexível via arquivo

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+** - Linguagem principal
- **Flask 2.0+** - Framework web
- **SQLite** - Base de dados
- **PyPDF2** - Processamento de PDFs
- **NLTK** - Processamento de linguagem natural

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna com Flexbox/Grid
- **JavaScript ES6+** - Interatividade e AJAX
- **Responsive Design** - Compatível com todos os dispositivos

### Arquitetura
- **MVC Pattern** - Separação clara de responsabilidades
- **RESTful API** - Endpoints padronizados
- **Modular Design** - Componentes reutilizáveis

## ⚡ Instalação Rápida

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 1. Clone o Repositório
\`\`\`bash
git clone https://github.com/ViniiciusTech/AutoU-MailAI.git
cd AutoU-MailAI
\`\`\`

### 2. Instale as Dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Execute a Aplicação
\`\`\`bash
cd app
python main.py
\`\`\`

### 4. Acesse a Aplicação
Abra seu navegador e acesse: **http://localhost:5000**

## 🚀 Como Usar

### 📝 Classificação por Texto
1. Acesse a aba **"Texto"**
2. Cole o conteúdo do email
3. Clique em **"Classificar Email"**
4. Visualize o resultado e resposta sugerida

### 📎 Classificação por Arquivo
1. Acesse a aba **"Upload"**
2. Selecione um arquivo (.txt ou .pdf)
3. Clique em **"Classificar Email"**
4. Analise os resultados detalhados

### 📊 Visualizar Histórico
- Acesse a seção **"Histórico de Emails Processados"**
- Visualize todas as classificações anteriores
- Analise métricas de performance

## 📁 Estrutura do Projeto

\`\`\`
AutoU-MailAI/
├── 📁 app/                     # Aplicação principal
│   ├── 📁 static/              # Arquivos estáticos
│   │   ├── 🎨 style.css        # Estilos CSS
│   │   └── ⚡ script.js        # JavaScript
│   ├── 📁 templates/           # Templates HTML
│   │   └── 🌐 index.html       # Interface principal
│   ├── 🐍 main.py              # Servidor Flask
│   ├── 🧠 classifier.py        # Lógica de classificação
│   ├── 🤖 responder.py         # Gerador de respostas
│   └── 🔧 utils.py             # Utilitários e BD
├── 📁 data/                    # Base de dados
│   └── 🗄️ emails.db           # SQLite database
├── 📋 requirements.txt         # Dependências Python
└── 📖 README.md               # Documentação
\`\`\`

## 🔌 API Documentation

### Endpoints Disponíveis

#### `POST /classify`
Classifica um email e retorna resultado detalhado.

**Request:**
\`\`\`json
{
  "email_content": "Conteúdo do email aqui...",
  "file_type": "text" // ou "pdf"
}
\`\`\`

**Response:**
\`\`\`json
{
  "category": "Produtivo",
  "confidence": 0.85,
  "sentiment": "positivo",
  "keywords": ["projeto", "reunião", "trabalho"],
  "suggested_response": "Resposta sugerida...",
  "processing_time": 0.23
}
\`\`\`

#### `GET /stats`
Retorna estatísticas do sistema.

**Response:**
\`\`\`json
{
  "total_emails": 150,
  "productive": 89,
  "unproductive": 61,
  "accuracy": 0.92,
  "avg_confidence": 0.87
}
\`\`\`

## ⚙️ Configuração Avançada

### Personalizar Palavras-chave
\`\`\`python
# Em classifier.py
PRODUCTIVE_KEYWORDS = [
    'projeto', 'reunião', 'trabalho', 'cliente',
    'suas_palavras_personalizadas'  # Adicione aqui
]
\`\`\`

### Configurar Respostas Automáticas
\`\`\`python
# Em responder.py
PRODUCTIVE_RESPONSES = [
    "Obrigado pelo seu email. Vou analisar e retornar em breve.",
    "Sua_resposta_personalizada_aqui"
]
\`\`\`

### Variáveis de Ambiente
\`\`\`bash
# .env (opcional)
FLASK_ENV=development
DATABASE_PATH=data/emails.db
LOG_LEVEL=INFO
\`\`\`

## 🧪 Testes

Execute os testes automatizados:
\`\`\`bash
python -m pytest tests/
\`\`\`

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Veja como contribuir:

### 1. Fork o Projeto
\`\`\`bash
git fork https://github.com/ViniiciusTech/AutoU-MailAI.git
\`\`\`

### 2. Crie uma Branch
\`\`\`bash
git checkout -b feature/nova-funcionalidade
\`\`\`

### 3. Commit suas Mudanças
\`\`\`bash
git commit -m "feat: adiciona nova funcionalidade"
\`\`\`

### 4. Push para a Branch
\`\`\`bash
git push origin feature/nova-funcionalidade
\`\`\`

### 5. Abra um Pull Request

### 📋 Guidelines de Contribuição
- Siga o padrão de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use commits semânticos (feat, fix, docs, etc.)


## 👨‍💻 Autor

**Vinícius Tech**
- GitHub: [@ViniiciusTech](https://github.com/ViniiciusTech)
- LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/marcos-vinicius-isteilo/)

## 🙏 Agradecimentos

- Comunidade Python pela excelente documentação
- Contribuidores do projeto Flask
- Todos que testaram e deram feedback

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela!**

**🐛 Encontrou um bug? [Reporte aqui](https://github.com/ViniiciusTech/AutoU-MailAI/issues)**

**💡 Tem uma ideia? [Sugira aqui](https://github.com/ViniiciusTech/AutoU-MailAI/discussions)**

</div>
