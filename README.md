# BCGenius
Repositório do grupo BCGenius (2024-2A-T03-ES11-G02)

# Inteli - Instituto de Tecnologia e Liderança 

<a href= "https://www.inteli.edu.br/"><img src="docs\assets\logo-inteli.webp" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>


<br>

# Projeto de estrutura e governança para análise de dados

## Grupo 2 - BCGenius

### 🚀 Integrantes
- <a href="https://www.linkedin.com/in/felipe-gomes-dev/">Felipe Gomes</a>
- <a href="https://www.linkedin.com/in/liviapcoutinho/">Livia Coutinho</a> 
- <a href="https://www.linkedin.com/in/lu%C3%ADsa-leite-681443230/">Luisa Leite</a> </br>
- <a href="https://github.com/themarcosf">Marcos Florencio</a> 
- <a href="https://www.linkedin.com/in/mike-mouadeb/">Mike Mouadeb</a>
- <a href="https://www.linkedin.com/in/raissa-sabino/">Raissa Sabino</a>
- <a href="https://www.linkedin.com/in/stefano-tinelli-b59515270/">Stefano Tinelli</a>

## Sumário
1. [Descrição]
   -  [Principais recursos]
   -  [Objetivos]
   -  [Metodologia]
2. [Principais entregas]
3. [Histórico de lançamentos]
4. [Como começar]
5. [Estrutura de pastas]

## 📜 Descrição

Este projeto visa desenvolver um ferramente de assistência de vendas personalizada para a empresa CosmeticCo, uma grande varejista de cosméticos. A solução inclui a construção de um pipeline de dados robusto e governança de dados, resultando em um DataApp que oferece visualizações personalizadas para gerentes e vendedores. As funcionalidades incluem projeções de vendas, recomendações de cross-sell, análise de margem de produtos e comparativos entre vendedores, com o objetivo de melhorar a performance e o engajamento da equipe de vendas.

**Principais recursos:**

- **Visualização personalizada:** Fornece visualizações de dados específicas para cada vendedor e gerente, facilitando o acesso à informações relevantes de vendas, desempenho e metas.

- **Projeção de vendas e remuneração:** Calcula e projeta o desempenho de vendas e a remuneração dos vendedores com base em modelos de remuneração variável, aumentando a transparência e o engajamento.

- **Recomendações de Cross-Sell:** Sugere produtos frequentemente comprados juntos, otimizando as estratégias de vendas e aumentando a receita.

- **Análise de margem de produtos:** Oferece insights sobre os produtos com maiores margens de lucro, auxiliando na tomada de decisões estratégicas de vendas.

- **Comparativos de desempenho:** Permite comparações entre o desempenho de diferentes vendedores e lojas, identificando oportunidades de melhoria e melhores práticas.

- **Simulador de remuneração:** Inclui uma funcionalidade que permite aos vendedores e gerentes prever a remuneração com base em diferentes cenários de vendas e metas.

- **Governança de dados:** Implementa uma estrutura de governança de dados, garantindo que todas as informações sejam processadas e armazenadas de forma segura e eficiente.

- **Pipeline de dados programático:** Um pipeline programático processa e estrutura diferentes bases de dados, garantindo que os dados estejam prontos para análise e visualização.

- **Documentação Completa:** Inclui uma documentação detalhada, com manual de utilização e manutenção da ferramenta, além da estrutura de governança e fluxos de dados.

**Objetivos**

- Melhorar a performance e o engajamento da equipe de vendas.

- Prover visualizações e insights acionáveis para tomadas de decisão.

**Metodologia**

- Utilizamos metodologias ágeis para o desenvolvimento do projeto, dividindo-o em sprints que permitem a entrega contínua de funcionalidades e feedback constante dos usuários.


## Principais entregas
- <a href="https://github.com/Inteli-College/2024-2A-T03-ES11-G02/blob/main/docs/template_arquitetura.md">Template da Arquitetura</a>
- <a href="https://github.com/Inteli-College/2024-2A-T03-ES11-G02/blob/main/docs/arquitetura_negocio.md"> Arquitetura de Negócios</a>
- <a href="https://github.com/Inteli-College/2024-2A-T03-ES11-G02/blob/main/docs/analise_exploratoria.Rmd">Análise Exploratória</a>
- <a href="https://github.com/Inteli-College/2024-2A-T03-ES11-G02/blob/main/docs/arquitetura_Dados.md">Arquitetura de Dados</a>
=======
## Como começar
**Para rodar o projeto, rode os seguintes comandos:**

### Usuarios para teste

**ADM**
 - Username: bob_a
 - Password: 456

**MNGR**
 - Username: alice_s
 - Password: 123

**Vendedor**
 - Username: charlie_d
 - Password: 789

