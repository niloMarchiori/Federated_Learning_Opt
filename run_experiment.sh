sudo -E python3 opttopology/topology.py
sudo -E python3 reference_topology/topology.py
git add .
git commit -m "Msg automatica: novos resultados"
git push
shutdown