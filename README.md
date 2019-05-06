# Money CLI

> A simple command line interface made to quickly check the currency rates in the market with respect to a base currency of your choice.

> Made using the [Foreign exchange rates API](https://exchangeratesapi.io/) *with currency conversion*

> Github repo of exchange rates API: [exchangeratesapi](https://github.com/exchangeratesapi/exchangeratesapi)


### Installation

+ `git clone https://github.com/adityaa30/cli-money`
+ `cd cli-money`
+ `pip install -r requirements.txt`

### Usage

```
usage: python run.py [-h] [-l] [-b BASE] [-t TIME]

optional arguments:
    -h, --help              show this help message and exit
    -l, --list              List all the valid currency rates
    -b BASE, --base BASE    Base currency relative to which the currency rates are to be displayed
    -t TIME, --time TIME    Time of which the currency dates to be displayed (YYYY-MM-DD)
```

### Examples
+ Fetch all latest currency exchange rates taking base currency as Indian Rupee
```bash
python run.py --base=inr
```
+ Fetch all latest currency exchange rates at a required time
```bash
python run.py --base=inr --time=2019-08-01
```
+ List out all the possible currency codes
```bash
python run.py --list
```