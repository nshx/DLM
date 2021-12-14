# Debian
Ubuntu 18.04 LTS ("Bionic")</br>

# Mosquitto MQTT Broker
## Installation
```
sudo apt update
sudo apt install mosquitto mosquitto-clients
```
Allow/disable mosquitto broker when device is turned on :
```
sudo systemctl (enable|disable) mosquitto
```

## Launch Mosquitto Broker
From Ubuntu shell :
`
sudo service mosquitto (start|stop)
mosquitto --verbose
`
By default, Mosquitto broker listens on port 1883
![image](https://user-images.githubusercontent.com/92402906/145909476-255130fd-8a60-49ff-90b9-9c56cf0c27c1.png)

### Test/debug : subscriber
`
mosquitto_sub -t <topic>
`
Assert payloads are decoded and sent to the correct topic. 
![image](https://user-images.githubusercontent.com/92402906/145909582-9008eafe-5ee4-4a29-b871-891bf18a2abe.png)

### Test/debug : publisher
`
mosquitto_pub -h localhost -P 1883 -t <topic> -m <message>
`
Simulate alerts (before node-red implementation)

# Node-red
Node-RED is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things.
## Installation
From Ubuntu Shell :
`
sudo apt install build-essential git curl
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered
`
note: first of all, it installs nodejs and npm before node-red

## Launch node-red
`
node-red
`
Once launched, node-red GUI is available at http://127.0.0.1:1880
![image](https://user-images.githubusercontent.com/92402906/145910656-a3c22296-c4e6-49f4-b55b-87cbc03fee32.png)
![image](https://user-images.githubusercontent.com/92402906/145910698-e2a593fd-7ace-461e-b717-7a13f579e601.png)
