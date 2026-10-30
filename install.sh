#!/usr/bin/env bash
set -euo pipefail

# Instala o NetSentinel e registra o comando "nst" no Kali/Debian.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -f "$SCRIPT_DIR/netsentinel.py" ]]; then
  echo "Erro: netsentinel.py não encontrado na pasta do instalador." >&2
  exit 1
fi

if ! command -v apt-get >/dev/null 2>&1; then
  echo "Este instalador requer Kali Linux, Debian ou derivado com apt-get." >&2
  exit 1
fi

if [[ "$(id -u)" -eq 0 ]]; then
  SUDO=()
else
  if ! command -v sudo >/dev/null 2>&1; then
    echo "Erro: sudo não encontrado. Execute o instalador como root." >&2
    exit 1
  fi
  SUDO=(sudo)
fi

echo "[NetSentinel] Instalando dependências..."
"${SUDO[@]}" apt-get update
"${SUDO[@]}" apt-get install -y python3 python3-rich nmap

echo "[NetSentinel] Instalando o comando nst..."
"${SUDO[@]}" install -d -m 755 /usr/local/lib/netsentinel
"${SUDO[@]}" install -m 644 "$SCRIPT_DIR/netsentinel.py" /usr/local/lib/netsentinel/netsentinel.py

# O wrapper utiliza o Python do sistema com o pacote Rich instalado pelo apt.
printf '%s\n' '#!/bin/sh' 'exec /usr/bin/python3 /usr/local/lib/netsentinel/netsentinel.py "$@"' |
  "${SUDO[@]}" tee /usr/local/bin/nst >/dev/null
"${SUDO[@]}" chmod 755 /usr/local/bin/nst

echo "[NetSentinel] Instalação concluída. Execute: nst --help"
