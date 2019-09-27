#!/usr/bin/env python
# -*- coding: utf-8 -
import os
from argparse import ArgumentParser

LISTPATH = os.path.dirname(os.path.realpath(__file__))


def get_server_list():
    with open("{}/servers.md".format(LISTPATH)) as f:
        svrs = f.readlines()
    svrs = [i for i in svrs if "169" in i]
    svrs = [[i.strip() for i in l] for l in [i.split("|")[1:4] for i in svrs]]
    return svrs


def get_ip(db):
    # TODO: allow choice between public or private IP
    dbs = get_server_list()
    if not db:
        return "\n".join([" | ".join(i) for i in dbs])
    ip = [i[2] for i in dbs if db in i][0]
    return ip


def handle():
    parser = ArgumentParser()
    parser.add_argument("db", default=None, nargs="?")
    args = parser.parse_args()
    db = args.db
    ip = get_ip(db)
    if db:
        print("{db}: {ip}".format(db=db, ip=ip))
        return
    print(ip)


if __name__ == "__main__":
    handle()
