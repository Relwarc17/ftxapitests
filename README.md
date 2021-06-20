## Simple script to test the ftx python client

To install the dependencies run `pip install -r requirements.txt`

To use this script we first need to copy .env.example file to the root folder of the project and rename it to .env.  
We have to configure our FTX **api key** and **api secret** in **_.env_** file

At the moment this is simply a terminal running script to run it we just have to execute  
`python main.py`  
on the root of folder of this project.


The script is using the example client from FTX github repo  
https://github.com/ftexchange/ftx/tree/master/rest  

This client has functions to call the different endpoints from FTX API, I've added the method `get_market_info` to get info from a certain market.
More info for all this endpoints in FTX API docs:  
https://docs.ftx.com/