#!/usr/bin/expect -f
#set USER [lindex $argv 0];
set NP [lindex $argv 0]
#set PASS [lindex $argv 2];

set USER render
set IP 10.10.10.$NP
set PASS Cambiame2016
spawn ssh -XC $USER@$IP
expect  "s password:"
send "$PASS\r"
expect '~$'
send "echo '//10.10.10.40/Pepito_Red /mnt/y cifs guest | sudo tee -a /etc/fstab\r"




interact
#interact
#expect "$"
#send "popo\r"
#expect "password:"
#send "$pw\r"
#expect "#"
