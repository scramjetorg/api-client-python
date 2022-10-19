#!/bin/bash
mkdir -p refapps/
cd refapps/
wget -q 'https://api.github.com/repos/scramjetorg/reference-apps/releases/latest' -O - | jq -r '.assets[].browser_download_url' | xargs -n 4 -P ${MAX_PARALLEL:-$(nproc)} wget -q -nc
