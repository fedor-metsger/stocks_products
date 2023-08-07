#!/bin/bash
cd /home/fedor/stocks_products
git pull origin ci_cd
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
sudo systemctl restart gunicorn
