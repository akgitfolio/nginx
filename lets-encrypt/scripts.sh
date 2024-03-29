
export CONTAINER_NAME=$(basename "$PWD")
brew install certbot
sudo certbot certonly --standalone -d localhost
docker-compose up --build

# sudo security import /path/to/your/certificate.p12 -k /Library/Keychains/System.keychain