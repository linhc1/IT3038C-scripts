#!/bin/bash

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
DEATHS=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')
HOSPITALIZED=$(curl  https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATHS deaths and $HOSPITALIZED hospitalized."
