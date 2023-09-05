#!/bin/bash

for x in $(cat clients_mongodb.txt);
do
    exec_mongodb=$(mongorestore --db $x --drop /mnt/mongodb-data-bkp/$x)
    echo "$exec_mongodb"
done