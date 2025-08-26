sudo rm -r client_log
sudo rm -r SIGCOMM-DEMO/sigcomm
docker kill $(docker ps -q)
docker rm $(docker ps -aq)