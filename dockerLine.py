docker run -itd --name submysql -p 3308:3306 -e MYSQL_ROOT_PASSWORD=1231230 mysql --character-set-server=utf8

docker exec f9c2ac5d3139 sh -c 'mysql -u root -p"" -e "create database wp;"'

docker run -itd --name myweb --link submysql:db -p 90:80 -v /container_data/web:/var/www/html richarvey/nginx-php