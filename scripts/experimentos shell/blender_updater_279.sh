#!/bin/bash
echo ' ip inicial '
read START
echo ' ip final '

read END
for i in $(eval echo "{$START..$END}")
do 
	ip="10.10.10.$i"
	echo "$ip"	
	echo ""
	echo "conectando a $ip"
	ssh -t "render@$ip" '/mnt/z/scripts/blender_update_279.sh'
	
#	CIP="10.10.10.$i"
#	echo "$CIP"
done







