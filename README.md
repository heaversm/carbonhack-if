# Impact Framework

## Running Impact Framework Getting Started Pipeline

Install Framework

`npm install -g "@grnsft/if"`

Install Plugins

`npm install -g "@grnsft/if-plugins"`

Install unofficial plugins

`npm i -g @grnsft/if-unofficial-plugins`

Create a manifest file - `manifest.yml`

Create a .env file



### Register for Watt Time



1. **Make an .env file**

```
WATT_TIME_USERNAME=<YOUR_DESIRED_USERNAME>
WATT_TIME_PASSWORD=<YOUR_DESIRED_PW>
WATT_TIME_EMAIL=<YOUR_DESIRED_EMAIL>
WATT_TIME_ORG=<YOUR_DESIRED_ORG>
```

2. Run the `watt-register.py script`:

`python3 utilities/watt-register.py`

Run the `watt-login.py` script:

`python3 utilities/watt-login.py`

3. Run the sample manifest file:

   ie `--manifest manifest-files/manifest-in.yaml --output manifest-output/manifest-out`


---

