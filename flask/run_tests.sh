#!/usr/bin/env bash

echo "Start running test inside TA-flask container:"
echo "Can take as argument -su or --snapshot-update (reinitialise the snapshot)"

CONTAINER_NAME=${CONTAINER_NAME:-ta-flask}
CONTAINER_ID=$(${DOCKER} ps -aqf "name=${CONTAINER_NAME}")
echo ""
echo "CONTAINER_NAME ${CONTAINER_NAME}"
echo "CONTAINER_ID ${CONTAINER_ID}"
echo ""

SNAPSHOT_UPDATE=$1
if [ "${SNAPSHOT_UPDATE}" = "--snapshot-update" ]|| [ "${SNAPSHOT_UPDATE}" = "-su" ]; then
    echo "----"
    echo "The snapshot will be updated"
    echo "----"
    SNAPSHOT_UPDATE=--snapshot-update
fi

#If docker.exe is used, add an environment variable DOCKER=docker.exe to do the trick
DOCKER=${DOCKER:-docker}
${DOCKER} exec ${CONTAINER_ID} py.test . ${SNAPSHOT_UPDATE}
