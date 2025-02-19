
import radical.pilot as rp


# ------------------------------------------------------------------------------
#
class PilotController(object):

    # --------------------------------------------------------------------------
    #
    def __init__(self, pmgr, tmgr):

        self._pmgr = pmgr
        self._tmgr = tmgr
        self._pilots = dict()


    # --------------------------------------------------------------------------
    #
    def __del__(self):

        for pilot_id in self._pilots:
            self.cancel_pilot(pilot_id)


    # --------------------------------------------------------------------------
    #
    def _submit_pilot(self, nodes=1, runtime=600):

        pd = rp.PilotDescription()
      # pd.resource = 'xgfabric.vslurm'
        pd.resource = 'local.localhost'
        pd.nodes    = nodes
        pd.runtime  = runtime

        pilot = self._pmgr.submit_pilots(pd)

        self._tmgr.add_pilots(pilot)
        self._pilots[pilot.uid] = pilot

        return pilot.uid


    # --------------------------------------------------------------------------
    #
    def cancel_pilot(self, pilot_id):

        pilot = self._pilots.get(pilot_id)

        if pilot:
            pilot.cancel()
            del self._pilots[pilot_id]


    # --------------------------------------------------------------------------
    #
    def start_initial_pilot(self):

      # if resources_are_cheap:
        if True:
            return self._submit_pilot()


    # --------------------------------------------------------------------------
    #
    def start_pilot(self, data):

        if len(self._pilots) >=2:
            # don't start more than 2 pilots
            return

        if data and len(data) > 10:
            # large data set - start another pilot
            return self._submit_pilot(nodes=2, runtime=10)


# ------------------------------------------------------------------------------

