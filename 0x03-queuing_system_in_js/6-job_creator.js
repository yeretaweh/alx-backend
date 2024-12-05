import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Define job data - phone number and message in this case
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the message for the notification',
};

// Create a job in the queue 'push_notification_code'
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.log('Notification job failed to create');
  }
});

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
