Various Command Line Tools

@author: Jean-Lou Dupont


* jldcmd-jwrite : write stdin JSON objects to target path
* jldcmd-wsniff : sniff 'beacon', 'probe request' and 'probe response' packets from an IEEE802.11 network interface
* jldcmd-wscan  : scan through 802.11 channels using a pattern


## jldcmd-jwrite

This command waits for line delimited JSON objects, constructs target file names from a pattern and writes the corresponding objects in the target path.  

`jldcmd-jwrite [-d] [-i] -tp targetPath -fp targetFilePattern` 

Where:
- `-d`   : debug mode
- `-i`   : ignore input line objects resulting in write error
- `-tp`  : the target base path to write the objects to
- `-fp`  : the file name pattern
- `-md5` : hash the resulting filename

The `file name pattern` is constructed using a string template with object keys has variables. Optionally, the resulting string can be hashed 
in order to accommodate potentially illegal file names.

Example usage:

`jldcmd-jwrite -i -tp /tmp/objs -fp "\$name-\$date" -md5`

The `\$` is used to espace the python string Template delimiter from bash/sh.

Would liste to stdin, decode each input line as JSON, use the value of the keys "name" and "date" to construct a filename md5 hashed, 
and finally write the corresponding object to the path `/tmp/objs/hashed_filename`.

## jldcmd-wsniff

This command listens for `beacon`, `probe request` and `probe response` packets from a WLAN interface and writes a JSON object 
on stdout with a number of information such as:

- sa :      source address
- da :      destination address (unless it is the broadcast address)
- bssid :   the access point's BSSID
- rssi :    the receive signal strength at this interface's antenna
- channel : the receive channel
- ssid :    the access point's SSID 

The specified WLAN interface must have been configured in `monitor` mode for the command to work :

- `ifconfig wlan0 down`
- `iwconfig wlan0 mode Monitor`
- `ifconfig wlan0 up`

Note that not all WLAN NICs support the `monitor` mode. For my tests, I have used a Panda Wireless USB dongle model PAU-03 which
includes a Ralink Technology chipset (USB device ID: 148f:5370).

## jldcmd-wscan

This command allows scanning 802.11 channels one by one using a pattern `channel:duration channel:duration ...`.

`jldcmd-wscan -iface wlan0 -p 1:5 6:10 11:5`  would scan channel 1 for 5 seconds, next on channel 6 for 10 seconds 
and finally channel 11 for 5 seconds before repeating the pattern.

History
=======

0.1 : initial release

