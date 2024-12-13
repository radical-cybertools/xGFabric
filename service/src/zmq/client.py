#!/usr/bin/env python3

import sys

import radical.utils as ru


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    addr  = sys.argv[1]
    fname = sys.argv[2]

    with open(fname) as fin:
        data = fin.read()

    c = ru.zmq.Client(url=addr)

    uid = c.request('register')
    result = c.request('register_data', uid=uid, data=data)

    print(1, c.request(cmd='register_data', uid=uid, urls=['http://example.com']))


# ------------------------------------------------------------------------------

