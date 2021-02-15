● Load Balancing - how would you distribute requests to your web application

- I assume that Load balancer will distribute requests in round-robin manner. Having said that, we can also configure the load-balancing algorithms to distribute requests based on the availability or traffic on end nodes in both clusters

● SSL support - where would you terminate SSL

- SSL can be terminated at the loadbalancer, and load balancer can handle the SSL encryption/decryption so that traffic between the load balancer and backend servers is in HTTP

● Database - how would you ensure data consistency from both active instances

- As sourced from (https://developer.mongodb.com/article/active-active-application-architectures/), we can adopt one of the following distributed database architectures for data consistency across active-active cluster

    1. Distributed transactions using two-phase commit
    2. Multi-Master, sometimes also called "masterless"
    3. Partitioned (sharded) database with multiple primaries each responsible for a unique partition of the data