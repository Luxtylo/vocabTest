vocabTest
=========

Python program for a French teacher to create vocabulary tests for his students, and for the students to take them

The teacher's program needs to be able to create tests, which are stored somewhere the students can access. The tests will always be a French word or phrase and its English translation. To avoid confusion, the answers should be compared with the questions in lowercase.

The students' program should be able to download a file created by the teacher's program (so a small server would be needed to serve up the files). It will list the French words, and the student will need to correctly input their translation. There will always be 10 questions in the test, which is few enough to show them all at once. After the student has put in their answers, the program should give them a total score.

Both sides of the program need a GUI. The creation program will not be distributed to the students, and so does not require a login, but the student part needs a secure login option to prevent students impersonating each other. The student client should send their result to the server.
