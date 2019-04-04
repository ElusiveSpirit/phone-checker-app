# Phone Checker app

## Overview

Simple testing module to find phone numbers on site contacts page.

The task required also to get the current phone number. But the feature not approach current service goals.

You should also understand that this's a simple test app, so there isn't integration tests.

## How to run

```bash
docker-compose up
```

Ready to access localhost:5000

## Public API

#### Create job for analysing page
```
>>> POST /phone-process
{
	"url": "https://hands.ru/company/about"
}
<<< 201
{
    "task_id": "66f231d6-a22f-41b3-b380-46af47ae8da6"
}
```
#### Get job's result
```
>>> GET /phone-process?task_id=66f231d6-a22f-41b3-b380-46af47ae8da6

# Not ready
<<< 200
{
    "status": "started"
}

# Finished
<<< 200
{
    "status": "finished",
    "phone_numbers": [
        "84951370720"
    ]
}
```
