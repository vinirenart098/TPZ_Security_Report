import requests
import csv
from urllib.parse import urlparse
import socket
from datetime import datetime

# Substitua pela nova chave de API
API_KEY = "at_32xqp7s2SknIOliLi2RIsLYVs6MjB"

# Lista completa de URLs para análise
urls = [
    "https://www.youtube.com/watch?v=qSWgqfIpsnk",
    "https://www.youtube.com/watch?v=MlFRR1-JYn4",
    "https://www.youtube.com/",
    "https://web.telegram.org/",
    "https://www.google.com/maps/",
    "https://outlook.live.com/mail/0/",
    "https://www.linkedin.com/feed/",
    "https://www.linkedin.com/analytics/profile-views/",
    "https://www.linkedin.com/notifications/",
    "https://www.delegaciaeletronica.policiacivil.sp.gov.br/ssp-de-cidadao/pages/comunicar-ocorrencia",
    "https://www.delegaciaeletronica.policiacivil.sp.gov.br/ssp-de-cidadao/home",
    "https://www.google.com/search?q=como+agir+em+caso+de+golpe+na+internet",
    "https://www.google.com/search?q=boletim+ocorrencia",
    "https://bancotpz.com.br/pagamentos",
    "https://bancotpz.com.br/extrato",
    "https://bancotpz.com.br/",
    "http://bancotpzatualiza.apps.dnofd.com/static/index.html",
    "http://bancotpzatualiza.apps.dnofd.com/",
    "https://www.infomoney.com.br/mercados/latam-tem-plano-de-recuperacao-judicial-aprovado-pela-justica-americana/",
    "https://www.infomoney.com.br/ultimas-noticias/",
    "https://www.bcb.gov.br/estabilidadefinanceira/fechamentodolar",
    "https://g1.globo.com/ms/mato-grosso-do-sul/noticia/2024/06/19/enfermeira-chega-para-trabalhar-e-encontra-filho-de-20-anos-morto-por-acidente-de-transito.ghtm",
    "https://g1.globo.com/mundo/noticia/2024/06/19/eleicoes-na-franca-macron-perde-maioria-no-legislativo-com-derrota-historica-e-avanco-da-esquerda-e-direita-radical.ghtml"
]

def extract_domains(urls):
    """
    Extrai os domínios de uma lista de URLs.
    """
    domains = set()
    for url in urls:
        parsed_url = urlparse(url)
        domains.add(parsed_url.netloc)
    return list(domains)

def get_ip(domain):
    """
    Obtém o endereço IP do domínio via DNS.
    """
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return "N/A"

def get_whois_data(domain):
    """
    Consulta a API WhoisXML para obter informações WHOIS de um domínio.
    """
    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    params = {
        "apiKey": API_KEY,
        "domainName": domain,
        "outputFormat": "JSON",
        "da": 1  # Verifica disponibilidade do domínio
    }
    try:
        response = requests.get(url, params=params)
        print(f"Consultando domínio: {domain}")
        print(f"Status HTTP: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            record = data.get("WhoisRecord", {})
            return {
                "domain": domain,
                "registrar": record.get("registrarName", "N/A"),
                "creation_date": format_date(record.get("createdDate")),
                "expiration_date": format_date(record.get("expiresDate")),
                "updated_date": format_date(record.get("updatedDate")),
                "name_servers": ", ".join(record.get("nameServers", [])),
                "status": record.get("status", "N/A"),
                "registrant": record.get("registrant", {}).get("organization", "N/A"),
                "ip_address": get_ip(domain),
                "availability": record.get("domainAvailability", "N/A")
            }
        else:
            return {"domain": domain, "error": f"HTTP Error {response.status_code}"}
    except Exception as e:
        return {"domain": domain, "error": str(e)}

def format_date(date_str):
    """
    Converte datas do formato ISO para DD/MM/AAAA.
    """
    if date_str:
        try:
            date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return date_obj.strftime("%d/%m/%Y")
        except Exception:
            return date_str
    return "N/A"

def save_to_csv(data, filename="whois_results.csv"):
    """
    Salva os resultados em um arquivo CSV.
    """
    keys = data[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Extrai os domínios do histórico
domains = extract_domains(urls)

# Consulta WHOIS para cada domínio
results = [get_whois_data(domain) for domain in domains]

# Salva os resultados no arquivo CSV
save_to_csv(results)

print("Consulta concluída. Resultados salvos em 'whois_results.csv'.")
