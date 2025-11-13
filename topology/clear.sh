sudo rm -r client_log
sudo rm -r optmization
sudo rm -r Results

docker kill $(docker ps -aq)
docker rm $(docker ps -aq)