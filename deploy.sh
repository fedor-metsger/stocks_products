#!/bin/bash
cd /home/<user_name>/<project_name>
git pull origin ci_cd
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
sudo systemctl restart gunicorn
