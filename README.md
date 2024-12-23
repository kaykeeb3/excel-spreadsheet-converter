# Conversor de Planilhas Excel

Este projeto é uma aplicação web desenvolvida para converter dados em formato **JSON** para planilhas **Excel** de maneira automatizada. Utilizando **Flask** para o backend e **HTML**, **JavaScript** e **TailwindCSS** para o frontend, a ferramenta proporciona uma experiência simples e intuitiva para a conversão de dados, economizando tempo e minimizando erros ao gerar relatórios Excel.

## Funcionalidades

- **Geração de Relatórios**: Converte dados JSON fornecidos pelo usuário em relatórios Excel personalizados.
- **Automatização**: Facilita a criação de relatórios a partir de dados estruturados, garantindo agilidade e precisão no processo.
- **Interface Intuitiva e Responsiva**: Desenvolvido com tecnologias modernas para garantir uma experiência de usuário otimizada em qualquer dispositivo.

## Tecnologias Utilizadas

- **Backend**: Flask (framework Python para APIs)
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Manipulação de Dados**: Pandas (para processamento de dados)
- **Geração de Excel**: Openpyxl (para criação e manipulação de arquivos Excel)

## Pré-requisitos

Antes de iniciar, você precisa ter os seguintes pré-requisitos instalados:

- **Python 3.x**
- **Pip** (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/kaykeeb3/excel-spreadsheet-converter.git
   cd excel-spreadsheet-converter
   ```

2. Crie e ative um ambiente virtual:

   Para Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   Para Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Executando a Aplicação

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

2. Abra o navegador e acesse `http://localhost:5000` para usar a aplicação.

## Uso

1. Cole os dados **JSON** no campo fornecido na interface.
2. Clique no botão **"Gerar Relatório"**.
3. O arquivo Excel será gerado automaticamente e será baixado para o seu dispositivo.

### Exemplo de Dados JSON

Aqui está um exemplo de como os dados JSON devem ser estruturados para gerar um relatório:

```json
[
  {
    "ID": 1,
    "Nome do cliente": "Alice",
    "Nome do cliente que chamou no WhatsApp": "João",
    "Nome da empresa": "Empresa A",
    "Duvida do cliente": "Produto X",
    "Horário que chamou": "10:00",
    "Tempo médio de resposta": "15 minutos",
    "Data": "2024-05-20",
    "Dia: .. Atendimento do dia": "Segunda-feira"
  },
  {
    "ID": 2,
    "Nome do cliente": "Bob",
    "Nome do cliente que chamou no WhatsApp": "Maria",
    "Nome da empresa": "Empresa B",
    "Duvida do cliente": "Serviço Y",
    "Horário que chamou": "11:30",
    "Tempo médio de resposta": "20 minutos",
    "Data": "2024-05-20",
    "Dia: .. Atendimento do dia": "Segunda-feira"
  },
  {
    "ID": 3,
    "Nome do cliente": "Charlie",
    "Nome do cliente que chamou no WhatsApp": "Pedro",
    "Nome da empresa": "Empresa C",
    "Duvida do cliente": "Produto Z",
    "Horário que chamou": "14:45",
    "Tempo médio de resposta": "10 minutos",
    "Data": "2024-05-21",
    "Dia: .. Atendimento do dia": "Terça-feira"
  }
]
```

## Melhorias Futuras

- **Suporte a Mais Formatos**: Implementação de suporte para importar e exportar outros formatos de dados (CSV, XML, etc.).
- **Autenticação de Usuários**: Implementação de autenticação e autorização de usuários para controle de acesso aos relatórios.
- **Análise de Dados**: Adição de funcionalidades para análise e visualização de dados com gráficos e relatórios dinâmicos.

## Contribuindo

Contribuições são sempre bem-vindas! Para contribuir, siga os passos abaixo:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-feature`).
3. Realize suas alterações e faça o **commit** (`git commit -am 'Adicionei uma nova feature'`).
4. Envie sua branch para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um **Pull Request** com uma descrição clara das alterações realizadas.
