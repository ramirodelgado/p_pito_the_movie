#!/usr/bin/expect -f
set username [lindex $argv 0];
set password [lindex $argv 1];
send_user "$username $password"
