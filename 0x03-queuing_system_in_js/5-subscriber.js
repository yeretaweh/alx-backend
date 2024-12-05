import redis from 'redis';

// Create a Redis client for the subscriber
const subscriber = redis.createClient();

// Event handler for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Subscribe to the 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(message);

  // If the message is 'KILL_SERVER', unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
