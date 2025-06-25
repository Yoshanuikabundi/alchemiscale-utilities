2.3.0rc1 is `fb-fit-v6-single-mean-k100-eps.offxml`; `fb-fit-v6-single-mean-k100-eps-witham1bcc.offxml` is identical but has a `<ToolkitAM1BCC>` tag to workaround a bug in pontibus 0.0.2 in which an absent `<ToolkitAM1BCC>` tag causes system prep to fail.


```sh
micromamba create -f gen_charges_env.yml
micromamba run -n pontibus_gen_charges python gen_charges.py

micromamba create -f ../alchemiscale-client.yml

cd freesolv
micromamba run -n alchemiscale-client python gen_network.py
micromamba run -n alchemiscale-client python ../shared-scripts/submit.py --network_filename alchemical_network.json --org_scope "openff" --scope_name_campaign "openff_2_3_0_rc1" --scope_name_project "freesolv" --repeats 3
cd ..

cd mnsol
micromamba run -n alchemiscale-client python gen_network.py
micromamba run -n alchemiscale-client python ../shared-scripts/submit.py --network_filename alchemical_network.json --org_scope "openff" --scope_name_campaign "openff_2_3_0_rc1" --scope_name_project "mnsol" --repeats 3
cd ..

cd highrmse
micromamba run -n alchemiscale-client python gen_network.py
micromamba run -n alchemiscale-client python ../shared-scripts/submit.py --network_filename alchemical_network.json --org_scope "openff" --scope_name_campaign "openff_2_3_0_rc1" --scope_name_project "highrmse" --repeats 3
cd ..

micromamba run -n alchemiscale-client python shared-scripts/monitor.py --scope_key mnsol-oe/scoped-key.dat
```
