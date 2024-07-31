#!/usr/bin/env node
import redis from 'redis';

const client = redis.createClient({
	host: '127.0.0.1',
	port: 6379
});

client.on('error', (err) => {
	console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
	console.log(`Redis client connected to the server`);
});

const channel = 'holberton school channel';
client.subscribe(channel);

client.on('message', (channel, message) => {
	//console.log(`Received message from ${ channel }: ${ message }`);
	if (message === 'KILL_SERVER') {
		client.unsubscribe(channel);
		client.quit();
	}
});
