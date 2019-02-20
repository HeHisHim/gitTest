ps -ef | grep nginx 查看nginx是否运行中

/sbin/nginx -c /etc/nginx/nginx.conf

/etc/nginx

firewall-cmd --state 查看防火墙状态
systemctl start firewalld.service
systemctl stop firewalld.service

停止
nginx -s stop
启动
cd sbin
./nginx


/root/www/static-web



scp index.html root@95.179.184.41:/root/www/static-web


server {
  server_name 95.179.184.41; // 你的域名或者 ip
  root /www/static-web; // 你的克隆到的项目路径
  index index.html; // 显示首页
  location ~* ^.+\.(jpg|jpeg|gif|png|ico|css|js|pdf|txt){
    root /www/static-web;
  } // 静态文件访问
}


/etc/nginx/conf.d

scp index.html root@95.179.184.41:/root/www/static-web
scp static_web.conf root@95.179.184.41:/etc/nginx/conf.d

/usr/share/nginx/html

开启80端口 firewall-cmd --zone=public(作用域) --add-port=80/tcp(端口和访问类型) --permanent(永久生效)
删除 firewall-cmd --zone= public --remove-port=80/tcp --permanent


cp 50x.html /root/www/static-web/