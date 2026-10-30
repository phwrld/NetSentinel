# NetSentinel

**Network Reconnaissance & Security Analysis Tool**

**Developed by PH**

O **NetSentinel** é uma ferramenta de linha de comando (CLI) desenvolvida em **Python**, com o objetivo de automatizar varreduras de rede, identificar serviços e auxiliar em atividades de **Cybersecurity, Pentest e CTFs**.

O projeto utiliza o **Nmap** para executar varreduras e o **Rich** para apresentar os resultados de maneira organizada no terminal.

---

## Funcionalidades

- **Network Scanning:** identificação de portas TCP abertas.
- **Host Discovery:** descoberta de hosts ativos na rede.
- **Service Detection:** identificação de serviços e versões.
- **OS Detection:** estimativa do sistema operacional do alvo.
- **Low Impact Scan:** varredura com temporização conservadora e portas específicas.
- **Full Host Scan:** análise das portas TCP, serviços e sistema operacional.
- **CLI Interface:** apresentação dos resultados em tabelas e painéis no terminal.
- **Simulation Mode:** preparação dos comandos sem executar varreduras reais.

## Comandos

| Comando | Função |
|---|---|
| `nst --help` | Exibe os comandos disponíveis. |
| `nst -ftv IP` | Varredura TCP de baixo impacto. |
| `nst -scan IP` | Varredura das 1.000 portas TCP mais comuns. |
| `nst -full IP` | Varredura completa de portas TCP, serviços e SO. |

### Exemplos de utilização

**Varredura de baixo impacto:**

```bash
nst -ftv 127.0.0.1
```

**Varredura padrão:**

```bash
nst -scan 127.0.0.1
```

**Varredura completa:**

```bash
sudo nst -full 127.0.0.1
```

**Observação:** para executar varreduras reais, configure `simulacao = False` no código. O comando `nst` precisa estar instalado e configurado no sistema.

---

## Tecnologias

- **Python 3:** desenvolvimento e automação.
- **Nmap:** descoberta e varredura de redes.
- **Rich:** interface visual no terminal.
- **XML:** processamento dos resultados do Nmap.
- **Linux / Kali Linux:** ambiente de execução e testes.
- **Git e GitHub:** versionamento e documentação.

---

## Instalação no Kali Linux

**1. Clone o repositório:**

```bash
git clone https://github.com/phwrld/NetSentinel.git
```

**2. Entre na pasta:**

```bash
cd NetSentinel
```

**3. Execute o instalador:**

```bash
chmod +x install.sh
./install.sh
```

**4. Verifique a instalação:**

```bash
nst --help
```

A instalação utiliza o `apt` para instalar Python 3, Rich e Nmap e registra o comando `nst` no sistema.

---

## Desenvolvimento futuro

- **Security Reports:** geração de relatórios HTML, TXT e JSON.
- **Risk Analysis:** classificação de portas e serviços potencialmente inseguros.
- **Automation:** criação de novos comandos para automatizar tarefas de reconhecimento.
- **Modular Architecture:** organização do projeto em módulos independentes.

---

## Desenvolvedor

**PH — Developer & Cybersecurity Student**

Estudante de Desenvolvimento de Sistemas no **SENAI**, com foco em **Cybersecurity, Ethical Hacking e Penetration Testing**.

O NetSentinel é um projeto pessoal desenvolvido para aplicar conhecimentos de programação, redes e segurança ofensiva em laboratórios, CTFs e testes autorizados.

**Status:** em desenvolvimento.

---

**NETSENTINEL**

*Learn. Analyze. Secure.*

**Developed by PH | 2026**
