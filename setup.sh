#!/bin/bash

# === 事前準備 ===
set -e  # エラーで即停止
sudo apt-get update

# === 1. 必要なaptパッケージのインストール ===
echo "🔧 Installing required system packages..."
sudo apt-get install -y i2c-tools python3-smbus

# === 2. Pythonモジュールのインストール（py_requirements.txtより）===
if [ -f py_requirements.txt ]; then
    echo "📦 Installing Python dependencies..."
    pip3 install -r py_requirements.txt
fi

# === 3 データファイルの作成とパーミッション設定 ===
USER_NAME=$(whoami)
DATA_DIR="/var/www/html/data"
sudo mkdir -p "$DATA_DIR"

for FILE in temp.txt humi.txt; do
    FILE_PATH="$DATA_DIR/$FILE"
    echo "📝 Creating $FILE_PATH..."
    sudo touch "$FILE_PATH"
    sudo chown "$USER_NAME":www-data "$FILE_PATH"
    sudo chmod 664 "$FILE_PATH"
done

# === 4. systemd .service ファイルを自動生成 ===
WORK_DIR=$(pwd)

declare -A SERVICES=(
  ["dht11_logger"]="dht11_logger.py"
  ["LCD_display"]="LCD_display.py"
)

for SERVICE_NAME in "${!SERVICES[@]}"; do
  SCRIPT_NAME=${SERVICES[$SERVICE_NAME]}
  SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
  SCRIPT_PATH="${WORK_DIR}/src/${SCRIPT_NAME}"

  echo "🛠 Creating $SERVICE_FILE..."

  cat <<EOF | sudo tee $SERVICE_FILE > /dev/null
[Unit]
Description=$SERVICE_NAME Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 $SCRIPT_PATH
Restart=always
User=$USER_NAME
WorkingDirectory=${WORK_DIR}/src

[Install]
WantedBy=multi-user.target
EOF
done

# === 5. サービスを登録・起動 ===
sudo systemctl daemon-reload
for SERVICE in "${!SERVICES[@]}"; do
  sudo systemctl enable "$SERVICE"
  sudo systemctl restart "$SERVICE"
  systemctl status "$SERVICE" --no-pager
done
echo "✅ Setup completed. Services are active:"
