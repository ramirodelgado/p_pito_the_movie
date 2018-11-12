#!/usr/bin/expect -f
#set USER [lindex $argv 0];
set NP [lindex $argv 0]
#set PASS [lindex $argv 2];
set USER render
set IP 10.10.10.$NP
set PASS pepito1234
spawn ssh -t $USER@$IP
expect  "sword:"
send "$PASS\r"
expect ":~$ "
send "/mnt/y/scripts/blender_filmic_render.sh -a \r"
expect  "ender:"
send "$PASS\r"



interact

