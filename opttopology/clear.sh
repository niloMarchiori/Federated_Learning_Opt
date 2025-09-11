sudo rm -r client_log
sudo rm -r optmization
docker kill $(docker ps -q)
docker rm $(docker ps -aq)