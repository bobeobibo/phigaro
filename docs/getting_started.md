## Getting Started
### Docker, Singularity
You can avoid all the installation and setup process by loading Phigaro in a prebuilt container. Now, Phigaro is available in [Docker](https://github.com/bobeobibo/phigaro/blob/master/Dockerfile) and [Singularity](https://github.com/bobeobibo/phigaro/blob/master/Singularity)! 
You can find `Dockerfile` and `Singularity` files for creating images at this repository.
Some useful paths in containers:
```
phigaro: /root/miniconda3/bin/phigaro
config.yml: /root/.phigaro/config.yml
test_data: /test_data
```

---
### Requirements
* **Python**: Python 3+.<br>
*Python 2.7 is available, but it is no longer supported.*
	* `pip` utility is also required (`sudo apt-get install python-pip` on Ubuntu).


* **Prodigal**: Download it from 
[https://github.com/hyattpd/Prodigal/wiki/installation](https://github.com/hyattpd/Prodigal/wiki/installation) 
and follow the instructions.

* **HMMER**: Download it from [http://hmmer.org/](http://hmmer.org/)

* **locate**: In order to install Phigaro, you need `locate`. 
 	- It is present in the latest Ubuntu distributions, 
but in case you don't have it, install it with `sudo apt-get install locate`.
 	- For MacOS, you may need to add the following softlink `ln -s /usr/libexec/locate.updatedb /usr/local/bin/updated` and `run brew install wget`.

---
### Installation
##### Via pip
```
pip3 install phigaro --user
```
##### Via conda
```
conda env create -f environment.yml
conda activate phigaro_env
```
Where environment.yml can be downloaded form this repository or created manually:
```
name: phigaro_env
dependencies:
  - python=3.7
  - pip
  - bioconda::prodigal
  - bioconda::hmmer
  - pip:
    - phigaro
```

---
### Setup
Create a config file with:
```
phigaro-setup
```
It may take some time, since you are downloading the databases.

##### Rootless Mode
By default, root permissions are required for the installation. But you can disable it by adding a flag to `phigaro-setup`:
```
phigaro-setup --no-updatedb
```

##### Manual Setup
Also, you can manually create/change a `config.yml` file and write the `hmmer`, `prodigal` and `pvogs` paths like it is done in an example below. Other parameters should stay the same for the proper work of Phigaro unless you want to change them on purpose.

For the `pvogs` you should download all the files to the `pvog` (or any other folder) via the [link](http://download.ripcm.com/phigaro/) unless it wasn't done previously by `phigaro-setup`.

The content of the `config.yml` file could be found in [the repository](https://github.com/bobeobibo/phigaro/blob/master/config.yml) or can be copied from down here. It is possible that you may need to change the following paths:
<ul>
<li> `hmmer: bin` </li>
<li> <code>hmmer: pvog_path </code> </li>
<li> `prodigal: bin` </li>
</ul>

```  
hmmer:
  bin: /usr/local/bin/hmmsearch
  e_value_threshold: 0.00445
  pvog_path: /root/.phigaro/pvog/allpvoghmms
phigaro:
  mean_gc: 0.46354823199323625
  penalty_black: 2.2
  penalty_white: 0.7
  threshold_max_abs: 52.96
  threshold_max_basic: 46.0
  threshold_max_without_gc: 11.42
  threshold_min_abs: 50.32
  threshold_min_basic: 45.39
  threshold_min_without_gc: 11.28
  window_len: 32
prodigal:
  bin: /root/miniconda3/bin/prodigal
```
 
!!! Note 
	If you use Phigaro version 2.1.x or lower (for some reason) you should use `config_old.yml` file, that you can find via [the link](https://github.com/bobeobibo/phigaro/blob/master/config_old.yml).
 



##### All Options
Moreover, you may want to change a path of a config installation file or reconfigurate your Phigaro by adding special flags:
```
phigaro-setup --help
usage: phigaro-setup [-h] [-c CONFIG] [-p PVOG] [-f] [--no-updatedb]

Phigaro setup helper

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to a config.yml, default is
                        /home/polly/.phigaro/config.yml (default:
                        /home/polly/.phigaro/config.yml)
  -p PVOG, --pvog PVOG  pvogs directory, default is /home/polly/.phigaro/pvog
                        (default: /home/polly/.phigaro/pvog)
  -f, --force           Force configuration and rewrite config.yml if exists
                        (default: False)
  --no-updatedb         Do not run sudo updatedb (default: False)
```
