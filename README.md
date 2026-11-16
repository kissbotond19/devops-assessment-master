# DevOps Engineer Homework

## Overview

The goal of this assignment is to evaluate how you approach a typical DevOps engineering task involving:

- Application development / scripting
- Containerization
- Kubernetes
- Helm
- Terraform
- CI/CD
- Code review

The repository contains intentionally incomplete and imperfect components.
Your task is to complete, improve and document the solution.

You are not expected to produce a perfect production-ready system. We are more interested in your engineering approach, decision-making and ability to balance quality with the time constraints.

Time limit: approximately **3 hours**

## Repository Contents

The repository contains:

- An incomplete application skeleton
- Terraform configuration requiring review and improvement
- An incomplete Helm chart
- An incomplete CI/CD pipeline

Your task is to complete and improve these components. Our goal is to understand your engineering approach, and we will build the upcoming technical interview on this project.

## Goal 1

Complete and improve the provided project.

The repository contains the following files:

- Incomplete application code
- Broken/incomplete terraform configuration
- Incomplete Helm Chart
- Incomplete Gitlab CI pipeline

### Requirements

#### Application

Implement a simple application in either:

- Go
- Python

The application must expose the following endpoints:

##### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

##### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

##### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

##### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

#### Containerization

- Create the necessary Dockerfile with minimal setup
- The image should:
  - build successfully
  - run locally
  - expose the application endpoint

#### Terraform

- Review and fix/complete the Terraform code
- The Terraform code contains several issues and areas for improvement
- In case you don't get time to implement changes describe what would you still improve and why
- Document any changes you make

#### Helm

- Review and fix/complete the Helm Chart
- The chart should deploy the application to Kubernetes
- Document any change you make

#### Gitlab CI

- Complete the pipeline so it becomes capable of building and deploying the application
- The pipeline should support the workflow required to build and deploy the application
- The pipeline should be logically complete and demonstrate how you would automate the process
- Add any other necessary jobs to the pipeline

### Timing

Timebox yourself to approximately **3 hours**. If you can't finish the work within the timebox, describe in the README.md what is left and how you would approach it.

--> I must admit that in 3 hours, I was only finished with the first 4/5 steps listed below. But I've still completed the rest too, just out of vanity and professional curiosity.:) (Usually I'm not working with Gitlab CI, so I was courious how exactly an E2E pipeline works there.)

#### Documentation

Update the project README with following information.

##### What You Changed

You can follow it step by step by checking the [commits](https://github.com/kissbotond19/devops-assessment-master/commits/main/) in [kissbotond19/devops-assessment-master](https://github.com/kissbotond19/devops-assessment-master) repo.

Step 1. -> [add simple python app](https://github.com/kissbotond19/devops-assessment-master/commit/43ee19788bcb6da16873aa65ad22b12d8e2dac6a) (FastAPI has been mostly chosen as framework over Flask because of its built-in Swagger UI/OpenAPI capability.)

Step 2. -> [add Dockerfile and requirements.txt](https://github.com/kissbotond19/devops-assessment-master/commit/6f5b87dac5459fdf2f1f797085b45da3e9e3e699) (requirements.txt is mostly needed because of uvicorn; and also practical if other packages would be required in the future during the further development of the app.)

Step 3. -> [restructure helm dir](https://github.com/kissbotond19/devops-assessment-master/commit/e5e16997ec12356b874588cbdf09e9aaa9ee64bd) (based on the helm chart's location in terraform main.tf, could be practical in case of further developments too.)

Step 4. -> [helm chart review and fix/complete](https://github.com/kissbotond19/devops-assessment-master/commit/ff887837e751796d40065f3bf11f1d57c21a19c8)
Main considerations behind the fixes and improvements:
- Make the chart more "templatable" -> control most of the variables via the Helm chart's values.yaml instead of statically hardcode them in the template yamls.
- Fix the misconfigurations, such as containerPort/targetPort and Service selector/Deployment label/Ingress backend name discrepancies.

Step 5. -> [review and fix/complete terraform code](https://github.com/kissbotond19/devops-assessment-master/commit/87d4125983a186745dc75615e4d5e5ef4efba5fd)
- Use variables instead of hardcode, where it's applicable.
- Add some output values which may be useful in the future.

Step 6. -> [complete gitlab ci pipeline](https://github.com/kissbotond19/devops-assessment-master/commit/69cc8c7596b41fefa189dfd44e9f025bef73bfab)

##### Assumptions

It's not definitely needed to utilize both Helm and Terraform for this assignment. It's better to choose one of them for the pipeline implementation to avoid unnecessary complexity. I preferred Helm, since that's more suitable for the current purpose. 
I've also assumed that Terraform is part of this project rather to prove my basic understanding of its concept - usually it's not the standard tool for this kind of tasks but rather for (cloud) infrastructure deployments and handlings as code.

##### Known Limitations

I've omitted Terraform because of the above reasons. Besides that, probably some test job would be also nice in the pipeline for Production usage. I'm not absolutely satisfied either with the image tagging approach regarding the Helm chart and the pipeline but since the clock was ticking, that's far I got.

##### Production Improvements

Apart of the missing test job and the possible improvement of the image tagging, I would also limit the pipeline to trigger new builds, only if the commit has changed something in app/, Dockerfile or requirements.txt. Otherwise only the deploy job should be running. 
In case of Helm, the usage of environment specific values.yaml could be an option (DEV/TEST/PROD). Perhaps the deploy job could be also re-structured to separate the deployments on the different environments; in case of Prod, I would rather not allow automatic deployments either. 
And obviously a container registry should be also part of a Prod implementation.

### Deliverables

- Source Code of the Go/Python application
- Dockerfile
- Terraform changes
- Helm changes
- CI pipeline changes
- README describing decisions, assumptions and user guide for the project.

### Notes

You are not expected to deploy to a cloud provider.
The solution should work with a local Kubernetes cluster such as:

- Kind
- Minikube
- K3d

## Goal 2

You get this half-baked project from one of your colleagues who is a Junior and asking for your guidance.

Provide a short code review in `REVIEW.md` where you address the **top 5 most important things** to fix so the colleague can move forward.

### Review Timing

Spend no more than **30 minutes** on review and feedback.

### Evaluation Criteria

We will evaluate:

- Code quality
- Terraform quality
- Kubernetes and Helm knowledge
- CI/CD design and implementation
- Documentation quality
- Code review quality
- Maintainability and operational thinking

### Use of AI

The use of AI-assisted tools is permitted. However, we encourage you to complete the assignment primarily based on your own knowledge, experience and reasoning. During the interview, we will discuss your implementation choices, trade-offs and decision-making process, so it is important that you fully understand and can explain every part of your solution.