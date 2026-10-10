
const http = require("http");

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/html"
    });

    res.end(`
        <h1>Hello Ritik!</h1>
        <h2>Node.js Server is Running</h2>
        <p>Welcome to GitHub Codespaces.</p>
    `);
});

server.listen(3000, () => {
    console.log("Server running on port 3000");
});
