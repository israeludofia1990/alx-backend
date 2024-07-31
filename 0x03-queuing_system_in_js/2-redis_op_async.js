#!/usr/bin/env node
import { promisify } from 'util';
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

const getAsync = promisify(client.GET).bind(client);

const displaySchoolValue = async (schoolName) => {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (err) {
		console.error('Error:', err);
	}
};

client.on('connect', async () => {
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
});
