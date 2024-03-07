#!/usr/bin/env python3
# sets up web servers for deployment of web_static
if [ ! -f /usr/bin/nginx ]; then
	apt-get update
	apt-get install -y nginx
fi
if [ ! -d /data/web_static/releases/test/ ]; then
	mkdir -p /data/web_static/releases/test/
fi
if [ ! -d /data/web_static/shared/ ]; then
	mkdir -p /data/web_static/shared/
fi
chown -R ubuntu:ubuntu /data
if [ ! -L /data/web_static/current ]; then
	ln -sfn /data/web_static/releases/test /data/web_static/current
else
	rm /data/web_static/current
	ln -sfn /data/web_static/releases/test //data/web_static/current
fi

echo "
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >> /data/web_static/releases/test/index.html
sed -i "s|root .*;|alias /data/web_static/current;\n\tindex.html index index.htm;" /etc/nginx/sites-available/default
nginx -t
service nginx restart
