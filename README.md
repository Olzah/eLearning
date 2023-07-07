There are ways to install and run Odoo locally: at first you need install and configurate necessary apps and libraries, all info in link below: https://www.odoo.com/documentation/16.0/administration/install/install.html#prepare

git clone with submodules: git clone --recurse-submodules 'url'

create venv

install requirements.txt pip3 install -r odoo/requirements.txt

configurate odoo.conf: maine big deal - add addons path parameter

start odoo with command below: ./odoo/odoo-bin -c /path/to/project/odoo/debian/odoo.conf with parameter in the end of line -d dataBaseName --dev xml,reload - that parameter gives us to reload server when we are changing code

