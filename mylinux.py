ps -ef | grep nginx 查看nginx是否运行中

/sbin/nginx -c /etc/nginx/nginx.conf

/etc/nginx

firewall-cmd --state 查看防火墙状态
systemctl start firewalld.service
systemctl stop firewalld.service

nginx 启动 停止 重启
service nginx start
service nginx stop
service nginx restart

打印nginx access.log里面ip的访问次数
awk '{print $1}' access.log |sort |uniq -c|sort -n


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

查看端口开启情况 netstat -tlunp

查看所有开启的端口
firewall-cmd --list-ports  

开启80端口 firewall-cmd --zone=public --add-port=8088/tcp --permanent
重启 firewall-cmd --reload
删除 firewall-cmd --zone=public --remove-port=3306/tcp --permanent


cp 50x.html /root/www/static-web/