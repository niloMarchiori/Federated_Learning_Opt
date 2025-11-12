sudo rm -r client_log
sudo rm -r optmization
sudo rm -r Results_Opt
sudo rm -r Input_Model

docker kill $(docker ps -q)
docker rm $(docker ps -aq)