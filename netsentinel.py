
import sys
import ipaddress
import subprocess
import xml.etree.ElementTree as ET

# Rich: biblioteca para deixar o terminal organizado e colorido
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Cria o console responsável pelas mensagens coloridas
console = Console()

# True = simula o comando sem executar o Nmap
# False = executa a varredura real
simulacao = False


# ============================================================
# INTERFACE INICIAL
# ============================================================

def mostrar_banner():
    # Exibe a identidade visual do NetSentinel
    banner = r"""
 _   _      _   ____             _   _            _
| \ | | ___| |_/ ___|  ___ _ __ | |_(_)_ __   ___| |
|  \| |/ _ \ __\___ \ / _ \ '_ \| __| | '_ \ / _ \ |
| |\  |  __/ |_ ___) |  __/ | | | |_| | | | |  __/ |
|_| \_|\___|\__|____/ \___|_| |_|\__|_|_| |_|\___|_|

                  CREATED BY PH
"""

    console.print(
        Panel(
            f"[bold cyan]{banner}[/bold cyan]",
            title="[bold green]NETSENTINEL[/bold green]",
            subtitle="[white]Network Scanner | Cybersecurity[/white]",
            border_style="cyan"
        )
    )


# ============================================================
# MENU DE AJUDA
# ============================================================

def mostrar_ajuda():
    # Cria a tabela com os comandos disponíveis
    tabela = Table(title="COMANDOS DO NETSENTINEL")

    tabela.add_column("Comando", style="cyan")
    tabela.add_column("Descrição", style="white")

    tabela.add_row("-ftv", "Varredura de baixo impacto")
    tabela.add_row("-scan", "Scan das 1000 portas TCP mais comuns")
    tabela.add_row("-full", "Scan completo, serviços e sistema operacional")
    tabela.add_row("--help", "Mostrar comandos disponíveis")

    console.print(tabela)


# ============================================================
# CONFIGURAÇÃO DOS SCANS
# ============================================================

def configurar_scan(comando, alvo):

    if comando == "-ftv":
        # -sT: realiza conexões TCP completas
        # -T2: utiliza temporização mais conservadora
        # -p: seleciona portas específicas
        # Não garante invisibilidade ou ausência de detecção
        nome = "LOW IMPACT SCAN"

        argumentos = [
            "-sT",
            "-T2",
            "-p", "21,22,23,80,443,445,3389"
        ]

    elif comando == "-scan":
        # -sT: realiza conexões TCP completas
        # --top-ports: verifica as portas mais frequentes
        nome = "STANDARD SCAN"

        argumentos = [
            "-sT",
            "--top-ports", "1000"
        ]

    elif comando == "-full":
        # -sS: TCP SYN Scan (normalmente exige root)
        # -PE: utiliza ICMP Echo na descoberta do host
        # -p-: verifica todas as 65535 portas TCP
        # -sV: identifica serviços e versões
        # -O: tenta identificar o sistema operacional
        # -sC: executa os scripts NSE padrão
        nome = "FULL HOST SCAN"

        argumentos = [
            "-sS",
            "-PE",
            "-p-",
            "-sV",
            "-O",
            "-sC"
        ]

    # -oX -: retorna o resultado em XML na saída padrão
    # O XML facilita a leitura dos dados pelo Python
    comando_nmap = ["nmap"] + argumentos + ["-oX", "-", alvo]

    return nome, comando_nmap


# ============================================================
# PROCESSAMENTO DOS RESULTADOS
# ============================================================

def mostrar_resultados(xml):

    # Converte o XML produzido pelo Nmap para uma estrutura
    # que o Python consegue percorrer
    raiz = ET.fromstring(xml)

    hosts = raiz.findall("host")

    if not hosts:
        console.print("[yellow]Nenhum host encontrado.[/yellow]")
        return

    for host in hosts:

        # Obtém o status do host: up ou down
        status = host.find("status")
        estado = status.get("state", "unknown") if status is not None else "unknown"

        # Procura o endereço IP no resultado
        ip = "Desconhecido"

        for endereco in host.findall("address"):
            if endereco.get("addrtype") in ["ipv4", "ipv6"]:
                ip = endereco.get("addr", "Desconhecido")
                break

        # Procura a latência medida pelo Nmap
        latencia = "Não disponível"
        tempos = host.find("times")

        if tempos is not None:
            valor = tempos.get("srtt")

            if valor is not None:
                # O Nmap informa srtt em microssegundos
                latencia = f"{int(valor) / 1000:.2f} ms"

        # Procura a estimativa de sistema operacional
        sistema = "Não identificado"
        osmatch = host.find("./os/osmatch")

        if osmatch is not None:
            sistema = osmatch.get("name", "Desconhecido")

        # Exibe informações do host dentro de um painel
        console.print(
            Panel(
                f"[cyan]IP:[/cyan] {ip}\n"
                f"[cyan]Status:[/cyan] {estado.upper()}\n"
                f"[cyan]Latência:[/cyan] {latencia}\n"
                f"[cyan]Sistema operacional:[/cyan] {sistema}",
                title="[bold green]INFORMAÇÕES DO HOST[/bold green]",
                border_style="green"
            )
        )

        # Cria tabela de portas
        tabela = Table(title="PORTAS E SERVIÇOS")

        tabela.add_column("Porta", style="cyan")
        tabela.add_column("Status", style="green")
        tabela.add_column("Serviço", style="yellow")
        tabela.add_column("Versão", style="white")

        abertas = 0

        # Percorre as portas identificadas no XML
        for porta in host.findall("./ports/port"):

            numero = porta.get("portid", "?")
            protocolo = porta.get("protocol", "tcp")

            estado_porta = porta.find("state")
            status_porta = (
                estado_porta.get("state", "unknown")
                if estado_porta is not None else "unknown"
            )

            # Mostra somente portas abertas
            if status_porta != "open":
                continue

            abertas += 1

            # Obtém o serviço e sua possível versão
            servico = porta.find("service")

            nome_servico = "Desconhecido"
            versao = "-"

            if servico is not None:
                nome_servico = servico.get("name", "Desconhecido")

                produto = servico.get("product", "")
                numero_versao = servico.get("version", "")

                versao = f"{produto} {numero_versao}".strip() or "-"

            tabela.add_row(
                f"{numero}/{protocolo}",
                status_porta.upper(),
                nome_servico,
                versao
            )

        if abertas > 0:
            console.print(tabela)
        else:
            console.print(
                "[yellow]Nenhuma porta aberta identificada.[/yellow]"
            )

        # Mostra um resumo no final
        console.print(
            Panel(
                f"[green]Portas abertas: {abertas}[/green]\n"
                f"[cyan]Status do host: {estado.upper()}[/cyan]\n"
                "[green]Análise concluída![/green]",
                title="[bold cyan]RESUMO DA VARREDURA[/bold cyan]",
                border_style="cyan"
            )
        )