### Para ver o front completo mockado: https://github.com/Inteli-College/2024-2A-T03-ES11-G02/tree/feature/streamlit-dataapp/src/frontend/front-mock

- acesse esta branch acima

```python
cd /src/frontend/front-mock
streamlit run main.py
```

### Caso não seja possivel rodar o projeto acesse o link para ver a versão integrada: https://drive.google.com/file/d/1yHkklw2R4SwI4SFO9mzPQ2UeX2nH23hL/view?usp=sharing


Adicionar .env com as variaveis nescessarias neste formato 
```python

# Data Directory
DATA_DIR=

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=

# Supabase Configuration
SUPABASE_DB=
SUPABASE_USER=
SUPABASE_PASSWORD=
SUPABASE_HOST=
SUPABASE_PORT=
SUPABASE_URL=

# ClickHouse connection parameters 
CLICKHOUSE_HOST=
CLICKHOUSE_PORT=
CLICKHOUSE_USER=
CLICKHOUSE_PASSWORD=
CLICKHOUSE_DB=

# RabbitMQ Configuration
RABBITMQ_HOST=

# Batch Processing Configuration
BATCH_SIZE=

TIMEOUT = 

```


## Rodar o Projeto Localmente

**Tenha a .env completa**

```python
docker-compose up --build
```


**ou**

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd src/backend/controller
python3 connection_controller.py
```

```python

cd src/frontend
streamlit run main.py
```




### Rodar Pipe de Cloud 

**Tenha a .env completa**
**Exporte suas credenciais AWS**
**Adicione sua chave .PEM no seguinte diretorio**

```python
/infra/terraform/
```
**depois**

```python
cd /infra/terraform/
terraform init
terraform plan
terraform apply
```

## 📁 Estrutura de pastas (a ser ajustada conforme estrutura de pastas final)

|--> assets<br>
  &emsp;| --> imagens <br>
  &emsp;| --> videos <br>
  &emsp;|--> readme.md<br>
|--> docs<br>
  &emsp;| --> apresentação <br>
  &emsp;| --> outros <br>
  &emsp;|--> readme.md<br>
|--> src<br>
  &emsp;|--> readme.md<br>
| readme.md<br>

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>assets</b>: aqui estão os arquivos relacionados a parte gráfica do projeto, ou seja, as imagens e links de vídeos que os representam (o logo do grupo pode ser adicionado nesta pasta).

- <b>docs</b>: aqui estão todos os documentos do projeto. Há também uma pasta denominada <b>outros</b> onde estão presentes outros documentos complementares, além de um arquivo README para o grupo registrar a localização de cada artefato.



## 🗃 Histórico de lançamentos

**1.0 — 16/08/2024 (Sprint I)**

* Análise exploratória e de governança de dados
* Template de arquitetura
* Arquitetura de negócio

**2.0 — 30/08/2024 (Sprint II)**

* Arquitetura de Dados e Informação
* Módulo de Ingestão e Transformação de Dados

**3.0 — 13/09/2024 (Sprint III)**

* Módulo de Processamento, Integração e Manipulação de Dados
* Documentação e Arquitetura Versão Incrementada
* Wireframe agnóstico de Dashboard

**4.0 — 27/09/2024 (Sprint IV)**

* Implantação do Pipeline na Nuvem
* Acesso, LGPD e Governança de Dados
* Dashboard (1ª versão)

**5.0 — 11/10/2024 (Sprint V)**

* Dashboard Final
* Documentação Incremental Versão Final com Governança de Dados

## Como começar
**Para rodar o projeto, rode os seguintes comandos:**

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📁 Estrutura de pastas

|--> assets<br>
  &emsp;| --> imagens <br>
  &emsp;| --> videos <br>
  &emsp;|--> readme.md<br>
|--> docs<br>
  &emsp;| --> apresentação <br>
  &emsp;| --> outros <br>
  &emsp;|--> readme.md<br>
|--> src<br>
  &emsp;|--> readme.md<br>
| readme.md<br>

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>assets</b>: aqui estão os arquivos relacionados a parte gráfica do projeto, ou seja, as imagens e links de vídeos que os representam (o logo do grupo pode ser adicionado nesta pasta).

- <b>docs</b>: aqui estão todos os documentos do projeto. Há também uma pasta denominada <b>outros</b> onde estão presentes outros documentos complementares, além de um arquivo README para o grupo registrar a localização de cada artefato.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto, incluindo backend e frontend se aplicáveis.

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="#">BCGenius</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="#">Inteli, Felipe Gomes, Livia Coutinho, Luisa Leite, Marcos Florêncio, Mike Mouadeb, Raíssa Sabino, Stefano Tinelli</a> is 
licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
