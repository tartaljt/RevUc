#!/bin/sh

dnf install -y libpq-devel
cd /opt/mcs
pipreqs .
pip install -r requirements.txt