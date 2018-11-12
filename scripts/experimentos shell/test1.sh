#!/usr/bin/expect -f
set times 101;
set LOGIN [lindex $argv 0];
set PASS [lindex $argv 1];
while { $times < 125 } {
   set IP 10.10.10.$times
   
   spawn ssh $LOGIN@$IP

   expect {
       "assword:" { send "PASS" }
	   send 'clear'
       
      
       #eof { }
       #timeout { puts "timeout waiting for response" ; close ; exit }
   }
   set times [ expr $times+1];
}






