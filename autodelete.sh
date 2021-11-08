#!/bin/bash



echo "Updating library..."

curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc

echo "Wait 1 minute to sync everything..."
sleep 60

echo "Cleaning library..."
curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "mybash"}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc


now=$(date +"%Y%m%d_%H:%I_autodelete.log")



mkdir -p log
python autodelete.py >> log/$now







echo "Updating library one more time..."

curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc

echo "Wait 1 minute to sync everything..."
sleep 60

echo "Cleaning library..."
curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "mybash"}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc

exit
