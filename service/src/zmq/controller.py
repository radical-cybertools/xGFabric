
import radical.pilot as rp


# ------------------------------------------------------------------------------
#
class Controller(object):

    # --------------------------------------------------------------------------
    #
    def __init__(self):

        self._pilots = dict()


    # --------------------------------------------------------------------------
    #
    def get_initial_pilot(self):

      # if resources_are_cheap:
        if True:
            pd = rp.PilotDescription()
            pd.nodes = 1
            ...

            return pd


    # --------------------------------------------------------------------------
    #
    def get_pilot_description(self, data):

        if len(data) > 1000:

            pd = rp.PilotDescription()
            pd.nodes = 8
            ...

            return pd


# ------------------------------------------------------------------------------

