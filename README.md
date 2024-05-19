### Conversor de Planilhas Excel

Este projeto é uma aplicação web que permite converter dados em formato JSON para planilhas Excel de forma automatizada.
Utilizando Flask para o backend e HTML, JS e TailwindCSS para o frontend, o conversor de planilhas é fácil de usar e oferece uma interface moderna e responsiva.

#### Funcionalidades

- **Geração de Relatórios:** Converte dados JSON fornecidos pelo usuário em relatórios Excel.
- **Automatização:** Facilita o processo de criação de relatórios, economizando tempo e minimizando erros.

#### Tecnologias Utilizadas

- **Backend:** Flask
- **Frontend:** HTML, TailwindCSS, JavaScript
- **Manipulação de Dados:** Pandas
- **Geração de Excel:** Openpyxl

#### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)

#### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/kaykeeb3/excel-spreadsheet-converter.git
   cd excel-spreadsheet-converter
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

#### Executando a Aplicação

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

2. Abra seu navegador e acesse `http://localhost:5000`.

#### Uso

1. Cole os dados JSON no campo fornecido.
2. Clique no botão "Gerar Relatório".
3. O relatório Excel será gerado e baixado automaticamente.

#### Exemplo de Dados JSON

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

#### Melhorias Futuras

- Adicionar suporte para mais formatos de entrada e saída.
- Implementar autenticação de usuário.
- Adicionar funcionalidades de análise de dados e gráficos.

#### Vídeo de Apresentação

[Assista ao vídeo de apresentação do projeto](link_para_o_video)

#### Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
