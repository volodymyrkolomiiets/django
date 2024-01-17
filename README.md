# django

docker run -d  --memory=200g --name mysql-database -e MYSQL_ROOT_PASSWORD=db_pass -e MYSQL_DATABASE=mydatabase -v /Users/volodymyrkolomiiets/testdb:/var/lib/mysql  -p 3306:3306 mysql