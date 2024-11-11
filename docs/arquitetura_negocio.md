# Arquitetura de Negócio

# Arquitetura de Negócio
1. [Governança de Dados](#Governança-de-Dados)
   - [Introdução à governança de dado](#Introdução-à-governança-de-dados)
   - [Importância da LGPD](#Importância-da-LGPD )
   - [Definição de acesso aos dados](#Definição-de-acesso-aos-dados )
   - [Processos de auditoria e compliance](#Processos-de-auditoria-e-compliance)
   - [Anonimização e pseudonimização dos dados](#Anonimização-e-pseudonimização-dos-dados)
   - [Treinamentos](#Treinamentos)
   - [Revisão e atualização contínua](#Revisão)
   - [Conclusão](#Conclusão)

2. [Medição de Qualidade dos Dados](#Medição-de-Qualidade-dos-Dados)
   - [Introdução à Qualidade dos Dados](#dados)
   - [Metodologia](#Metodologia)
   - [Processos de Qualidade](#Processamento)
   - [Monitoramento e Revisão](#Monitoramento)

## Governança de Dados 

## Introdução à governança de dados 

A governança de dados é um componente vital na administração moderna de dados empresariais, especialmente em um contexto regulatório rigoroso como o que enfrentamos hoje. Para a CosmeticCo, uma empresa com uma vasta rede de lojas e uma base de mais de 600 vendedores, estabelecer uma governança de dados robusta não é apenas uma questão de eficiência operacional, mas também de conformidade legal e proteção da reputação corporativa.

## Importância da LGPD 

A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) é a base legal que regulamenta o tratamento de dados pessoais no Brasil. No projeto de assistente de vendas para a CosmeticCo, a observância rigorosa da LGPD é crucial, pois o manuseio de dados pessoais de colaboradores, como informações de desempenho e remuneração, está diretamente envolvido. A conformidade com a LGPD não apenas evita penalidades severas, que podem chegar a 2% do faturamento da empresa, limitadas a R\$ 50 milhões por infração, mas também fortalece a confiança dos empregados e clientes na capacidade da empresa de proteger seus dados.

## Definição de acesso aos dados

Um dos princípios fundamentais da LGPD é a limitação de acesso aos dados com base no "need-to-know", ou seja, os dados devem ser acessíveis apenas para aqueles que realmente necessitam deles para desempenhar suas funções. Dentro do contexto trabalhado, temos então que:

-   **Vendedores e gerentes** terão acesso exclusivamente às suas próprias métricas de desempenho, como projeções de vendas e comparativos com outros vendedores, garantindo que informações sensíveis não sejam indevidamente expostas.
-   **Manutenção (TI e engenharia de dados)** terá acesso às bases de dados brutas e intermediárias para garantir a operação eficiente e segura do pipeline de dados. No entanto, esse acesso será monitorado e registrado para garantir a integridade e a segurança dos dados.
-   **Desenvolvedores (analistas de dados)** terão acesso a conjuntos de dados anonimizados ou pseudonimizados, permitindo análises detalhadas sem comprometer a privacidade dos titulares dos dados.

# 4. Políticas de segurança

As políticas de segurança adotadas no projeto são fundamentadas nos princípios de confidencialidade, integridade e disponibilidade (CIA triad), conforme descrito no NIST SP 800-53 e na ISO/IEC 27001.

-   **Confidencialidade**: Será implementada autenticação multifatorial (MFA) para todos os acessos aos sistemas de dados, conforme as melhores práticas recomendadas pelo NIST. Além disso, políticas de senha robustas e criptografia AES-256 para o armazenamento de dados sensíveis serão adotadas.
-   **Integridade**: Utilizaremos controles de versão e revisões para garantir que os dados permaneçam íntegros ao longo de todo o seu ciclo de vida. A integridade dos dados também será mantida através da implementação de checksums e hashes criptográficos, conforme recomendado pela ISO/IEC 27002.
-   **Disponibilidade**: A disponibilidade dos dados será assegurada através de sistemas de backup contínuo, utilizando soluções de armazenamento em nuvem e infraestrutura através da AWS. Planos de recuperação de desastres serão implementados, incluindo testes periódicos de failover para garantir a continuidade dos negócios em caso de incidentes.

## Processos de auditoria e compliance 

A conformidade com a LGPD será verificada por meio de auditorias regulares, que avaliarão a adesão às políticas de acesso, armazenamento e processamento de dados. Essas auditorias seguirão um cronograma anual e utilizarão frameworks reconhecidos, como o COBIT 5 (COBIT 5: a business framework for the governance and management of enterprise IT), para garantir que todos os aspectos de governança e compliance sejam abordados. Qualquer não conformidade deve ser rapidamente tratada através de um processo de correção documentado, garantindo que a empresa esteja sempre em linha com as exigências legais vigentes.

## Anonimização e pseudonimização dos dados 

Em conformidade com os artigos 12 e 13 da LGPD, dados pessoais serão anonimizados sempre que possível. Isso significa que os dados serão transformados de forma que não possam ser associados a um indivíduo específico sem o uso de informações adicionais, que serão mantidas separadamente e protegidas. Nos casos em que a anonimização completa não for viável, será aplicada a pseudonimização, que reduz significativamente os riscos associados ao tratamento de dados pessoais, limitando o impacto de eventuais violações de dados.

## Treinamentos 

A conscientização é uma parte crítica (e elementar) da governança de dados. É recomendado que a empresa implemente para todos envolvidos no projeto a participação em treinamentos regulares sobre a LGPD e as melhores práticas de manuseio de dados. Este treinamento deve incluir não apenas a legislação aplicável, mas também estudos de caso de violações de dados, reforçando a importância da conformidade e os riscos associados a falhas. Esses treinamentos devem ser obrigatórios e periódicos, com avaliações para garantir a compreensão e a aplicação correta das políticas.

#  Revisão e atualização contínua {#Revisão}

Em complementaridade ao tópico acima, governança de dados não é estática e deve ser adaptada continuamente para responder a novas ameaças, tecnologias e alterações regulatórias. A cada seis meses, a estrutura de governança será revisada, e atualizações serão implementadas conforme necessário. Esta revisão incluirá uma análise completa das políticas de acesso, segurança e compliance, bem como a adaptação às novas diretrizes regulamentares que possam surgir.

# Conclusão {#Conclusão}

A estrutura de governança de dados delineada aqui garante que o projeto de Estrutura e governança para análise de dados para a CosmeticCo esteja em plena conformidade com a LGPD, enquanto protege os dados sensíveis dos colaboradores e clientes da CosmeticCo. A abordagem adotada assegura que os dados sejam tratados de forma segura, ética e eficaz, promovendo a confiança em todos os níveis e suportando o sucesso a longo prazo do projeto.

## Medição de Qualidade dos Dados

#### **1. Introdução**

-   **Objetivo**:

    Nosso objetivo principal é garantir que as decisões tomadas neste projeto sejam precisas e confiáveis. Acreditamos que a qualidade dos dados é fundamental para o sucesso do nosso negócio. Por isso, dedicamos grande parte do nosso tempo e esforço para garantir que os dados que utilizamos sejam completos, consistentes e confiáveis. Ao garantir a qualidade dos dados, podemos tomar decisões mais assertivas, otimizar nossos processos e, consequentemente, alcançar melhores resultados.

    Dados de baixa qualidade podem levar a decisões erradas, resultando em perdas financeiras e no desengajamento dos colaboradores, prejudicando a eficácia das operações e a motivação da equipe. Garantir dados completos, consistentes, conformes, íntegros, precisos e atualizados é vital para manter a confiança no sistema, possibilitando uma análise mais acertada das vendas e do desempenho dos colaboradores. Isso, por sua vez, sustenta uma cultura de tomada de decisão informada e estratégica, que é essencial para o sucesso e a competitividade da organização.

    As práticas de qualidade dos dados aqui sitadas permitem que a organização identifique e corrija rapidamente qualquer discrepância, minimizando o impacto negativo e promovendo uma operação mais ágil e eficiente. Além disso, ao garantir que os dados sejam confiáveis, os gestores podem tomar decisões que reforçam o engajamento dos funcionários e melhoram os resultados de vendas, alinhando o desempenho dos colaboradores com os objetivos estratégicos da empresa.

#### **2. Metodologia** {#Metodologia}

Para garantir a confiabilidade e a precisão das nossas análises, estabelecemos as seguintes metas de qualidade dos dados:

-   **Completude:** Nossa meta é garantir que todos os dados essenciais para as nossas análises estejam presentes em nossos conjuntos de dados. Para isso, vamos monitorar constantemente a taxa de dados faltantes e implementar medidas para reduzir essa taxa ao mínimo.

-   **Consistência:** Nosso objetivo é assegurar que os dados sejam coerentes tanto internamente quanto entre diferentes fontes. Para alcançar isso, vamos identificar e corrigir qualquer inconsistência, como datas conflitantes ou valores duplicados.

-   **Conformidade:** Queremos garantir que os nossos dados sigam os padrões e formatos estabelecidos, como as normas da empresa ou as melhores práticas do setor. Nossa meta é manter uma taxa de conformidade superior a 95%.

-   **Integridade:** Nosso objetivo é manter a integridade das relações entre os dados, evitando erros de referência e inconsistências lógicas. Para isso, vamos realizar verificações regulares de integridade e implementar mecanismos de validação.

-   **Precisão:** Queremos garantir que os nossos dados reflitam a realidade de forma precisa. Para isso, vamos utilizar métodos estatísticos, como o cálculo do desvio padrão, para avaliar a precisão dos dados e identificar possíveis outliers.

-   **Atualidade:** Nossa meta é manter os dados sempre atualizados, garantindo que as nossas análises sejam relevantes. Para isso, vamos estabelecer um cronograma regular de atualização dos dados e implementar processos automatizados sempre que possível.

#### **3. Processos de Qualidade** {#Processamento}

-   Nós utilizaremos o processo de ETL descrito aqui para garantir que os dados extraídos de fontes como as tabelas CSV fornecidas pelo parceiro sejam corretamente integrados e transformados para se adequarem às necessidades de análise e modelagem. Este fluxo é essencial para garantir a qualidade e a utilidade dos dados, permitindo que os insights gerados sejam confiáveis e relevantes para a tomada de decisões na organização.

### **1. Extração (E)**

```         
Na etapa de extração, os dados são coletados a partir de diversas tabelas em formato Excel (CSV). Cada arquivo CSV contém um conjunto específico de dados, como informações de vendas, dados de clientes ou registros de produtos. A extração consiste em carregar esses arquivos CSV para dentro do ambiente de análise, onde eles serão processados.

**Subetapas:**
```

-   **Leitura dos Arquivos CSV**: Utilização de scripts para ler os arquivos CSV e convertê-los em dataframes no ambiente de análise.

-   **Validação dos Dados Extraídos**: Verificação de integridade dos arquivos, garantindo que todos os dados foram corretamente extraídos e que não há problemas como arquivos corrompidos ou ausentes.

### **2. Transformação (T)**

```         
Na transformação, os dados brutos extraídos são processados para torná-los mais adequados para a análise ou para uso em modelos de machine learning. Esta é uma fase crítica onde os dados são limpos, transformados e preparados.
```

**Subetapas:**

-   **Tratamento de Dados Nulos**: Identificação e remoção ou imputação de valores nulos presentes nos dados.

-   **Tratamento de Outliers**: Identificação e tratamento de valores extremos que possam distorcer a análise.

-   **Seleção de Variáveis**: Identificação e separação das variáveis importantes que serão usadas na análise ou no modelo.

-   **Conversão de Tipos de Dados**: Garantir que os dados estão nos formatos corretos, por exemplo, converter datas para o formato de data correto ou transformar variáveis categóricas em fatores. -

-   **Integração de Dados**: Combinação de diferentes datasets (tabelas CSV) em um único dataset coerente, que pode envolver a junção de tabelas com base em chaves comuns.

### **3. Carga (L)**

```         
Na etapa de carga, o dataset transformado e limpo é carregado no modelo de análise ou de machine learning. Esta etapa envolve a inserção dos dados em um ambiente onde eles possam ser utilizados para previsões, análises descritivas, ou outras aplicações.
```

**Subetapas:**

-   **Carregamento no Modelo**: Inserção dos dados processados no modelo de machine learning ou em ferramentas de análise.

-   **Validação Pós-Carga**: Verificação para garantir que os dados foram carregados corretamente e que estão prontos para uso.

-   **Documentação e Auditoria**: Registro de todas as transformações realizadas, garantindo que o processo possa ser revisado ou reproduzido no futuro.

```{r}
   knitr::include_graphics("../assets/etl.png")
```

### **4. Monitoramento e Revisão** {#Monitoramento}

Para monitorar a qualidade dos dados em tempo real e garantir que os logs coletados sejam úteis para manutenção preventiva e análise de qualidade, nós usaremos funções fornecidas nas ferramentas como o **Supabase** com **Grafana** o **ClickHouse** que é crucial. Vamos explorar como a monitoria funciona e os processos envolvidos:

### **1. Supabase**

Escolhemos o Supabase como nossa plataforma de banco de dados por sua flexibilidade e facilidade de uso. Ele nos permite armazenar os logs de forma estruturada e organizada, facilitando a consulta e a análise. Aqui estão alguns pontos importantes:

-   **Armazenamento de Logs:** Utilizamos o Supabase para armazenar todos os logs gerados pelo nosso sistema, desde eventos de usuários até métricas de performance. Dessa forma, temos um histórico completo das atividades e podemos identificar padrões e tendências.

-   **Triggers e Funções Personalizadas:** Criamos triggers e funções personalizadas no Supabase para automatizar tarefas como a detecção de anomalias e o envio de alertas. Por exemplo, configuramos um trigger para notificar a equipe de dados sempre que houver um pico inesperado no número de erros.

-   **Integração com Ferramentas de Visualização:** Integramos o Supabase com o Grafana para criar dashboards personalizados e visualizar os dados de forma mais intuitiva. Isso nos permite monitorar a qualidade dos dados em tempo real e identificar problemas rapidamente.

### **2. ClickHouse**

ClickHouse é um sistema de gerenciamento de banco de dados columnar projetado para consultas analíticas de alta performance. Ele será utilizado como um data lake devido à sua capacidade de lidar com grandes volumes de dados em tempo real. No nosso contexto de monitoramento, o ClickHouse desempenha um papel crucial nas seguintes áreas:

-   **Armazenamento e Análise de Logs:** Utilizamos o ClickHouse como um data lake para armazenar todos os nossos logs. Isso nos permite realizar análises históricas e identificar tendências de longo prazo.
-   **Detecção de Anomalias:** Através de consultas SQL otimizadas, identificamos rapidamente anomalias nos dados, como valores outliers ou padrões inesperados.
-   **Relatórios e Dashboards:** Criamos relatórios periódicos e dashboards interativos no ClickHouse e utilizando o grafana para acompanhar a qualidade dos dados e tomar decisões mais informadas.

```{r}
  knitr::include_graphics("../assets/Dashboards.png")
```

### **Processos Utilizados para Monitorar a Qualidade dos Dados**

Para garantir a qualidade dos dados, seguimos um processo rigoroso que envolve:

-   **Coleta de Logs:** Coletamos logs de diversas fontes, como bancos de dados, sistemas operacionais e aplicações.

-   **Armazenamento:** Armazenamos os logs no Supabase e no ClickHouse.

-   **Análise:** Realizamos análises exploratórias e estatísticas nos dados para identificar padrões e anomalias.

-   **Detecção de Anomalias:** Utilizamos técnicas de detecção de anomalias para identificar valores discrepantes ou comportamentos inesperados.

-   **Alertas:** Configuramos triggers para notificar a equipe sobre problemas de qualidade dos dados.

-   **Relatórios:** Geramos relatórios periódicos para acompanhar a evolução da qualidade dos dados ao longo do tempo.

```{r}
knitr::include_graphics("../assets/fluxo.png")
```
