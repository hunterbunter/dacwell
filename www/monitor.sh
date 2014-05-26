#!/bin/bash
cd /home/dac/well/www
response=$(curl --write-out %{http_code} --silent --output /dev/null http://dacwell.com)
if [[ $response = "502" ]]; then
	echo "Server reporting bad gateway, restarting"
	./stop
	./stop
	./start
else
	echo "Server doing just fine"
fi