# ============================================================
# EXECUÇÃO DO NMAP
# ============================================================

def executar_scan(comando, alvo):

    # Valida se o endereço fornecido é IPv4 ou IPv6
    try:
        ipaddress.ip_address(alvo)

    except ValueError:
        console.print("[bold red][-] Endereço IP inválido![/bold red]")
        return

    # Prepara o comando de acordo com o modo escolhido
    nome, comando_nmap = configurar_scan(comando, alvo)

    console.print(
        Panel(
            f"[green]IP válido:[/green] {alvo}\n"
            f"[yellow]Modo:[/yellow] {nome}\n"
            f"[cyan]Simulação:[/cyan] {simulacao}",
            title="CONFIGURAÇÃO DO SCAN",
            border_style="blue"
        )
    )

    console.print(
        "[cyan]Comando preparado:[/cyan]",
        " ".join(comando_nmap)
    )

    # Se a simulação estiver ativa, não executa o Nmap
    if simulacao:
        console.print(
            Panel(
                "[yellow]Nenhuma varredura foi executada.[/yellow]\n"
                "[green]Configuração validada com sucesso![/green]",
                title="MODO SIMULAÇÃO",
                border_style="yellow"
            )
        )
        return

    try:
        # Executa o Nmap e captura stdout e stderr
        with console.status(
            "[bold yellow]Executando varredura...[/bold yellow]",
            spinner="dots"
        ):
            resultado = subprocess.run(
                comando_nmap,
                capture_output=True,
                text=True,
                timeout=600
            )

        # returncode 0 indica que o Nmap terminou sem erro
        if resultado.returncode == 0:

            console.print(
                "[bold green][+] Varredura finalizada![/bold green]"
            )

            # Processa o XML e organiza os resultados
            mostrar_resultados(resultado.stdout)

        else:
            console.print("[bold red][-] Erro no Nmap![/bold red]")
            console.print(resultado.stderr or resultado.stdout)

    except FileNotFoundError:
        # Ocorre quando o Nmap não está instalado ou no PATH
        console.print("[red]Nmap não encontrado![/red]")

    except subprocess.TimeoutExpired:
        # Interrompe a execução se ultrapassar 600 segundos
        console.print("[red]Tempo limite da varredura excedido![/red]")

    except ET.ParseError:
        # Trata uma resposta XML inválida ou incompleta
        console.print("[red]Erro ao interpretar o XML do Nmap![/red]")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    mostrar_banner()

    # sys.argv contém os argumentos enviados pelo terminal
    # Exemplo: python3 netsentinel.py -scan 127.0.0.1

    if len(sys.argv) < 2:
        console.print("[red]Nenhum comando informado![/red]")
        mostrar_ajuda()
        return

    comando = sys.argv[1]

    # Abre o menu de ajuda
    if comando == "--help":
        mostrar_ajuda()
        return

    # Verifica se o comando informado existe
    if comando not in ["-ftv", "-scan", "-full"]:
        console.print("[red]Comando inválido![/red]")
        mostrar_ajuda()
        return

    # Confirma se o usuário informou um endereço IP
    if len(sys.argv) < 3:
        console.print("[red]Nenhum alvo informado![/red]")
        return

    alvo = sys.argv[2]

    # Impede argumentos extras não reconhecidos
    if len(sys.argv) > 3:
        console.print("[red]Argumentos extras não reconhecidos![/red]")
        return

    executar_scan(comando, alvo)


# Executa main somente quando o arquivo é iniciado diretamente
if __name__ == "__main__":
    main()
