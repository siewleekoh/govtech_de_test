# Govtech Data Engineer Tech Challenge


## Section 1: Data Pipelines
The data pipeline python script will be run by a cron job in a shell script, `load_data.sh`.

The main data processing python script is `main.py`.


### Setup python environment
1) In the terminal, change the working directory to the where the project folder is in the command line.  

   ```console
   cd C:\Users\xxx\govtech_de_test\
   ```

2) Create a virtual environment.
```console
virtualenv -p python3 myenv
```

3) Activate the virtual environment
```console
source myenv/bin/activate
```

4) Install all packages from the `requirements.txt`.
 ```console
 pip install -r requirements.txt

 ```



### Change working directory to the directory where the csv file will be in `load_data.sh`
```console
export DIR=/home/xxx
```

### Setting up cron job to run the bash script.
1) Open crontab in linux terminal.  
```console
crontab -e
```

2) Set the shell script to run everyday at 1.20 am and save the run log by date.
```console
20 1 * * * /cron_scripts/load_data.sh > $HOME/`date +\%Y\%m\%d\%H\%M\%S`-load_data.log 2>&1
```
