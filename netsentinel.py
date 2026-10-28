
import sys
import ipaddress
import subprocess

print(r"""
 _   _      _   ____             _   _            _
| \ | | ___| |_/ ___|  ___ _ __ | |_(_)_ __   ___| |
|  \| |/ _ \ __\___ \ / _ \ '_ \| __| | '_ \ / _ \ |
| |\  |  __/ |_ ___) |  __/ | | | |_| | | | |  __/ |
|_| \_|\___|\__|____/ \___|_| |_|\__|_|_| |_|\___|_|

                  CREATED BY PH
""")

print("Argumentos recebidos:", sys.argv)

simulacao = True

if len(sys.argv) > 1:

    comando = sys.argv[1]

    if comando == "-ftv":

        if len(sys.argv) > 2:
            alvo = sys.argv[2]

            try:
                ipaddress.ip_address(alvo)

                print("[+] IP válido!")
                print("[+] Modo de baixo impacto ativado!")
                print("[+] Alvo selecionado:", alvo)

                comando_nmap = [
                    "nmap",
                    "-sT",
                    "-T2",
                    "-p", "21,22,23,80,443,445,3389",
                    alvo
                ]

                print("[+] Nmap configurado!")
                print("[+] Comando:", " ".join(comando_nmap))

                if simulacao:
                    print("[SIMULAÇÃO] Nenhuma varredura foi executada.")
                    print("[+] Comando preparado com sucesso!")

                else:
                    try:
                        resultado = subprocess.run(
                            comando_nmap,
                            capture_output=True,
                            text=True
                        )

                        if resultado.returncode == 0:
                            print("[+] Varredura finalizada!")
                            print(resultado.stdout)

                        else:
                            print("[-] Erro durante a varredura!")
                            print(resultado.stderr)

                    except FileNotFoundError:
                        print("[-] ERRO: Nmap não encontrado!")

            except ValueError:
                print("[-] ERRO: IP inválido!")

        else:
            print("[-] ERRO: Nenhum alvo informado!")

    elif comando == "-scan":

        if len(sys.argv) > 2:
            alvo = sys.argv[2]

            try:
                ipaddress.ip_address(alvo)

                print("[+] IP válido!")
                print("[+] Modo de varredura ativado!")
                print("[+] Alvo selecionado:", alvo)

                comando_nmap = [
                    "nmap",
                    "-sT",
                    "--top-ports", "1000",
                    alvo
                ]

                print("[+] Nmap configurado!")
                print("[+] Comando:", " ".join(comando_nmap))

                if simulacao:
                    print("[SIMULAÇÃO] Nenhuma varredura foi executada.")
                    print("[+] Scan preparado com sucesso!")

                else:
                    try:
                        resultado = subprocess.run(
                            comando_nmap,
                            capture_output=True,
                            text=True
                        )

                        if resultado.returncode == 0:
                            print("[+] Varredura finalizada!")
                            print(resultado.stdout)

                        else:
                            print("[-] Erro durante a varredura!")
                            print(resultado.stderr)

                    except FileNotFoundError:
                        print("[-] ERRO: Nmap não encontrado!")

            except ValueError:
                print("[-] ERRO: IP inválido!")

        else:
            print("[-] ERRO: Nenhum alvo informado!")

    elif comando == "--help":

        print("Sejam bem-vindos ao NetSentinel!")
        print("Automatizador de varreduras e relatórios.")
        print()
        print("Comandos disponíveis:")
        print("-ftv  : Modo de baixo impacto")
        print("-scan : Varredura padrão")
        print("--help: Mostrar ajuda")

    else:
        print("[-] Comando inválido!")

else:
    print("[-] Nenhum comando informado!")
    print("Digite --help para ver os comandos.")
