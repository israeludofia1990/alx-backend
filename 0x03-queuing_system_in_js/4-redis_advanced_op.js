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
	console.log('Redis client connected to the server');
});

const createHash = () => {
	const hashKey = 'HolbertonSchools';
	const hashValues = {
		Portland: 50,
		Seattle: 80,
		'New York': 20,
		Bogota: 20,
		Cali: 40,
		Paris: 2
	};
	for (const [field, value] of Object.entries(hashValues)) {
		client.hset(hashKey, field, value, redis.print);
	}
};

const displayHash = () => {
	const hashKey = 'HolbertonSchools';
	client.hgetall(hashKey, (err, result) => {
		if (err) {
			console.error(err);
		} else {
			console.log(result);
		}
	});
};

//client.on('connect', () => {
//	console.log('Redis client connected to the server');
	createHash();
	displayHash();
//});
