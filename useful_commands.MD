### Installing libraries
  
#### PIP ✔️  
* To install pip libraries from requirements.txt, run
    ````pip install -r requirements.txt````
* To update requirements.txt after installing new library via `pip`,
    run ````pip list --format=freeze > requirements.txt````

#### CONDA ( ⚠️`conda list --no-pip` has issues. DO NOT EXECUTE BELOW COMMANDS)
* Save packages for future use after installing a new conda package:
⚠️```conda list --no-pip --export > package-list.txt```

* Reinstall packages from an export file:\
⚠️```conda create -n myenv --file package-list.txt```