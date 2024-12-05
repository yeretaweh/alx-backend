import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Before each test, enter test mode
  beforeEach(() => {
    queue = kue.createQueue();
    kue.Job.rangeByType(
      'push_notification_code_3',
      'active',
      0,
      -1,
      'asc',
      (err, jobs) => {
        if (jobs) {
          jobs.forEach((job) => job.remove());
        }
      }
    );
    queue.testMode.enter();
  });

  // After each test, clear the queue and exit test mode
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs must be an array'
    );
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate that two jobs have been added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate the first job
    const firstJob = queue.testMode.jobs[0];
    expect(firstJob.type).to.equal('push_notification_code_3');
    expect(firstJob.data).to.deep.equal({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    });

    // Validate the second job
    const secondJob = queue.testMode.jobs[1];
    expect(secondJob.type).to.equal('push_notification_code_3');
    expect(secondJob.data).to.deep.equal({
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account',
    });
  });
});
