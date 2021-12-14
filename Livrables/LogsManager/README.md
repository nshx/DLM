### Debian
Ubuntu 18.04 LTS ("Bionic")</br>

### Mosquitto MQTT Broker
# Installation
```
sudo apt update
sudo apt install mosquitto mosquitto-clients
```
Pour autoriser/désactiver le broker mosquitto à chaque démarrage :
```
sudo systemctl (enable|disable) mosquitto
```
# Broker
Depuis une invite de commande :
`
sudo service mosquitto (start|stop)
mosquitto --verbose
`
Le broker écoute tout message qui arrive sur le port 1883
![image](https://user-images.githubusercontent.com/92402906/145909476-255130fd-8a60-49ff-90b9-9c56cf0c27c1.png)
# Test/debug : subscriber
`
mosquitto_sub -t <topic>
`
Utile pour vérifier la redirection correcte des trames décodées vers le display.
![image](https://user-images.githubusercontent.com/92402906/145909582-9008eafe-5ee4-4a29-b871-891bf18a2abe.png)
# Test/debug : publisher
`
mosquitto_pub -h localhost -P 1883 -t <topic> -m <message>
`
Utile pour simuler l'arrivée d'alerte (avant l'implémentation du serveur node-red).

### Node-red
```
sudo apt install build-essential git curl
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered
```
