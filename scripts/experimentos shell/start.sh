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
#send "sudo mount -a \r"
#expect  "ender:"
#send "$PASS\r"
#expect ":~$ "
send "/mnt/z/ss.sh \r"
expect  "ender:"
send "$PASS\r"



interact

