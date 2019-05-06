# Money CLI

> A simple command line interface made to quickly check the currency rates in the market with respect to a base currency of your choice.

> Made using the [Foreign exchange rates API](https://exchangeratesapi.io/) *with currency conversion*


### Installation

+ `git clone https://github.com/adityaa30/cli-money`
+ `cd cli-money`
+ `python setup.py install`

### Usage

```
usage: run.py [-h] [-l] [-b BASE] [-t TIME]

optional arguments:
    -h, --help              show this help message and exit
    -l, --list              List all the valid currency rates
    -b BASE, --base BASE    Base currency relative to which the currency rates are to be displayed
    -t TIME, --time TIME    Time of which the currency dates to be displayed (YYYY-MM-DD)
```