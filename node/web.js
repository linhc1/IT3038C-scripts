const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
  var sec = os.uptime();
  var min = sec/60;
  var hour = min/60;
  var day = hour/24;
  
  sec = Math.floor(sec);
  min = Math.floor(min);
  hour = Math.floor(hour);
  day = Math.floor(day);
	  
  day = day%24
  hour = hour%60
  min = min%60
  sec = sec%60
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${"Days:" + day + ", Hours:" + hour + ", Minutes:" + min + ", Seconds:" + sec}</p>
        <p>Total Memory: ${os.totalmem()/1024/1024 + "MB"} </p>
        <p>Free Memory: ${os.freemem()/1024/1024 + "MB"}</p>
        <p>Number of CPUs: ${os.cpus().length} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
