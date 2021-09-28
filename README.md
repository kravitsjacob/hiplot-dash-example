# hiplot-dash-example
This repository provides a simple example of how to embed a hiplot experiement into dash. This is mainly a reference to [this](https://github.com/facebookresearch/hiplot/issues/194) issue.

# Repository organization
* `app.py`: Python script containing simple example
* `hiplot-dash-example.yml`: Conda environment with proper dependencies
* `run.sh`: Bash script to run `app.py` in the conda environment specified in `hiplot-dash-example.yml`
* `LICENSE`: Feel free to use this code! Reach out to me if you are interested on collaborating on a better integration between hiplot and dash. 
* `README.MD`: Documentation file you are reading now.
* `/assets`: Images for `README.MD`

# To run the example
1. Clone this repository to your machine
2. Change to this working directory $`cd hiplot-dash-example`
3. Ensure conda is install by running $`conda --version`
    1. If conda is not installed follow instructions [here](https://docs.conda.io/en/latest/miniconda.html).
4. Install the conda environment  $`conda env create -f hiplot-dash-example.yml`
5. Run demonstration file $`bash run.sh`

# Screenshot of usage
![Usage](https://github.com/kravitsjacob/hiplot-dash-example/blob/main/assets/usage.PNG)
