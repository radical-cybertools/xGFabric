#!/bin/bash

# get data following Rich instruction
/sharedfs/cups-data/senspot-get -W woof://169.231.230.76/sharedfs/cups-data/daviscupsout

# Split velocity and direction on componets x and y, or get components if there is any


# Update files
python deleteme.py 3.8 0 0 --file angled_test_fixing
