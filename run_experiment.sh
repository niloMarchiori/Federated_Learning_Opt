sudo -E sh -c "python topology/topology_rsamples.py;\
        mnf_clean;\
        python topology/topology_same.py"

echo > end