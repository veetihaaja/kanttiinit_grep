A script to fetch food data from Kanttiinit.fi API kitchen.kanttiinit.fi. getMap.py fetches the current mapping between all restaurants and their ID, and menuGet.py gets the relevant menus specified in .env.

Instructions:

- After first trial run, or by using the precompiled list, check list of restaurants from restaurants.txt

- touch .env, or rename .env.example to just .env

- make a comma-separated list of restaurants you want to queue to the environmental variables "RESTAURANTS"

- python3 -m venv .venv
	- source .venv/bin/activate

- pip install -r requirements.txt

- chmod +777 getdata.sh

- ./getdata.sh, and check data.txt for success
