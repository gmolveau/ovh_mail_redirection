# OVH mail redirection via API

> WIP

- simple program to create a mail-redirection (in order to have a unique mail adresse by service)

1. create your API key > https://api.ovh.com/createToken/index.cgi?GET=/*&POST=/*
2. update `ovh.conf` file
3. run `python3 cli.py --help`

## Getting started

- clone this repo

```bash
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python3 cli.py --help
```

then

```bash
(venv) $ python3 cli.py list yourdomain.fr
# {
#     "from": "mail1@yourdomain.fr",
#     "id": "123456677",
#     "to": "redirectedmail@anotherdomain.fr"
# }
(venv) $ python3 cli.py generate facebook
# facebook-ly4sbyg0p5s6kydzn7tl8zuy6xfeilpw
(venv) $ python3 cli.py add -D yourdomain.fr -s newmail@yourdomain.fr -d redirect@anotherdomain.fr
# {
#     "action": "add",
#     "date": "2020-03-12T17:10:41+01:00",
#     "account": "testtest",
#     "type": "forward",
#     "domain": "yourdomain.fr",
#     "id": 123454321
# }
```
