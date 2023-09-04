# Bibliotecas usadas
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

# Função para realizar a rolagem até o final da página
def scroll_ate_final(driver):
    atual_altura = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Rola até o final da página atual
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(1)
        
        # Pega a altura depois da página ser rolada
        nova_altura = driver.execute_script("return document.body.scrollHeight")
        
        # Verifica se chegou ao final 
        if nova_altura == atual_altura:
            break
        
        atual_altura = nova_altura

# Função para extrair os dados de cada vaga
def extrair_dados_vagas(vaga):
    # extrai os dados contido em cada vaga 
    empresa = vaga.find("p", class_="cQyvth").text
    cargo = vaga.find("h2", class_="XNNQK").text
    dados_spans = vaga.find_all("span", class_="cezNaf")  
    localizacao = dados_spans[0].text
    modalidade = dados_spans[1].text
    contrato = dados_spans[2].text

    # Verifica se tem 4 itens de dados, se tiver adiciona o conteúdo
    if len(dados_spans) >= 4:
        pcd = dados_spans[3].text
    else:
        pcd = "Não informado"  

    # Adiciona somente os 10 ultimos caracteres que por padrão é a data xx/xx/xxxx
    data = vaga.find("p", class_="inqtnx").text[-10:]

    return {
        'empresa': empresa,
        'cargo': cargo,
        'localizacao': localizacao,
        'modalidade': modalidade,
        'contrato': contrato,
        'pcd': pcd,
        'data': data
    }

# Função principal para buscar e salvar os dados
def main():
    driver = webdriver.Chrome()
    
    # URL da página + termo de pesquisa
    value_term = "Dados"
    url = f"https://portal.gupy.io/job-search/term={value_term}"
    
    # Abre a pag da web com o url definido na variavel
    driver.get(url)
    
    # Chama a função para rolar a página até o final
    scroll_ate_final(driver)
    
    time.sleep(2)
    
    # Armazena a página que foi rolada até o final, e traz para ser tratado pelo bs4
    page_source = driver.page_source
    site = BeautifulSoup(page_source, 'html.parser')
    
    # Criando um dicionário para armazenar os dados
    dict_vagas = {
        'empresa':[],
        'cargo':[],
        'localizacao':[],
        'modalidade':[],
        'contrato':[],
        'pcd':[],
        'data':[]
    }

    # Pegando a lista onde tem as vagas
    cards_vagas = site.find('ul', class_="zVzmE")

    # Pegando todas vagas da lista de vagas
    card_vagas = cards_vagas.find_all('li')

    # Percorrendo vaga a vaga
    for vaga in card_vagas:
        vaga_data = extrair_dados_vagas(vaga)
        # Coloca os dados de cada vaga no dict
        for key, value in vaga_data.items():
            dict_vagas[key].append(value)

    # Transforma o dict preenchido em um df
    df = pd.DataFrame(dict_vagas)
    
    # Salva esse df em csv, usando o UTF-8 como linguagem, separando por ";" e sem index
    df.to_csv("base_dados_vagas.csv", encoding='utf-8', sep=';', index=False)
    
    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    main()