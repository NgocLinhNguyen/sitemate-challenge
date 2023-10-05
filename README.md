# Setup BE 

Run the following commands to setup BE locally. The port will be 8000. I fixed the BE port on client side for now.
- cd sitemate_challenge_backend
- docker-compose up -d --build

# Setup FE

Commands to start the client:
- cd sitemate_challenge_frontend
- npm i 
- npm run dev

# Overall
## Server side
- 5 APIs for issues:
  + Listing issues
  + Read details of a issue
  + Update a issue
  + Create new issue
  + Delete a issue
- Tech stacks: Using Python (Flask Framework) & PostgreSQL
- Use Docker to wrap Server side application

## Client side
- 5 features:
  + Listing issues
  + Read details of a issue
  + Update a issue
  + Create new issue
  + Delete a issue
- Tech stacks: ReactJS (NextJS Framework)
- Managing status is ready on Frontend but not Backend
