#!/bin/bash

LOG_DIR="/home/cowrie/cowrie/var/log/cowrie"
TTY_DIR="/home/cowrie/cowrie/var/lib/cowrie/tty"

DR="15"
DD="30"

FILES_DEL_LOG=$(find "$LOG_DIR" -type f ! -name ".git*" -mtime +"$DD" -print)
FILES_DEL_TTY=$(find "$TTY_DIR" -type f ! -name ".git*" -mtime +"$DD" -print)

FILES_ROT_LOG=$(find "$LOG_DIR" -type f ! -name ".git*" -mtime +"$DR" -print)
FILES_ROT_TTY=$(find "$TTY_DIR" -type f ! -name ".git*" -mtime +"$DR" -print)

echo -e "\n$(date +'%F %T')\n"
if [[ -n "$FILES_DEL_LOG" ]] ; then
        echo "Removing files older then "$DD" days from LOGS"
        echo -e "$FILES_DEL_LOG\n"
        find "$LOG_DIR" -type f ! -name ".git*" -mtime +"$DD" -delete


else
        echo -e "LOG files for deleting not found\n"

fi


if [[ -n "$FILES_ROT_LOG" ]] ; then
        echo "Rotating files older then "$DR" days from LOGS"
        echo -e "$FILES_ROT_LOG\n"
        find "$LOG_DIR" -type f ! -name ".git*" -mtime +"$DR" -exec gzip {} \;

else
        echo -e "LOG files for rotating not found\n"

fi


if [[ -n "$FILES_DEL_TTY" ]] ; then
        echo "Removing files older then "$DD" days from TTY"
        echo "$FILES_DEL_TTY\n"
        find "$TTY_DIR" -type f ! -name ".git*" -mtime +"$DD" -delete
else
        echo -e "TTY files for deleting not found\n"
fi




if [[ -n "$FILES_ROT_TTY" ]] ; then
        echo "Rotating files older then "$DR" days from TTY"
        echo "$FILES_ROT_TTY\n"
        find "$TTY_DIR" -type f ! -name ".git*" -mtime +"$DR" -exec gzip {} \;
else
        echo -e "TTY files for rotating not found\n"
fi

