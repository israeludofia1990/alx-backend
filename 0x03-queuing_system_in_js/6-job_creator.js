#!/usr/bin/env node
import Kue from 'kue';
import redis from 'redis';

// Create a Redis client
const redisClient = redis.createClient({
	host: '127.0.0.1',
	port: 6379
});

// Create a Kue queue
const queue = Kue.createQueue({
	redis: { host: '127.0.0.1', port: 6379 }
});

// define job data
const jobData = {
	phoneNumber: '1234567890',
	message: 'This is a notification message.'
};

const job = queue.create('push_notification_code', jobData);
job.save((err) => {
	if (err) {
		console.error('Error creating job:', err);
	} else {
		console.log(`Notification job created: ${job.id}`);
	}
});

job.on('complete', () => {
	console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
	console.error(`Notification job failed: ${errorMessage}`);
});
