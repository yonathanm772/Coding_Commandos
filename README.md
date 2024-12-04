## Product Name: KnightWallet

## 1. What is the software product?
The product that the coding commandos are going to develop is a finance app to help users manage their personal finances effectively. It provides tools for budgeting, tracking expenses, and monitoring financial goals.

## 2. Possible Names Considered
```
-KnightWallet 
-KnightFund
-KnightTrack
```

## 3. Final Chosen Name
We decided to go with the name KnightWallet because it relates to our target group and identifies the type of app we are going to develop.

## 4. Potential Customers, End Users, or Buyers
Our target customers are going to be college students who want to save and spend money effectively while in college, but our app can be used by anyone country wide that wants to learn how to budget.

## 5. Potential Features and Functions
The features we are going to potentially incorporate a budgeting tool that will allow students to learn how to budget effectively, how to save effectivly and manage any assets.
```
-A budgeting tool to help students learn how to budget effectively
-A savings feature to assist users in tracking their savings and assets
```

## 6. Product Vision Statement
Overall, our vision for our product is to empower college students to learn how to take control of their finances.  This is accomplished with a user-friendly finance app to take control of their finances with simple, intuitive tools.  We aim to help users achieve their financial goals and build a secure financial future.

## 7. Website
- link: https://jcfarese.github.io/Coding_Commandos/
- Design Video: https://video.bellarmine.edu/media/KnightWallet/1_f26jw0dy

  
## 8. Unit Testing
### Budget Tracker

This is a simple budgeting and spending tracker application built with Flask, containerized with Docker, and includes a separate container for running unit tests.

## Features
- Add and view transactions.
- Dockerized for easy setup and deployment.
- Includes basic unit tests.

---

## Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 9. Running the Application
##### 1. Clone the repository:
   - git clone https://github.com/jcfarese/Coding_Commandos.git
     
##### 2. Change Directory to knight-wallet
   - cd knight-wallet

##### 3. Setup the Docker Container
   - docker-compose down (deletes any active dockers)
   - docker-compose up --build (build the feature in a docker)
   - docker-compose up tests (runs the unit tests)

#### 4. Run the Docker Container
   - In the terminal open the port: http://127.0.0.1:5000

