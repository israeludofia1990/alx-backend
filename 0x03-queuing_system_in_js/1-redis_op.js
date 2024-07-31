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

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (err, reply) => {
		if (err) {
			console.error(`Error fetching value for ${schoolName}: ${err.message}`);
		} else {
			console.log(`${reply}`);
		}
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
