from ftxclient import FtxClient
from dotenv import dotenv_values
import sys, time


# This class will take care of the calls to the ftx client.
class FtxTests:

    def __init__(self) -> None:
        # Load the enviroment variables to be used by the script
        config = dotenv_values(".env")
        # Initialize the FtxClient to call it in the methods of our class
        self._ftxclient = FtxClient(config.get('API_KEY'), config.get('API_SECRET'))

    # This method calls get_market_info ('markets/{market}' endpoint) method in ftxclient and prints the response in console
    def get_market_info(self, market_name):
        while True:
            market_data = self._ftxclient.get_market_info(market_name)
            print(market_data)
            time.sleep(5)


# This is the main method, it will be called everytime we execute the following command 'python main.py'
if __name__ == '__main__':

    # Print a message explainig how to use this script
    print(f'Usage: python {sys.argv[0]}')

    # We initialize FtxTest class
    ftxclass = FtxTests()

    # Call to get BTC/USD market
    ftxclass.get_market_info('BTC/USD')


