const WebSocket = require("ws");
const PORT = process.env.PORT || 3001;

const server = require("http").createServer();
const wss = new WebSocket.Server({ server });

console.log(`🟢 WebSocket server live on port ${PORT}`);

function getRandomThreat() {
  const baseLat = 13.0;
  const baseLng = 80.2;
  return {
    lat: +(baseLat + (Math.random() - 0.5) * 0.4).toFixed(4),
    lng: +(baseLng + (Math.random() - 0.5) * 0.4).toFixed(4),
    risk: +(Math.random()).toFixed(2)
  };
}

setInterval(() => {
  const threat = getRandomThreat();
  const msg = JSON.stringify(threat);
  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(msg);
    }
  });
}, 5000);

server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
