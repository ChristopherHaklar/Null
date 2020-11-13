#######################################################################
## While loop to keep running the script
#######################################################################
while true; 

do
#######################################################################
## Curl the PS5 store webpage twice, 5 seconds apart
#######################################################################
CURLA=$(curl https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816 | grep "<p class="sony-text-body-1">Out of Stock</p>")
sleep 5
CURLB=$(curl https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816 | grep "<p class="sony-text-body-1">Out of Stock</p>")

if [ "$CURLA" = "$CURLB" ]; then
	printf '\033[0;31m PS5 Out of Stock \n' ## Changes text color to red then prints PS5 out of stock
	printf '\033[0m' ## Changes text color back to default
else
	printf '\033[0;32m  PS5 might be in stock \n' ## Changes text color to green then prints PS5 might be in stock
	printf '\a' ## Makes Windows Chime
	printf '\033[0m' ## Changes text color back to default
	printf '  Checked at this time: '
	date ## Prints the date and time
	tput bel ## Makes Windows Chime
	printf '  Waiting One Hour before stating to check again... \n'
	sleep 3600 ## Waits one hour before starting to check again
fi
#######################################################################
## Wait 5 seconds to run the request again
#######################################################################

sleep 5;

#######################################################################
## Exit Condition
#######################################################################
done
