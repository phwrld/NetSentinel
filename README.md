\<div align="center">

# 🛡️ NETSENTINEL

### Network Reconnaissance & Security Analysis Tool

**Developed by PH**



\


*A Python-based CLI tool for network reconnaissance, security analysis and penetration testing automation.*

\</div>

---

## 📖 Sobre o Projeto

O **NetSentinel** é uma ferramenta de linha de comando (CLI) desenvolvida em **Python**, com o objetivo de automatizar tarefas de reconhecimento de redes e auxiliar profissionais e estudantes de Cybersecurity durante testes de penetração autorizados.

O projeto foi criado para aplicar conhecimentos adquiridos em estudos de:

- 🔹 Network Reconnaissance
- 🔹 TCP/IP e protocolos de rede
- 🔹 Nmap e Network Scanning
- 🔹 Python Automation
- 🔹 Ethical Hacking
- 🔹 Penetration Testing

> ⚠️ **Status:** Projeto em desenvolvimento. A integração com Nmap está sendo implementada e ainda não foi validada em ambiente de testes.

---

## 🚀 Funcionalidades

### ✅ Funcionalidades iniciais

- [x] Interface CLI desenvolvida em Python.
- [x] Banner ASCII personalizado.
- [x] Identificação de argumentos com `sys.argv`.
- [x] Comandos `-scan`, `-ftv` e `--help`.
- [x] Validação de endereços IPv4 e IPv6.
- [x] Tratamento de entradas inválidas com `try/except`.

### 🔧 Funcionalidades planejadas

- [ ] Integração funcional com Nmap.
- [ ] Varredura TCP automatizada.
- [ ] Modo FTV de reconhecimento de baixo impacto.
- [ ] Identificação de serviços e versões.
- [ ] Análise de portas potencialmente inseguras.
- [ ] Classificação de riscos.
- [ ] Geração de relatórios HTML e JSON.
- [ ] Instalação como ferramenta CLI independente.

---

## 💻 Comandos do NetSentinel

| Comando   | Descrição                                 | Status |
| :-------- | :---------------------------------------- | :----: |
| `--help`  | Exibe os comandos disponíveis             |    ✅   |
| `-scan`   | Perfil de varredura padrão                |   🚧   |
| `-ftv`    | Perfil de reconhecimento de baixo impacto |   🚧   |
| `-report` | Geração de relatórios de segurança        |   📅   |
| `-svc`    | Identificação de serviços e versões       |   📅   |

**Legenda:** ✅ Implementado | 🚧 Em desenvolvimento | 📅 Planejado

### 📌 Exemplos de utilização

**Exibir o menu de ajuda:**

```bash
python netsentinel.py --help
```

**Selecionar o modo de varredura padrão:**

```bash
python netsentinel.py -scan 127.0.0.1
```

**Selecionar o modo FTV:**

```bash
python netsentinel.py -ftv 127.0.0.1
```

> Os comandos de scan ainda estão em desenvolvimento. Os exemplos demonstram a interface planejada e não garantem a execução de varreduras.

---

## 🥷 FTV — Low Impact Reconnaissance

O **FTV** é um modo planejado para executar reconhecimento de rede com intensidade reduzida.

### Objetivos

- Reduzir o volume de tráfego gerado durante o reconhecimento.
- Utilizar perfis de temporização conservadores.
- Limitar a quantidade de portas verificadas.
- Coletar informações relevantes sobre serviços expostos.
- Organizar os resultados para análise posterior.

### Configuração inicial planejada

```bash
nmap -sT -T2 -p 21,22,23,80,443,445,3389 127.0.0.1
```

| Parâmetro   | Descrição                     |
| ----------- | ----------------------------- |
| `-sT`       | TCP Connect Scan              |
| `-T2`       | Temporização conservadora     |
| `-p`        | Seleção das portas analisadas |
| `127.0.0.1` | Endereço de teste local       |

> **Nota técnica:** baixo impacto não significa invisibilidade. O tráfego pode ser registrado e detectado por mecanismos de segurança.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade                          |
| ---------- | ----------------------------------- |
| Python 3   | Desenvolvimento da ferramenta       |
| Nmap       | Reconhecimento e varredura de redes |
| sys        | Processamento de argumentos CLI     |
| ipaddress  | Validação de endereços IP           |
| subprocess | Execução de ferramentas externas    |
| Git        | Controle de versões                 |
| GitHub     | Hospedagem e documentação           |

---

## 📂 Estrutura do Projeto

```text
NetSentinel/
│
├── netsentinel.py
├── README.md
├── .gitignore
│
└── LICENSE (opcional)
```

### Estrutura futura

```text
NetSentinel/
│
├── netsentinel.py
│
├── core/
│   ├── scanner.py
│   ├── analyzer.py
│   └── validator.py
│
├── reports/
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/phwrld/NetSentinel.git
```

### 2. Acesse o diretório

```bash
cd NetSentinel
```

### 3. Execute a ferramenta

```bash
python netsentinel.py --help
```

**Requisitos:**

- Python 3
- Windows ou Linux
- Nmap instalado e disponível no PATH para as futuras funcionalidades de varredura

---

## 🗺️ Roadmap de Desenvolvimento

### Fase 1 — CLI Foundation

- [x] Criar a estrutura inicial.
- [x] Desenvolver banner ASCII.
- [x] Implementar argumentos de execução.
- [x] Validar endereços IP.

### Fase 2 — Network Scanning

- [ ] Integrar Nmap.
- [ ] Implementar TCP scanning.
- [ ] Desenvolver modo FTV.
- [ ] Tratar erros de execução.

### Fase 3 — Security Analysis

- [ ] Identificar portas abertas.
- [ ] Analisar serviços expostos.
- [ ] Criar alertas de segurança.
- [ ] Classificar riscos encontrados.

### Fase 4 — Reporting

- [ ] Exportar resultados JSON.
- [ ] Gerar relatórios HTML.
- [ ] Registrar histórico de varreduras.
- [ ] Documentar evidências técnicas.

### Fase 5 — Release

- [ ] Refatorar o código.
- [ ] Adicionar testes automatizados.
- [ ] Publicar a versão estável.
- [ ] Disponibilizar instalação via terminal.

---

## 🔐 Aviso Legal

O NetSentinel é um projeto desenvolvido exclusivamente para **fins educacionais, pesquisa e testes de segurança autorizados**.

A utilização da ferramenta deve ocorrer somente em:

- Ambientes de laboratório.
- Máquinas virtuais próprias.
- Redes sob administração do usuário.
- Sistemas com autorização explícita para testes.

O autor não incentiva sua utilização contra sistemas sem autorização.

---

## 👨‍💻 Desenvolvedor

**PH — Developer & Cybersecurity Student**

Estudante de **Desenvolvimento de Sistemas no SENAI**, com foco em Segurança Ofensiva, Redes de Computadores e Penetration Testing.

Atualmente aprofundando conhecimentos em Python, Linux, Nmap, Ethical Hacking e segurança de redes.

**GitHub:** [github.com/phwrld](https://github.com/phwrld)

---

\<div align="center">

### 🛡️ NETSENTINEL

**Learn. Analyze. Secure.**

*Developed by PH | 2026*

\</div>
