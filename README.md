# dblkp

A teensy python script for looking up server addresses from a list of IP addresses in markdown tables

## Installation

```
git clone https://github.com/tym-xqo/dblkp.git
chmod +x dblkp/dblkp.py
ln -s /full/path/to/dblkp/dblkp.py /usr/local/bin/dblkp
```

## Usage

- Edit `servers.md` as needed to suit your case (included lists are current for BenchPrep)
- `dblkp <database_hostname>`

If `database_hostname` is omitted, script returns the whole list. Otherwise you get just the IP you asked for
