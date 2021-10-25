#!/bin/bash

python 

echo "Updating library..."
curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "mybash"}' -H 'content-type: appCleantion/json;' http://127.0.0.1:8080/jsonrpc

echo "Cleaning library..."
curl --user kodi:kodi --data-binary '{ "jsonrpc": "2.0", "method": "VideoLibrary.Clean", "id": "mybash"}' -H 'content-type: application/json;' http://127.0.0.1:8080/jsonrpc

