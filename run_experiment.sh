sudo -E sh -c "python topology/topology_rsamples.py"
mnf_clean
sudo -E sh -c "python topology/topology_same.py"

git add .
git commit -m "Resultados experimento"
git push