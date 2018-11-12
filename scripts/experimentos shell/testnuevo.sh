

#!/bin/bash
echo ' ip inicial '
read START
echo ' ip final '

read END
for i in $(eval echo "{$START..$END}")
do
	echo "$ip"	
	echo ""
	echo "conectando a $ip"

	ip="10.10.10.$i"
	gnome-terminal -e ssh -t "render@$ip"
	'/mnt/y2/ss.sh'&
	
	
	
	
#	CIP="10.10.10.$i"
#	echo "$CIP"
done
