#!/bin/sh

pip install psycopg2-binary
cd /opt/mcs
pipreqs .
pip install -r requirements.txt