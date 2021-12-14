# Debian
Ubuntu 18.04 LTS ("Bionic")</br>

# Mosquitto MQTT Broker
## Installation
```
sudo apt update
sudo apt install mosquitto mosquitto-clients
```
Enable/disable mosquitto broker when device is turned on :
```
sudo systemctl (enable|disable) mosquitto
```

## Launch Mosquitto Broker
From Ubuntu shell :</br>
```
sudo service mosquitto (start|stop)
mosquitto --verbose
```
By default, Mosquitto broker listens on port 1883</br>
![image](https://user-images.githubusercontent.com/92402906/145909476-255130fd-8a60-49ff-90b9-9c56cf0c27c1.png)

### Test/debug : subscriber
```
mosquitto_sub -t <topic>
```
Assert payloads are decoded and sent to the correct topic</br>
![image](https://user-images.githubusercontent.com/92402906/145909582-9008eafe-5ee4-4a29-b871-891bf18a2abe.png)

### Test/debug : publisher
```
mosquitto_pub -h localhost -P 1883 -t <topic> -m <message>
```
Simulate alerts (before node-red implementation)

# MongoDB Atlas - Remote free DB
## Register new account
https://www.mongodb.com/cloud/atlas/lp/general/try?utm_source=compass&utm_medium=product</br>
1. Create project: DLM</br>
2. Create user|pw</br>
3. Create cluster</br>
4. Create collection: logs</br>
5. Configure Network Access</br>
6. Get remote URL: Connect()</br>
![image](https://user-images.githubusercontent.com/92402906/145913907-7bf96ffb-2282-4085-bcd0-21da38af67cb.png)

## Mongo Shell
### Installation
```
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb-mongosh
```
### Start mongosh
```
mongosh "mongodb+srv://cluster0.t22mb.mongodb.net/DLM" --username <user>
```
![image](https://user-images.githubusercontent.com/92402906/145914954-4f443ea4-1477-43fa-92fc-f8a9e92d0b2a.png)

# Node-red
Node-RED is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things.
## Installation
From Ubuntu Shell :
```
sudo apt install build-essential git curl
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered
```
note: first of all, it installs nodejs and npm before node-red

## Launch node-red
```
node-red
```
Once launched, node-red GUI is available at http://127.0.0.1:1880</br>
![image](https://user-images.githubusercontent.com/92402906/145910656-a3c22296-c4e6-49f4-b55b-87cbc03fee32.png)
![image](https://user-images.githubusercontent.com/92402906/145910698-e2a593fd-7ace-461e-b717-7a13f579e601.png)

## mongodb dependency
From Ubuntu Shell:
```
cd ~/.node-red
npm install mongodb
vi setting.js
```
In the file setting.js, look for 'functionGlobalContext'</br>
press 'I' (insert) to enter the following line :</br>
![image](https://user-images.githubusercontent.com/92402906/145914616-90a45305-d4ed-4094-b27f-6d4569384ff0.png)</br>
press 'esc' ('echap') then write ':wq' to save the changes.
