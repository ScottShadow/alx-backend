export default function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((data) => {
      const Push3 = queue.create('push_notification_code_3', data).save((err) => {
        if (!err && Push3) {
          console.log(`Notification job created: ${Push3.id}`);
          Push3.on('complete', () => {
            console.log(`Notification job ${Push3.id} completed`);
          }).on('progress', (progress) => {
            console.log(`Notification job ${Push3.id} ${progress}% complete`);
          }).on('failed', (err) => {
            console.log(`Notification job $${Push3.id} failed: ${err}`);
          });
        } else {
          console.error('Failed to create job');
        }
      });

    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
