
docker build -t petclinic .
docker run -p 80:8080 --network=my-network -e DB_MODE=$DB_MODE -e MYSQL_URL=jdbc:mysql://$SQL_URL:3306/petclinic wolender/release_repo:$VERSION

docker run -p 80:8080 