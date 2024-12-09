#!/usr/bin/env python3

import radical.utils as ru


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    c = ru.zmq.Client(url='tcp://localhost:10000')

    uid = c.request('register')
    print(1, c.request(cmd='register_data', uid=uid, urls=['http://example.com']))


# ------------------------------------------------------------------------------

