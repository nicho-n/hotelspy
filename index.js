var express = require("express");
var app = express();

var http = require("http");
var server = http.Server(app);

var socketio = require("socket.io");
var io = socketio(server);

var location = "Marquette, MI, United States"
var checkin = "2018-06-25"
var checkout = "2018-06-26"
var spawn = require('child_process').spawn

app.use(express.static("pub"));

io.on('connection', function(socket){


  socket.on('request', function(request){
     location = request[0];
     checkin = request[1];
     checkout = request[2];
     console.log("ok");
     var py=spawn('python3', ['hotels.py', location, checkin, checkout]),
     dataString = '';

     py.stdout.on('data', function(data){
        console.log(data.toString())
        socket.emit("data", data.toString())
     });
  });
});


server.listen(4041, function(){
  console.log('listening on *:4041');
});
