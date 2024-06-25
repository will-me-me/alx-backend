import * as r from 'redis';

const client = r.createClient();

// Event handler for successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Event handler for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});
