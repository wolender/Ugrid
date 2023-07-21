#Aditional implementation of task 6 using docker and smtp test container

docker build . -t sm

docker-compose up

#Go to http://localhost:3000/ to see recived mail
#Email adresses get pulled from recipients.txt file
