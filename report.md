Domain - I got a free domain name from Freenom

NameServer - I configured my Domain to point at the Digital Ocean nameservers and there configured my DNS records to point at my servers public IP adress

SSL ceritfate - I used certbot to get an SSL  ecnryption protocol for the domains i am using. This made sure all HTTP request are redirected to secure HTTPS. This required me to change the NGINX firewall and disable NGINX http.

CI/CD - Not sure if this is the right way to do so, but I made sure that my cd solution using github actions worked before I setup my ""webapp"", for now the app is really simple but i can work on this now and autmaticaly update it and don't have to think about it anymore. I used action from the github marketplace to make the SSH connection, which took some setting up and figuring things out. I first did as a root user, but later changed it to seperate sudo user.
