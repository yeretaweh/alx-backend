import kue from 'kue';

const queue = kue.createQueue();

//Function to handle notification sending
function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

// Process the queue and listen for new jobs
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message);

  // Mark the job as done
  done();
});
