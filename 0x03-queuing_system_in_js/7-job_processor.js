import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress as 0% at the start
  job.progress(0, 100);

  // Check if the phoneNumber is in the blacklisted array
  if (blacklistedNumbers.includes(phoneNumber)) {
    // If blacklisted, fail the job
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track job progress to 50%
  job.progress(50, 100);

  // Log notification sending
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // Complete the job successfully
  done();
}

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs from the 'push_notification_code_2' queue with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
