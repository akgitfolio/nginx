
export CONTAINER_NAME=$(basename "$PWD")

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ssl/server.key -out ./ssl/server.crt -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=example.com"
docker-compose up --build