A script to fetch food data from Kanttiinit.fi API kitchen.kanttiinit.fi

Instructions:

- After first trial run, or by using the precompiled list, check list of restaurants from restaurants.txt

- touch .env, or rename .env.example to just .env

- make a comma-separated list of restaurants you want to queue to the environmental variables "RESTAURANTS"

- chmod +777 getdata.sh

- ./getdata.sh, and check data.txt for success