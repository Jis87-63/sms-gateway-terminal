#!/data/data/com.termux/files/usr/bin/bash
set -e
pkg update -y
pkg install -y python termux-api git
pip install --upgrade pip requests rich typer
chmod +x start.sh
mkdir -p ~/.shortcuts
cat > sms <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")"
python main.py "$@"
EOF
chmod +x sms
echo "Instalação concluída. Edite config.json com a URL do backend e rode: ./start.sh"
