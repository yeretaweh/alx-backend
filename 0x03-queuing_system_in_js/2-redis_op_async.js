import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connect
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Promisify the Redis get method
const getAsync = promisify(client.get).bind(client);

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to get the value for a given key in Redis
async function displaySchoolValue(schoolName) {
  try {
    // Await the result of the promisified get method
    const value = await getAsync(schoolName);
    console.log(value); // Log the value from Redis
  } catch (err) {
    console.error('Error retrieving value:', err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
