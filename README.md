# Room Conditions API

## 概要

部屋の温度と湿度を返却する API です。  
SHT31 センサーを搭載した Raspberry Pi での使用を想定しています。

## 準備

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## 起動方法

```sh
. venv/bin/activate # 必要に応じて実行
gunicorn -b 0.0.0.0:5000 "app:app"
```

## systemd を用いた自動起動

1. 以下のコマンドでサービスファイルを作成します。

```sh
sudo vi /etc/systemd/system/room_conditions_api.service
```

2. サービスファイルに以下の内容をコピーします。`your_username` は適宜実際のユーザー名に変更してください。

```ini
[Unit]
Description=Room Conditions API
After=network.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/room_conditions_api
Environment="PATH=/home/your_username/room_conditions_api/venv/bin"
ExecStart=/home/your_username/room_conditions_api/venv/bin/gunicorn -b 0.0.0.0:5000 "app:app"

[Install]
WantedBy=multi-user.target
```

3. サービスを有効化し、起動します。

```sh
sudo systemctl enable room_conditions_api.service
sudo systemctl start room_conditions_api.service
```
