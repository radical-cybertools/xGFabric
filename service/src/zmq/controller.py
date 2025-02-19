
import radical.pilot as rp


# ------------------------------------------------------------------------------
#
class PilotController(object):

    # --------------------------------------------------------------------------
    #
    def __init__(self):

        self._pilots = dict()


    # --------------------------------------------------------------------------
    #
    def get_initial_pilot_description(self):

      # if resources_are_cheap:
        if True:
            pd = rp.PilotDescription()
            pd.resource = 'xgfabric.vslurm'
            pd.nodes    = 1
            pd.runtime  = 600

            return pd


    # --------------------------------------------------------------------------
    #
    def get_pilot_description(self, data=None):

        if data and len(data) > 1000:

            pd = rp.PilotDescription()
            pd.nodes = 8
            ...

            return pd


# ------------------------------------------------------------------------------

