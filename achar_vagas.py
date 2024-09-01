from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

navegador = webdriver.Chrome()
navegador.get("https://www.empregare.com/pt-br/vagas?query=software&localidade=&ordenacao=DataAtualizacao")

empresas = navegador.find_elements(By.XPATH, "//p[@class='text-truncate card-vaga-empresa']")

datas_publicacao = navegador.find_elements(By.CLASS_NAME, 'texto-data-card')

cargos = navegador.find_elements(By.XPATH, "//p[@class='fw-bold fs-4 titulo-vaga text-truncate']")

descricoes = navegador.find_elements(By.XPATH, "//p[@class='d-none d-lg-flex']/small")

cidades = navegador.find_elements(By.XPATH, "//p[@class='card-cidades ']")

tipos_de_trabalhos = navegador.find_elements(By.XPATH, "//div[@class='col gx-3 align-self-center']/small[@class='fw-normal']")


link_vagas = navegador.find_elements(By.XPATH, "//a[@class='text-decoration-none']")



planilha = openpyxl.load_workbook('vagas.xlsx')

pagina_planilha = planilha['plan1']

for empresa, data, cargo, descricao, cidade, trabalho, link in zip(empresas, datas_publicacao, cargos, descricoes, cidades, tipos_de_trabalhos, link_vagas):
    empresas_ok = empresa.text
    data_ok = data.text
    cargo_ok = cargo.text
    descricao_ok = descricao.text
    cidade_ok = cidade.text
    trabalho_ok = trabalho.text
    links_ok = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    pagina_planilha.append([empresas_ok, data_ok, cargo_ok, descricao_ok, cidade_ok, trabalho_ok, links_ok, data_atual])
planilha.save('vagas.xlsx')