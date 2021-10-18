#!/bin/bash

# This file is part of DRK Antikoerpererfassung.

echo "Starting Reminding"
cd /home/webservice/Antikoerpererfassung/AppointmentReminderJob
python3 job.py $(date '+%Y-%m-%d')
echo "Reminding complete"