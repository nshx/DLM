const express = require("express");
var mqtt = require("mqtt");
var fs = require("fs").promises;
const app = express();
app.use(express.static('./public'));
var mqtt_message;
var CC;
var TT;
var DDDD;

//Called on server creation
app.listen(8080, function(req, res)
{
    console.log("Server listen on 8080");
    client  = mqtt.connect("tcp://127.0.0.1:1883",{clientId:"dlm_hud"});
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

    //console.log("onMessageArrived: " + message);
    //console.log("" + message);
    mqtt_message = message.toString();    
    //Parsing du message MQTT
    CC = mqtt_message.substring(0,2);
    TT = mqtt_message.substring(2,4);
    DDDD = mqtt_message.substring(4,8);
    
    //console.log(CC);
    //console.log(TT);
    //console.log(DDDD);
    
    //Détection de la caméra
    switch((CC)){
        case "00":
            console.log("FRONT CAM");
            break;
        case "01":
            console.log("BACK CAM");
            break;
        default:
            console.log("Unknown Cam");
    }

    //Détection du type d'alerte
    switch((TT)){
        case "00":
            console.log("Info");
            break;
        case "01":
            console.log("Warning");
            break;
        case "10":
            console.log("Critical");
            break;
        case "11":
            console.log("Unknown Type");
            break;
        default:
            console.log("Unknown Type");
    }
    
    //Détection de la donnée
    switch((DDDD)){
        case "0000":
            console.log("Pedestrian");
            break;
        case "0001":
            console.log("Car");
            break;
        case "0010":
            console.log("Truck");
            break;
        case "0011":
            console.log("Bike");
            break;
        case "0100":
            console.log("Line");
            break;
        case "0101":
            console.log("Red Light");
            break;
        case "0110":
            console.log("Green Light");
            break;
        case "0111":
            console.log("Speed limitation");
            break;
        case "1000":
            console.log("Licence Plate");
            break;
        case "1001":
            console.log("Stop");
            break;
        case "1010":
            console.log("Give Way");
            break;
        case "1011":
            console.log("No Entry");
            break;
        default:
            console.log("Unknown Detection");
    }
}
