import kue from 'kue'; 
import redis from 'redis'; 

// create Redis Client
const redisClient = redis.createClient({
	host: '127.0.0.1',
	port: 6379
});

const queue = kue.createQueue({
	redis: redisClient
});

const sendNotification = (phoneNumber, message) => {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
queue.process('push_notification_code', (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
	console.log('Job processor is running and listening for jobs...');
});
