
```sh
wget https://raw.githubusercontent.com/openforcefield/openff-sage/refs/tags/2.0.0-rc.1/data-set-curation/physical-property/benchmarks/data-sets/sage-mnsol-test-v1.txt
wget https://raw.githubusercontent.com/openforcefield/openff-sage/refs/tags/2.0.0-rc.1/data-set-curation/physical-property/benchmarks/data-sets/sage-fsolv-test-v1.csv
wget https://github.com/OpenFreeEnergy/alchemiscale.org-deployment/raw/refs/tags/2025.03.04-0/deployments/root/conda-envs/alchemiscale-client.yml

micromamba create -f gen_charges_env.yml
micromamba run -n pontibus_gen_charges python gen_charges.py

micromamba create -f alchemiscale-client.yml

cd freesolv-oe
micromamba run -n alchemiscale-client python gen_network.py
micromamba run -n alchemiscale-client python ../shared-scripts/submit.py --network_filename alchemical_network.json --org_scope "openff" --scope_name_campaign "openff_2_2_1_oe" --scope_name_project "freesolv" --repeats 3

cd mnsol-oe
micromamba run -n alchemiscale-client python gen_network.py
micromamba run -n alchemiscale-client python ../shared-scripts/submit.py --network_filename alchemical_network.json --org_scope "openff" --scope_name_campaign "openff_2_2_1_oe" --scope_name_project "mnsol" --repeats 3
```
