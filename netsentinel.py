import sys
import ipaddress

print(r"""
 _   _      _   ____             _   _            _
| \ | | ___| |_/ ___|  ___ _ __ | |_(_)_ __   ___| |
|  \| |/ _ \ __\___ \ / _ \ '_ \| __| | '_ \ / _ \ |
| |\  |  __/ |_ ___) |  __/ | | | |_| | | | |  __/ |
|_| \_|\___|\__|____/ \___|_| |_|\__|_|_| |_|\___|_|

                  CREATED BY PH
""")

print("Argumentos recebidos:", sys.argv)

if len(sys.argv) > 1:

    comando = sys.argv[1]  # Comando

    if comando == "-ftv":

        if len(sys.argv) > 2:
            alvo = sys.argv[2]  # Alvo

            try:
                ipaddress.ip_address(alvo)

                print("[+] IP válido!")
                print("[+] Modo de baixo impacto ativado!")
                print("[+] Alvo selecionado:", alvo)

            except ValueError:
                print("[-] ERRO: IP inválido!")

        else:
            print("[-] ERRO: Nenhum alvo informado!")

    elif comando == "-scan":

        if len(sys.argv) > 2:
            alvo = sys.argv[2]  # Alvo

            try:
                ipaddress.ip_address(alvo)

                print("[+] IP válido!")
                print("[+] Modo de varredura ativado!")
                print("[+] Alvo selecionado:", alvo)

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
    