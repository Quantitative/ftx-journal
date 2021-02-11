## What it does: ##

grabs USD balance on FTX every 10 minutes, can change this though below

then u can plot a nicey nicey equity curve with it


## How to set it up: ##

**IMPORTANT:**
Before anything, make sure to setup a postgreSQL database with heroku (this is just easy tbh)
Tutorial: https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1


Setup a VPS on Vultr (any VPS provider works) running ubuntu 20.04

Connect to it through some sort of SSH terminal or however u want to connect to it

*you will need to install pip, npm and pm2

1. **git clone https://github.com/Quantitative/ftx-journal.git**

2. cd ftx-journal

3. bash init.sh

4. copy the contents of the dotenv_template.txt file

5. paste the contents from the template in a new file called ".env" fill out each variable

6. The FTX API keys are key/secret read-only FTX API keys

7. The Database details can be taken from your heroku database, check tutorial or google how to find database credentials on heroku postgreSQL

**Note:** If you want to change the time at which balance is grabbed make sure to edit the --cron in init.sh (where the PM2 job is starting), look up how cronjobs work to do this


