sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE bbase;"
mysql -uroot -e "CREATE USER 'user'@'localhost' IDENTIFIED BY 'pass';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
