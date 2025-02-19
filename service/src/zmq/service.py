#!/usr/bin/env python3

'''
This file implements a xGFabric HPC service endpoint.  The service can be
contacted via a REST API.

    register() -> str

        REST: GET /register
        returns: a unique ID to identify the client on further requests.

        Register client and return a unique client ID.  That ID is required for
        all further requests.

      - use cookie instead of client id
      - add authorization and authentication
'''

from typing import List

import time

import radical.utils as ru
import radical.pilot as rp

from .controller import PilotController


# ------------------------------------------------------------------------------
#
class Client(ru.TypedDict):

    _schema = {
        'uid'    : str,              # client uid
        't_reg'  : float,            # registration time
        'data'   : str,              # fake input data

        'session': rp.Session,       # RP session etc.
        'pmgr'   : rp.PilotManager,
        'tmgr'   : rp.TaskManager,
        'pilot'  : rp.Pilot,
        }

    _defaults = {
        'uid'    : None,
        't_reg'  : None,
        'data'   : None,
        'session': None,
        'pmgr'   : None,
        'tmgr'   : None,
        'pilot'  : None,
        }


# ------------------------------------------------------------------------------
#
class xGFabric_EP(ru.zmq.Server):

    #---------------------------------------------------------------------------
    #
    def __init__(self, url: str):

        super().__init__(url)

        self._p_ctrl = PilotController()

        self._clients = dict()

        self.register_request('register',       self.register)
        self.register_request('register_fname', self.register_fname)


    # --------------------------------------------------------------------------
    #
    def start(self):

        super().start()
        print(self.addr)


    # --------------------------------------------------------------------------
    #
    def get_clients(self, uid:str) -> Client:

        assert uid in self._clients, 'unknown client [%s]' % uid
        return self._clients[uid]


    # --------------------------------------------------------------------------
    #
    def register(self) -> str:

        client = Client(uid=ru.generate_id('client'),
                        t_reg=time.time())

        self._clients[client.uid] = client

        self._log.info('client %s registered', client.uid)

        session = rp.Session()
        tmgr    = rp.TaskManager(session=session)
        pmgr    = rp.PilotManager(session=session)

        pd = self._p_ctrl.get_initial_pilot_description()

        if pd:
            pilot = pmgr.submit_pilots(pd)
            tmgr.add_pilots(pilot)

        client.session = session
        client.pmgr    = pmgr
        client.tmgr    = tmgr
        client.pilot   = pilot


        self._log.info('client %s session: %s', client.uid, session.uid)

        return client.uid


    # --------------------------------------------------------------------------
    #
    def register_fname(self, uid:str, fname: str) -> str:

        client = self.get_clients(uid)

        with open(fname) as fin:
            data = fin.read()

        tmgr = client.tmgr

        self._log.info('client %s registered %s', uid, len(data))

        pd = self._p_ctrl.get_pilot_description(data)

        if pd:
            pilot = self._pmgr.submit_pilots(pd)
            tmgr.add_pilots(pilot)

        tds = list()
        client.data = data
        td = rp.TaskDescription()
        td.executable = '/bin/echo'
        td.arguments  = ['DATA:', data]
        tds.append(td)

        tasks = tmgr.submit_tasks(tds)
        tmgr.wait_tasks()

        res = list()
        for task in tasks:
            res.append(task.stdout)

        self._log.info('client %s result: %s', uid, res)

        return str(res)


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    s = xGFabric_EP(url='tcp://*:10000-10020')
    s.start()
    s.wait()


# ------------------------------------------------------------------------------

