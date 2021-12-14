const express = require("express");
var mqtt = require("mqtt");
const app = express();
app.use(express.static('public'));
var mqtt_message;

//Called on server creation
app.listen(8080, function(req, res)
{
    console.log("Server listen on 8080");
    client  = mqtt.connect("tcp://127.0.0.1:1883",{clientId:"dlm/display"});
    client.on('disconnect', function(){
        onConnectionLost();
    });
    client.on('message', function(topic,message){
    console.log("Message arrived on " + topic)
    onMessageArrived(res, topic, message);
    });
    client.on('connect', function(){
        onConnect();
    }); 
});

// Called when the client connects
function onConnect(){
    var topic = '#';
    client.subscribe(topic);
    console.log("Connected")
    //document.getElementById("messages").innerHTML + "Client Subscribbed" + '</span><br/>';
    //document.getElementById("messages").innerHTML + topic + message + '</span><br/>';
}

// Called when the client loses its connection
function onConnectionLost(responseObject) {
    document.getElementById("messages").innerHTML += '<span>ERROR: Connection lost</span><br/>';
    if (responseObject.errorCode !== 0) {
        document.getElementById("messages").innerHTML += '<span>ERROR: ' + + responseObject.errorMessage + '</span><br/>';
    }
}

// Called when a message arrives
function onMessageArrived(res, topic, message) {

    console.log("onMessageArrived: " + message);
    mqtt_message = message.toString();    
    //Parsing du message MQTT
    
    //Détection de la donnée
    switch((mqtt_message)){
        case "pieton":
            console.log("Pedestrian");
            break;
        case "voiture":
            console.log("Car");
            break;
        case "camion":
            console.log("Truck");
            break;
        case "velo":
            console.log("Bike");
            break;
        case "ligne":
            console.log("Line");
            break;
        case "feu_R":
            console.log("Red Light");
            break;
        case "feu_V":
            console.log("Green Light");
            break;
        case "vitesse":
            console.log("Speed limitation");
            break;
        case "plaque":
            console.log("Licence Plate");
            break;
        case "stop":
            console.log("Stop");
            break;
        case "ceder_pass":
            console.log("Give Way");
            break;
        case "sens_interd":
            console.log("No Entry");
            break;
        default:
            console.log("Unknown Detection");
    }
}




