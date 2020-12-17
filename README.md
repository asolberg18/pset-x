[![Build Status](https://travis-ci.com/asolberg18/pset-x.svg?token=8b7y214fLCZnijNpb6Pv&branch=master)](https://travis-ci.com/asolberg18/pset-x)

[![Maintainability](https://api.codeclimate.com/v1/badges/1697bf141cb6fe23030a/maintainability)](https://codeclimate.com/github/asolberg18/pset-x/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/1697bf141cb6fe23030a/test_coverage)](https://codeclimate.com/github/asolberg18/pset-x/test_coverage)

# Pset X

Customizing our own Yeoman repo, and using it to complete a streaming data pipeline
using Elastic Search.

Note: This problem set will involve submitting two separate repos:

1. customized Yeoman generator
2. pset X

Please submit both links to the Canvas assignments when you have completed!

<!-- TOC depthFrom:1 depthTo:3 withLinks:1 updateOnSave:false orderedList:0 -->

- [Pset X](#pset-x)
	- [Preface](#preface)
		- [ElasticSearch](#elasticsearch)
		- [Async Programming in Python](#async-programming-in-python)
		- [Non-blocking IO](#non-blocking-io)
- [Problems](#problems)
	- [Use your Yeoman generator to create your pset-X repo](#use-your-yeoman-generator-to-create-your-pset-x-repo)
	- [Create Free ElasticSearch account](#create-free-elasticsearch-account)
	- [Create ElasticSearch logging module](#create-elasticsearch-logging-module)
		- [Step 1: Setup your project](#step-1-setup-your-project)
		- [Step 2: Copy the LogEvent class](#step-2-copy-the-logevent-class)
		- [Step 3: Create ElasticLogger class](#step-3-create-elasticlogger-class)
		- [Step 4: Create TaskEngine class](#step-4-create-taskengine-class)
		- [Step 5: Implement the CLI](#step-5-implement-the-cli)
	- [Initialize, load, and query the ElasticSearch index](#initialize-load-and-query-the-elasticsearch-index)
		- [Step 1: Initialize the ElasticSearch log schema](#step-1-initialize-the-elasticsearch-log-schema)
		- [Step 2: Populate the ElasticSearch index with test events](#step-2-populate-the-elasticsearch-index-with-test-events)
		- [Step 3: Execute queries against ElasticSearch](#step-3-execute-queries-against-elasticsearch)

<!-- /TOC -->

## Preface

DO NOT CLONE THIS REPO LOCALLY YET.  We will manually create a repo and link it.
If you have cloned this repo locally, simply delete it (it's fine if it's
already forked on github).

### ElasticSearch

Elasticsearch is a distributed, open source search and analytics engine for all
types of data, including textual, numerical, geospatial, structured, and
unstructured. Elasticsearch is built on Apache Lucene and was first released in
2010 by Elasticsearch N.V. (now known as Elastic). Known for its simple REST
APIs, distributed nature, speed, and scalability, Elasticsearch is the central
component of the Elastic Stack, a set of open source tools for data ingestion,
enrichment, storage, analysis, and visualization. Commonly referred to as the
ELK Stack (after Elasticsearch, Logstash, and Kibana), the Elastic Stack now
includes a rich collection of lightweight shipping agents known as Beats for
sending data to Elasticsearch.

Read more at: https://www.elastic.co/what-is/elasticsearch

Once you have data in ElasticSearch you will want to be able to query the data.
You can query ElasticSearch using the console, but it is often useful to be
able to query ElasticSearch from a Python program. This data could be used
directly to solve some problem, or fed into a pipeline for additional processing
using tools like Dask or Luigi. In this pset you will create a Python module for
querying and extracting data from ElasticSearch. This module will have the
ability to generate test log events using advanced python async programing and
non-blocking IO.

### Async Programming in Python

When programming in Python, you have several options for concurrent programming
or parallel processing. This includes multithreading, multiprocessing, and
cooperative multitasking. Python 3.5 added language support for the latter,
cooperative multitasking.

Cooperative multitasking is the core of asynchronous programming in Python. In
this style of computer multitasking, it's not a responsibility of the operating
system to initiate a context switch (to another process or thread), but instead
every process voluntarily releases the control when it is idle to enable
simultaneous execution of multiple programs. This is why it is called
cooperative. All processes need to cooperate in order to multitask smoothly.  

The async and await keywords are the main building blocks in Python asynchronous
programming. The async keyword, when used before the def statement, defines a
new coroutine. The execution of the coroutine function may be suspended and
resumed, allowing the program to perform other functions while the coroutine is
suspended. The await keyword tells Python to wait for a coroutine to finish
executing before continuing to the next statement. This allows multitasking
operations to be serialized when a specific execution sequence is needed.

### Non-blocking IO

Cooperative multitasking isn't ideal for all parallel processing tasks. In
particular, tasks that are compute heavy are not suited for cooperative
multitaksing. However, many tasks spend a large percentage of their time waiting
for IO operations to complete. This is called blocking IO. Even though your
program is just waiting for the disk or network, it is blocked from doing any
other work.

Non-blocking IO allows the program to continue running while waiting for the
resource such as disk or network. These IO-bound applications can often achieve
significant performance improvement using async operations in an event loop
using cooperative multitasking.

You will be using Python async coroutines with the async and await keywords to
implement cooperative multitasking in the ElasticSearch logger. Unfortunately,
the Python requests module, which implements HTTP methods, is not non-blocking.
You will install AIOHTTP, which is an asynchronous HTTP Client/Server for
asyncio and Python.


# Problems

## Use your Yeoman generator to create your pset-X repo

In the directory above `generator-yopy`, *do the
following*:

```bash
yo yopy
```

You have configured many things already such as name, github id, travis, etc.

In addition, for this project specifically, make sure to *do the following*:  

| Param | Value |  
|-|-|  
| project_name | `Pset X` |  
| repo_name | (should default to `<semester>-pset-x-<github_id>`) |  
| project_slug | (should default to `pset_x`) |

### Push your pset X repo

Now you can *push to your pset X repo* via:

```bash
# Create a git repo in your new project folder
cd <rendered pset folder>
git init

# You can now open in sourcetree and manually add project files

# alternately...
git add --all
git commit -m "Add initial project skeleton."

# Now configure and push to remote
git remote add origin git@github.com:<github_id>/generator-yopy.git
git fetch
git merge origin/master --allow-unrelated-histories
git push -u origin master
```

## Create Free ElasticSearch account

### Step 1

Navigate to https://www.elastic.co/ and click on `Try Free` on the top right.

<img src="/2020fa-pset-x-asolberg18/images/step1.png" alt="Step 1" width="600px" />

### Step 2

Fill out registration form, and click `Start Free Trial`.

<img src="/2020fa-pset-x-asolberg18/images/step2.png" alt="Step 2" width="400px" />


### Step 3

Verify your email address, then select `Elastic Stack`.

<img src="/2020fa-pset-x-asolberg18/images/step3.png" alt="Step 3" width="600px" />


### Step 4

Accept all default values, scroll down and click on `Create Deployment`

<img src="/2020fa-pset-x-asolberg18/images/step4.png" alt="Step 4" width="600px" />


### Step 5

Click download to save your elastic credentials. You will need these to access
your deployment APIs.

<img src="/2020fa-pset-x-asolberg18/images/step5.png" alt="Step 5" width="400px" />


### Step 6

Scroll down the dashboard to the list of applications (it should list Kibana,
ElasticSearch, and APM). Click `copy endpoint` for your ElasticSearch instance.
Be sure to save this endpoint for later use.

<img src="/2020fa-pset-x-asolberg18/images/step6.png" alt="Step 6" width="600px" />


### Step 7

Open a new tab. Paste your copied endpoint into the address bar, and enter the
saved username and password credentials from Step 5.

<img src="/2020fa-pset-x-asolberg18/images/step7.png" alt="Step 7" width="400px" />


This shows your metadata and status of your instance. It should look similar to
this:

<img src="/2020fa-pset-x-asolberg18/images/step7b.png" alt="Step 7b" width="400px" />


The ElasticSearch API is a REST API and you can use it to explore all of your
data and services. You can also use tools like Postman, or the built in Kibana
DevTools application to test your queries. We will be using DevTools in a later
step.


## Create ElasticSearch logging module

ElasticSearch is capable of storing, indexing, and querying extremely large
datasets. You will write a utility module that can initialize an ElasticSearch
index with a schema for storing web server log events. The schema is provided
below.

Once the index is created, the utility module can be used to generate any number
of test log events using randomized event attributes. This part of the code will
be provided for you to standardize our expected results. The generating module
includes the ability to very flexibly specify date and time ranges for the
generated events. Log events will be encapsulated in a LogEvent class. This
class will include a static factory method to generate the random log events.

The challenge is to generate a large number of events efficiently and quickly.
You will create a TaskEngine class that encapsulates the logic to call the
ElasticSearch APIs in parallel. However, you must also ensure that you don't
make too many simultaneous requests against the server. This would likely
trigger rate limiting by ElasticSearch and could even be considered a
denial-of-service attack. For this assignment, you should limit the maximum
number of concurrent requests to 10.


### Step 1: Setup your project

You will need to have four .env variables set up for this project.
```
ELASTIC_USERID=elastic
ELASTIC_PASSWORD=<YOUR_GENERATED_CREDENTIAL_PASSWORD>
ELASTIC_HOST=<YOUR_ELASTIC_SEARCH_ENDPOINT>
ELASTIC_INDEX=pset_x
```
You will also need to `pipenv install aiohttp`.


### Step 2: Copy the LogEvent class

In the pset_x folder, create `log_event.py`. Copy the contents below into this
file. You can use this class as is because it is only being utilized with the
async TaskEngine.

```python

class LogEvent:

    logged = 0
    countries = ['VI', 'EG', 'US', 'UK',
                 'CN', 'CA', 'DE', 'MX', 'FR', 'BR']
    browsers = ['Chrome', 'Safari', 'IE', 'Firefox', 'Edge']
    os = ['Mac', 'Android', 'Linux', 'IOS', 'windows']
    resp_codes = [501, 100, 200, 201, 303, 411, 403, 406, 507, 208, 426]

    def __init__(self, logID, eventTime, url, ua_country, userId, browser, ua_os, responseCode, ttfb, location):
        self.logID = logID
        self.eventTime = eventTime
        self.url = url
        self.ua_country = ua_country
        self.userId = userId
        self.browser = browser
        self.ua_os = ua_os
        self.responseCode = responseCode
        self.ttfb = ttfb
        self.location = location

    async def log(self, logger):
        await logger(self.__dict__)
        LogEvent.logged += 1

    @staticmethod
    def CreateTimestamp(mask):
        y = datetime.today().year + random.randint(-5,
                                                   5) if mask['y'] == '?' else mask['y']
        m = random.randint(1, 12) if mask['m'] == '?' else mask['m']
        d = random.randint(1, 31) if mask['d'] == '?' else mask['d']
        if m == 2 and d > 28:
            d -= 3
        elif m in [9, 4, 6, 11] and d == 31:
            d = 30
        H = random.randint(0, 23) if mask['H'] == '?' else mask['H']
        M = random.randint(0, 59) if mask['M'] == '?' else mask['M']
        S = random.randint(0, 59) if mask['S'] == '?' else mask['S']
        return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y, m, d, H, M, S)

    @staticmethod
    def ParseTimestampMask(ts_str):
        t = ts_str.split('T')
        t = t if len(t) == 2 else ts_str.split(' ')
        if len(t) != 2:
            raise ValueError()
        if t[0].lower() == 'today':
            t[0] = datetime.today().strftime('%Y-%m-%d')
        if t[1].lower() == 'now':
            t[1] = datetime.today().strftime('%H:%M:%S')
        ymd = t[0].split('-')
        hms = t[1].split(':')
        if len(ymd) != 3 or len(hms) != 3:
            raise ValueError()
        ymd = [x if x == '?' else int(x) for x in ymd]
        hms = [x if x == '?' else int(x) for x in hms]
        if not ((ymd[0] == '?' or len(str(ymd[0])) == 4) and
                (ymd[1] == '?' or (ymd[1] >= 1 and ymd[1] <= 12)) and
                (ymd[2] == '?' or (ymd[2] >= 1 and ymd[2] <= 31)) and
                (hms[0] == '?' or (hms[0] >= 0 and hms[0] <= 23)) and
                (hms[1] == '?' or (hms[1] >= 0 and hms[1] <= 59)) and
                (hms[2] == '?' or (hms[2] >= 0 and hms[2] <= 59))):
            raise ValueError()
        ts = {'y': ymd[0], 'm': ymd[1], 'd': ymd[2],
              'H': hms[0], 'M': hms[1], 'S': hms[2]}
        return ts

    @staticmethod
    def random_event(ts_mask, countries=countries, browsers=browsers, os=os, resp_codes=resp_codes):
        return LogEvent(
            logID=str(uuid.uuid4()),
            eventTime=LogEvent.CreateTimestamp(ts_mask),
            url="http://example.com/?url={:03d}".format(random.randint(0, 15)),
            ua_country=countries[random.randint(0, len(countries)-1)],
            userId="user{:03d}".format(random.randint(1, 15)),
            browser=browsers[random.randint(0, len(browsers)-1)],
            ua_os=os[random.randint(0, len(os)-1)],
            responseCode=resp_codes[random.randint(
                0, len(resp_codes)-1)],
            ttfb=float(round(random.uniform(0.4, 10.6), 2)),
            location={'lat': round(random.uniform(-90.0, 90.0), 5),
                      'lon': round(random.uniform(-180.0, 180.0), 5)}
        )

```

### Step 3: Create ElasticLogger class

In the pset_x directory create a file called `es_logger.py`. The ElasticLogger
class encapsulates all the code that interacts with ElasticSearch through the
ElasticSearch REST API's. The schema for the pset_x index mappings is given
below, but you will need to complete some of the async functions. Each of
these functions can/should be completed in 10 or ideally fewer lines.


```python

class ElasticLogger:

    schema = {
        "mappings": {
            "properties": {
                "browser": {
                    "type": "keyword"
                },
                "eventTime": {
                    "type": "date"
                },
                "logID": {
                    "type": "text"
                },
                "responseCode": {
                    "type": "integer"
                },
                "ttfb": {
                    "type": "float"
                },
                "ua_country": {
                    "type": "keyword"
                },
                "ua_os": {
                    "type": "text"
                },
                "url": {
                    "type": "keyword"
                },
                "userId": {
                    "type": "text"
                },
                "location": {
                    "type": "geo_point"
                }
            }
        }
    }

    def __init__(self, host=None, index=None, user=None, pw=None):
        # Initalize host and index using .env vars
        ...
        # Use aiohttp.ClientSession to create an authenticated http session
        # using basic authentication and the credentials read from the .env
        ...

    async def __call__(self, event):
        # Post the json event object to the ElasticSearch index
        # hints:
        # - the aiohttp session object has methods for get, post, put, ...
        # - Be sure to await on the request so you can test the response
        # - e.g. resp = await self.session.post(url, json=event)
        # - The url for posting events is:
        #   <host>/<index>/_doc
        ...
        return resp

    async def close(self):
        await self.session.close()

    async def init_schema(self):
        # Delete the index if it exists
        await self.session.delete(self.index_uri)

        # Create the index using json = self.schema
        # hint: the url for the put is <host>/<index>
        ...
        print("\nResponse: {}".format(resp.status))
        print(await resp.json())
        return resp

    async def query(self, query):
        # Execute the specified ElasticSearch query and print the results
        # hint: query url to get is <host>/<index>/_search
        ...
        print("\nResponse: {}".format(resp.status))
        print(await resp.json())
        return resp

```

### Step 4: Create TaskEngine class

In the pset_x directory create a file called `task_engine.py`. The TaskEngine
class encapsulates all the code that executes tasks in parallel on the Python
event loop. To avoid overwhelming the server, the class will ensure that no more
than 10 (default) requests are simultaneously pending.

The TaskEngine constructor should take a logger instance for extensible logging.
It should also set up instance variables to track the number of started,
pending, and completed tasks. It can use a boolean flag stopped to indicate that
the engine should stop and cleanly exit.

This class includes some functions that begin with two underscores (such as
__run). This naming convention is intended to identify private methods. Python
doesn't actually support private methods, but this convention comes close to it.


```python

class TaskEngine:

    def __init__(self, max_tasks=10, monitor=False, logger=None):
        self.loop = asyncio.get_event_loop()
        self.started = 0
        self.pending = 0
        self.completed = 0
        self.stopped = False
        self.max_tasks = max_tasks
        self.logger = logger
        self.monitor = monitor
        if self.monitor:
            self.loop.create_task(self.__monitor())


    def run(self, driver):
        self.loop.run_until_complete(self.__run(driver))

    async def stop(self):
        print("\nStopping...")
        self.stopped = True
        while self.monitor:
            await asyncio.sleep(0.01)

    def running(self):
        return not self.stopped

    async def start_task(self, task, *args, **kwargs):
        # Before creating the new task, you need to make sure that the
        # current pending task count is less than self.max_tasks, otherwise
        # you can sleep in short intervals until this condition is met.
        # e.g. await asyncio.sleep(0.01)
        ...
        if self.running():
            self.__start_task()
            # Use self.loop.create_task to schedule the task instance
            # Be sure to pass in *args and *kwargs
            ...
        else:
            print("Error: engine stopped")

    async def run_until_complete(self):
        # Sleep until self.pending == 0
        ...

    async def __run(self, driver):
        await driver(self)
        await self.run_until_complete()
        await self.stop()
        if self.logger:
            await self.logger.close()

    async def __run_async(self, task, *args, **kwargs):
        # Run the users task (with args, and kwargs)
        # Make sure the task is finished before calling
        # self.___complete_task()
        ...
        self.__complete_task()

    def __start_task(self):
        self.pending += 1
        self.started += 1

    def __complete_task(self):
        self.pending -= 1
        self.completed += 1

    async def __monitor(self):
          while self.running():
              print("\rStarted: {:04d} : Pending: {:04d} : Completed: {:04d}".format(
                  self.started, self.pending, self.completed), end="")
              await asyncio.sleep(0.5)
          print("\rStarted: {:04d} : Pending: {:04d} : Completed: {:04d}".format(
              self.started, self.pending, self.completed))
          print("Engine stopped.")
          self.monitor = False

```

### Step 5: Implement the CLI

The classes we have implemented so far encapsulate the various functionality for
running tasks, creating events, and interacting with ElasticSearch. This will
make the CLI simpler and easier to understand.

Note that you need to pass in the program args from your `__main__.py` with
`main(sys.argv[1:])`.

Replace the contents of your `cli.py` with the following:

```python

parser = argparse.ArgumentParser(description="Command description.")
parser.add_argument("command", choices=["generate", "init", "query"])
parser.add_argument("--timestamp", type=str, default="todayT?:?:?")
parser.add_argument("--count", type=int, default="1")

random.seed(time.time())


def main(args):

    args = parser.parse_args(args)
    num_events = args.count
    # ts_mask is used to specify a template for generating random timestamps
    # You can look at the code if you want to understand the options more
    ts_mask = LogEvent.ParseTimestampMask(args.timestamp)

    async def non_blocking_logger(engine):
        # Call engine.start_task num_events times to create the requested
        # number of log events in non-blocking parallel tasks
        # hints:
        # - Use LogEvent.random_event(ts_mask) to create events
        # - engine.start_task is used to start each task
        # - The event.log method is an async method that can be passed to start_task
        ...

    # If you're stuck on non_blocking_logger, reference init_logger
    # and query_logger below for ideas.
    async def init_logger(engine):
        await engine.start_task(engine.logger.init_schema)

    async def query_logger(engine):
        # The query json is read from standard in
        # This can be piped in the command line
        query = json.load(sys.stdin)
        await engine.start_task(engine.logger.query, query)

    engine = TaskEngine(monitor=True, logger=ElasticLogger())

    if args.command == 'generate':
        # Run non_blocking_logger using TaskEngine
        ...
        print("{} log events generated".format(LogEvent.logged))

    elif args.command == 'init':
        # Run init_logger using TaskEngine
        ...
        print("Schema generated")

    elif args.command == 'query':
        # Run query_logger using TaskEngine (completed for you)
        engine.run(query_logger)
        print("Query finished")

```


## Initialize, load, and query the ElasticSearch index

If everything is working, you should now be able to initialize your
ElasticSearch index, load in data, and run queries.


### Step 1: Initialize the ElasticSearch log schema

Run the command

```bash
$ pipenv run python -m pset_x init
```

Your output should look something like:

```bash
Loading .env environment variables...
Started: 0001 : Pending: 0001 : Completed: 0000
Response: 200
{'acknowledged': True, 'shards_acknowledged': True, 'index': 'pset_x'}

Stopping...
Started: 0001 : Pending: 0000 : Completed: 0001
Engine stopped.
Schema generated
```

### Step 2: Populate the ElasticSearch index with test events

Run the command

```bash
$ pipenv run python -m pset_x generate --count=1000
```

Your output should look something like:

```bash
Loading .env environment variables...
Started: 1000 : Pending: 0006 : Completed: 0994
Stopping...
Started: 1000 : Pending: 0000 : Completed: 1000
Engine stopped.
1000 log events generated
```

If you want to verify that your data has loaded correctly to your ElasticSearch
account, you can launch Kibana from your homepage and access the Dev Tools app
from the left dropdown menu. To verify your data was generated, run the
following in the Dev Tools interface:

```
GET pset_x/_search
{
  "query": {
    "match_all": {}
  }
}
```

Your result should look something like this:

<img src="/2020fa-pset-x-asolberg18/images/devtools.png" alt="Kibana Dev Tools" width="900px" />



### Step 3: Execute queries against ElasticSearch

We are going to provide some suggested queries. Feel free to refer to the
ElasticSearch documentation and create more interesting queries if you like.

Create a `query1.json` file with the following:

```json
{}
```

Create a `query2.json` file with the following:
```json
{
    "size": 0,
    "aggregations": {
        "country": {
            "terms": {
                "field": "ua_country"
            },
            "aggregations": {
                "browser": {
                    "terms": {
                        "field": "browser"
                    }
                }
            }
        }
    }
}
```

Create a `query3.json` file with the following:

```json
{
    "size": 0,
    "query": {
        "range": {
            "responseCode": {
                "gte": 500,
                "lte": 599
            }
        }
    },
    "aggregations": {
        "url": {
            "terms": {
                "field": "url",
                "size": 5,
                "order": {
                    "_count": "desc"
                }
            }
        }
    }
}
```

Run the query with the following command. You can substitute any of the above
queries, or pipe your own queries on the command line.

```bash
$ pipenv run python -m pset_x query < query1.json
```

The output will look something like:

```bash
Loading .env environment variables...
Started: 0000 : Pending: 0000 : Completed: 0000
Response: 200
{'took': 3, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1000, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'pset_x', '_type': '_doc', '_id': 'SY3FNnYB4uwO_odrNl9e', '_score': 1.0, '_source': {'logID': '531ba445-501c-4fab-8fe4-7da2f0207001', 'eventTime': '2020-12-05T11:11:13', 'url': 'http://example.com/?url=002', 'ua_country': 'FR', 'userId': 'user015', 'browser': 'Firefox', 'ua_os': 'Android', 'responseCode': 426, 'ttfb': 8.58, 'location': {'lat': 15.39896, 'lon': -165.95673}}}, {'_index': 'pset_x', '_type': '_doc', '_id': 'T43FNnYB4uwO_odrNl-t', '_score': 1.0, '_source': {'logID': '0304e931-32f1-47b6-a9de-f3007ae53420', 'eventTime': '2020-12-05T13:24:13', 'url': 'http://example.com/?url=001', 'ua_country': 'FR', 'userId': 'user003', 'browser': 'Chrome', 'ua_os': 'Android', 'responseCode': 426, 'ttfb': 6.41, 'location': {'lat': 55.31781, 'lon': -63.20766}}} <snip> ...}

Stopping...
Started: 0001 : Pending: 0000 : Completed: 0001
Engine stopped.
Query finished
```
