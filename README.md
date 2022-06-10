# Password project setup
## Setup

Make sure you have the latest version of Python installed.

The postgres user needs to have the same as the password in ```config.json```:

```bash
sudo -su postgres psql
```
```bash
\password
```
Copy and paste the password and do:

```bash
\q
```

Alternatively change the password in ```config.json``` to the one the postgres user uses.

To install the necessary packages:

```bash
pip install -r Requirements.txt
```


## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://127.0.0.1:5001`


## Interaction With The App

click the different buttons and have fun:)))
