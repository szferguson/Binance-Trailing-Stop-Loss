# Binance-Trailing-Stop-Loss
Provides a dynamic stop-loss that automatically adjusts as the price increases or decreases (depending on mode specified)

## Installation
Clone the repository
`git clone https://github.com/sf04/Binance-Trailing-Stop-Loss`

Install required libraries
```
apt-get install python-pip -y
pip install ccxt
```

## Running

# Usage
```
$ python main.py --help
usage: main.py [-h] --symbol SYMBOL --size SIZE --type TYPE
               [--interval INTERVAL]

optional arguments:
  -h, --help           show this help message and exit
  --symbol SYMBOL      Market Symbol (Ex: NEO/BTC - NEO/USDT)
  --size SIZE          How many satoshis (or USD) the stop loss should be
                       placed above or below current price
  --type TYPE          Specify whether the trailing stop loss should be in
                       buying or selling mode. (Ex: 'buy' or 'sell')
  --interval INTERVAL  How often the bot should check for price changes
```

# Important note
If you are running in sell mode, it is assumed that you have already purchased the coins. If you are running in buy mode, it will use the total available balance in the base (USDT, BTC, etc). I will likely add an option later to specify investment ratio.


## About the bot

# Buy mode
If the **buy** option is set, the bot will initially place a stop-loss `size` satoshis (or USD) **above** the current market price. As the price goes lower, the stop-loss will get dragged with it, staying no higher than the size specified. Once the price crosses the stop-loss price, a buy order is executed.

# Sell mode
If the **sell** option is set, the bot will initially place a stop-loss `size` satoshis (or USD) **below** the current market price. As the price goes higher, the stop-loss will get dragged with it, staying no lower than the size specified. Once the price crosses the stop-loss price, a sell order is executed.

# Size
This is the amount in satoshis (or USD) you would like the stop-loss to be retained at. The difference between the current price and stop-loss will never be larger than this amount.

## License
Copyright (c) 2018 Steven Ferguson, released under GPLv3.
