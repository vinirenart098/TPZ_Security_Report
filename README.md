
# TPZ_Security_Report

Projeto de análise e mitigação de fraudes bancárias, desenvolvido para identificar domínios fraudulentos, investigar vulnerabilidades no domínio oficial do banco e propor soluções para evitar novos ataques.

---

## 🎯 Objetivos do Projeto
- **Identificar e Analisar Fraudes:** Investigar domínios fraudulentos usados em ataques de phishing.
- **Avaliar Domínio Oficial:** Verificar configurações e segurança do domínio principal do banco.
- **Propor Recomendações:** Sugerir ações para mitigar riscos futuros e proteger clientes.

---

## 🔧 Funcionalidades
- **Consulta WHOIS:** Obtenção de informações detalhadas sobre domínios (registrador, IP, status).
- **Análise Técnica:** Comparação entre domínios legítimos e fraudulentos.
- **Geração de Relatórios:** Criação de relatórios técnicos em CSV e Excel com dados estruturados.
- **Recomendações de Segurança:** Boas práticas para mitigar riscos e evitar fraudes.

---

## 🚀 Como Executar o Projeto

### **1. Pré-requisitos**
- Python 3.8 ou superior.
- Instale as bibliotecas necessárias com:
  ```bash
  pip install requests pandas openpyxl
  ```

### **2. Clonar o Repositório**
```bash
git clone https://github.com/vinirenart098/TPZ_Security_Report.git
cd TPZ_Security_Report
```

### **3. Configurar a API Key**
Atualize a chave de API no script para realizar consultas WHOIS:
```python
API_KEY = "sua_api_key_aqui"
```

### **4. Executar o Script**
```bash
python consulta_whois.py
```

Os resultados serão salvos no arquivo `whois_results.csv` na raiz do projeto.

---

## 📂 Estrutura do Projeto
```
TPZ_Security_Report/
├── consulta_whois.py       # Script principal para consulta WHOIS
├── whois_results.csv       # Resultados das consultas WHOIS
├── README.md               # Documentação do projeto
```

---

## 📊 Exemplos de Saída
| Domínio                            | Registrador           | Data de Criação | IP              | Observações          |
|------------------------------------|-----------------------|-----------------|-----------------|----------------------|
| bancotpzatualiza.apps.dnofd.com    | GoDaddy.com, LLC      | 13/07/2017      | 54.80.239.42    | Domínio Fraudulento  |
| bb.com.br                          | Registro.br           | 20/03/1996      | 170.66.10.10    | Protegido            |
| itau.com.br                        | CSC CORPORATE DOMAINS | 17/12/1997      | 170.79.10.10    | Protegido            |

---

## 🛠️ Melhorias Futuras
- Implementação de monitoramento contínuo de domínios suspeitos.
- Integração com ferramentas de segurança para análise automática de domínios.

---

## 📞 Contato
Desenvolvido por **vinirenart**  
[GitHub Profile](vinirenart@yahoo.com.br)
