#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    // Iterate through the tasks
    tasks.forEach((task) => {
      // Check if task is completed
      if (task.completed) {
        // Check if task is present in completedTasks
        if (completedTasks[task.userId]) {
          // Increment the count for that task
          completedTasks[task.userId] += 1;
        } else {
          // Task does not exist. Add it to completedTasks
          completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
