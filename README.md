# Impact Framework

[![How to use the Impact Framework from the Green Software Foundation](https://img.youtube.com/vi/5WImTN8840E/0.jpg)](https://www.youtube.com/watch?v=5WImTN8840E)

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

`ie --manifest manifest-input/manifest-in.yaml --output manifest-output/manifest-out`


---

## Other Info

### Relevant Plugins

* [Teads Curve](https://github.com/Green-Software-Foundation/if-unofficial-plugins/blob/main/src/lib/teads-curve/README.md) - estimates CPU usages across varying type of CPUs
* [Watt Time](https://github.com/Green-Software-Foundation/if-unofficial-plugins/blob/main/src/lib/watt-time/README.md) - provides a way to calculate emissions for a given time in a specific geolocation.
* [Cloud Metadata](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/cloud-metadata/README.md) - determine an instance's physical processor and thermal design power based on its instance name.
* [Sci](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/sci/README.md) - amount of carbon emitted per[ functional unit](https://sci-guide.greensoftware.foundation/R/) (e.g. API request)
* [Sci-E](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/sci-e/README.md)- simply sums up the contributions to a component's energy use (CPU/memory/network in kWh over a duration, in seconds). Acts as input to operational emissions ↩️
* [Sci-O](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/sci-o/README.md) - Operational emissions of component while in use (energy in kWh X grid intensity in gCO2e/kWh) - yields gCO2eq
* [Sci-M](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/sci-m/README.md) - carbon emitted during the manufacture and eventual disposal of a component and is added to operational carbon, yielding gCO2eq
* [TDP](https://github.com/Green-Software-Foundation/if-plugins/blob/main/src/lib/tdp-finder/README.md) - Thermal Design Power of a processor - sourced from Codecarbon, Boavista, and Kaggle.