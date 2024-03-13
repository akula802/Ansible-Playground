#!/bin/bash

# Place this script in /etc/dnf/plugins/post-transaction-actions.d/alert-dnf.action
# Make sure the extension is .action and make it executable


# Get a formatted timestamp
TIMESTAMP_NOW=`date +%m-%d-%y_%H:%M:%S`

# Create a file in /var/tmp that will persist for 30 days
FILENAME="/var/tmp/patchJob_$TIMESTAMP_NOW"
touch $FILENAME

# Get the last DNF transaction number
LAST_DNF_TRXN_ID=`dnf history | sed -n 4p | awk {'print $1'}`
dnf history info $LAST_DNF_TRXN_ID > $FILENAME

# Activate the venv
source "/scripts/venv/alert-dnf/bin/activate"

# Execute the python script
python3 /scripts/alert-dnf/send_email.py $FILENAME

