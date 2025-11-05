sudo -E sh -c "python3 reference_topology/topology.py && \
               mnf_clean && \
               python3 opttopology/topology.py"

git add .
git commit -m "Resultados teste r_samples"
git push

shutdown -r