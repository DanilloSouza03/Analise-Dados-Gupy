## 🚀 Desafio - Driva

### Análise de Vagas de Dados na Plataforma Gupy 🎯

Nesta análise, explorei um conjunto de 587 vagas disponíveis na plataforma Gupy, todas relacionadas à área de dados. Os dados foram obtidos por meio de web scraping feito na data (28/08/2023), por meio deste arquivo. [Web Scraping](https://github.com/DanilloSouza03/Analise-Dados-Gupy/blob/main/getData.py)

<details>
  <summary><b>📁 Estrutura do Repositório</b></summary>

 Dentro deste repositório, você encontrará os seguintes arquivos e pastas:
- Arquivo "getData.py"
  - Contém o script feito para realizar o web scraping na plataforma da Gupy.
- Arquivo “base_dados_vagas.csv”
	- Contém os dados em obtidos pela raspagem em .csv.
- Arquivo “analise_vagas_gupy.ipynb”
	- Contém o código de como foram feitas as análises.
- Pasta “graficos”
	- Esta pasta contém os gráficos da análise.  
- .gitattributes
	- Arquivo default para criação do repositório.
- README.md
	- Arquivo com informações para entender o objetivo do repositório.
- LICENSE
	- Informações da licença do repositório.

</details>

<details>
  <summary><b>💻 Tecnologias Usadas </b></summary>

 Para este projeto foram utilizados as seguintes tecnologias para certos fins
- **Python** (linguagem de programação).
  - Utilizada para escrever o script de web scraping e análises.
- **Selenium** (framework de automação de testes).
	- Utilizado para automatizar a interação com a página da plataforma Gupy.
- **Pandas** (biblioteca Python para análise de dados).
	- Utilizada para a limpeza, organização e análise dos dados obtidos.
- **BeautifulSoup** (biblioteca Python para análise de arquivos HTML e XML).
	- Utilizada para extrair informações específicas das páginas web.
- **Unidecode** <small>(biblioteca Python para conversão de caracteres acentuados)</small>
  -  Utilizada para lidar com a conversão de caracteres acentuados em caracteres ASCII.
- **Matplolib** (biblioteca Python para visualização de dados).
  - Utilizada para criar visualizações gráficas dos dados analisados.

</details>

#### Distribuição de Vagas por Estado

Ao analisar os **10 estados com o maior número de vagas**, constatamos que a região Sudeste domina as ofertas de emprego, com São Paulo liderando, seguido por Rio de Janeiro e Minas Gerais. 

<p align="left">
  <img src="graficos/Top10EstadosVagas.png" alt="Gráfico Vagas por Estado">
</p>

#### Tipos de Contratos Mais Comuns

Em uma base de 587 vagas, notamos que mais de **400 delas são para cargos efetivos**, isso sinaliza uma alta demanda  por **profissionais qualificados e de longo prazo.** Além disso, identificamos um grande número de vagas com contratos de **Banco de Talentos e Estágio**, indicando que as empresas estão investindo em **novos talentos e em formar equipes diversificadas.**

<p align="left">
  <img src="graficos/VagasTipoContrato.png" alt="Gráfico Tipos de Contratos Mais Comuns">
</p>

#### Vagas para Pessoas com Deficiência (PcD)

Do total de vagas analisadas, **77,3%** são direcionadas a pessoas com deficiência. É importante mencionar que os 22,7% restantes têm dados não informados, o que pode indicar uma oportunidade para melhorar a coleta de informações nessa área. 

<p align="left">
  <img src="graficos/PercentualdeVagasparaPcD.png" alt="Gráfico Vagas para Pessoas com Deficiência">
</p>

Entre as vagas remotas, 82% também oferecem oportunidades para PcD, demonstrando um esforço para deixar mais acessiviel.

<p align="left">
  <img src="graficos/PerncentualdeVagasRemotaparaPcD.png" alt="Gráfico Vagas Remotas para Pessoas com Deficiência">
</p>

#### Modalidade de Trabalho

Com relação à modalidade de trabalho, 67,8% das vagas são presenciais e 32,2% são remotas. Essa distribuição revela a preferência das empresas por terem colaboradores que possam estar presentes fisicamente em seus locais de trabalho.

<p align="left">
  <img src="graficos/DistribuicaoporModalidade.png" alt="Gráfico Modalidade de Trabalho">
</p>

#### Top 10 Empresas com Mais Oportunidades

Ao analisar as empresas com mais vagas, o **Itaú** lidera, seguido por **NAVA** e **Stefanini**. Essas empresas demonstram um compromisso contínuo em oferecer oportunidades na área de dados.

<p align="left">
  <img src="graficos/Top10Empresas.png" alt="Gráfico Top 10 Empresas com mais vagas">
</p>

#### Top 10 Cidades com Mais Vagas Presenciais

São Paulo e Rio de Janeiro surgem como as principais cidades com vagas presenciais, refletindo o cenário econômico e populacional dessas regiões. Observamos que há uma porção significativa de dados não informados, sugerindo a importância de melhorias no preenchimento de informações por parte das empresas e/ou plataforma.

<p align="left">
  <img src="graficos/Top10Cidades.png" alt="Gráfico ">
</p>

Esta análise oferece insights valiosos para candidatos em busca de oportunidades de emprego e empresas que desejam entender as tendências do mercado.

<hr>
<p align="center">
Desenvolvido por Danillo Souza.
</p>
