import wifi

# Set the interface to use (e.g. wlan0)
interface = wifi.interface()

# Scan for available networks
networks = interface.scan()

# Print the list of available networks
for network in networks:
    print(network.ssid)

# Select the network you want to connect to
network_ssid = input('Enter the name of the network you want to connect to: ')
network_password = input('Enter the password for the network: ')

# Connect to the network
interface.connect(ssid=network_ssid, password=network_password)

# Check if the connection was successful
if interface.status() == wifi.WIFI_CONNECTED:
    print('Connected to', network_ssid)
else:
    print('Failed to connect to', network_ssid)
