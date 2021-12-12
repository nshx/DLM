UBUNTU 20.04 LTS (Focal Fossa)\\
Node-JS v14.x : https://github.com/nodesource/distributions/blob/master/README.md\\
`
# Using Ubuntu
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
`
Node-RED https://nodered.org/docs/getting-started/local
Prerequisites
To install Node-RED locally you will need a supported version of Node.js.
Node-RED currently recommends Node 14.x LTS.

Installing with npm
To install Node-RED you can use the npm command that comes with node.js:
`
sudo npm install -g --unsafe-perm node-red
`
Mosquitto broker : https://mosquitto.org/download/
Mosquitto is available in the Ubuntu repositories so you can install as with any other package. If you are on an earlier version of Ubuntu or want a more recent version of mosquitto, add the mosquitto-dev PPA to your repositories list - see the link for details. mosquitto can then be installed from your package manager.
`
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
`
