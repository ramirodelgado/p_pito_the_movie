#!/usr/bin/expect -f
#set USER [lindex $argv 0];
set NP [lindex $argv 0]
#set PASS [lindex $argv 2];
set PROG blender

set USER render
set IP 10.10.10.$NP
set PASS Cambiame2016
spawn ssh -XC $USER@$IP
expect  "assword:"
send "$PASS\r"
expect ":~$ "
send "/mnt/y/ss.sh -a \r"
#send "sudo $PROG '/home/render/.config/blender/2.77/config/startup.blend' -noaudio -y -f 11 \r"


interact
#interact
#expect "$"
#send "popo\r"
#expect "password:"
#send "$pw\r"
#expect "#"
