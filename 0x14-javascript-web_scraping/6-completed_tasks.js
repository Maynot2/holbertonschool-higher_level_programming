#!/usr/bin/node

const request = require('request');
const url = process.argv[2] || '';

request(url, function handleResponse (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completedById = {};
    for (const todo of todos) {
      const userId = todo.userId;
      if (todo.completed) {
        if (completedById[userId]) {
          completedById[userId] += 1;
        } else {
          completedById[userId] = 1;
        }
      }
    }
    console.log(completedById);
  }
});
