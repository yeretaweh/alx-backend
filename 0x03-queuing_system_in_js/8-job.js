export default function createPushNotificationsJobs(jobs, queue) {
  // Check if the argument 'jobs' is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs must be an array');
  }

  // Loop through each job in the 'jobs' array
  jobs.forEach((jobData) => {
    // Create a job in the 'push_notification_code_3' queue
    const job = queue.create('push_notification_code_3', jobData);

    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Listen for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Listen for job failure
    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Listen for job progress updates
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} is ${progress}% complete`);
    });
  });
}
