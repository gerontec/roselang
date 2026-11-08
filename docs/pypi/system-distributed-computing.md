# System / Distributed Computing

[Index](README.md) · 15 packages in this topic, 76 more listed under another topic, by downloads.

### modal

Python client library for Modal

`pip install modal` · installs (wheel) · licence: Apache-2.0 · rank 474 · last release 2026-10-27 · [PyPI](https://pypi.org/project/modal/) · [docs](https://modal.com/docs) · [source](https://github.com/modal-labs/modal-client)

<details><summary>README extract</summary>

The Modal Python SDK provides convenient, on-demand
access to serverless cloud compute from Python scripts on your local computer.

See the online documentation for many
example applications,
a user guide, and the detailed
API reference.

Sections: Modal Python SDK, Documentation

</details>

### aiokafka

Kafka integration with asyncio

`pip install aiokafka` · installs (wheel) · licence: Apache-2.0 · rank 1089 · last release 2026-10-28 · [PyPI](https://pypi.org/project/aiokafka/) · [docs](http://aiokafka.readthedocs.org) · [source](https://github.com/aio-libs/aiokafka)

<details><summary>README extract</summary>

asyncio client for Kafka

Python 3.11 or newer is required.

AIOKafkaProducer is a high-level, asynchronous message producer.

Example of AIOKafkaProducer usage:

Example:
```python
from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("my_topic", b"Super message")
...
```

Sections: aiokafka, AIOKafkaProducer, AIOKafkaConsumer, Documentation, Running tests

</details>

### c7n-org

Cloud Custodian - Parallel Execution

`pip install c7n-org` · installs (wheel) · licence: Apache-2.0 · rank 1301 · last release 2026-10-01 · [PyPI](https://pypi.org/project/c7n-org/) · [docs](https://cloudcustodian.io/docs/tools/c7n-org.html) · [source](https://github.com/cloud-custodian/cloud-custodian)

<details><summary>README extract</summary>

% [comment]: # ( !!! IMPORTANT !!! )
% [comment]: # (This file is moved during document generation.)
% [comment]: # (Only edit the original document at ./tools/c7n_org/README.md)

c7n-org is a tool to run Custodian against multiple AWS accounts,
Azure subscriptions, GCP projects, or OCI tenancies in parallel.

Sections: c7n-org: Multi Account Custodian Execution, Config File Generation, Running a Policy with c7n-org, Selecting accounts, regions, policies for execution, Defining and using variables, Validating Policies, Other commands, Additional Azure Instructions, Additional OCI Instructions

</details>

### flower

Celery Flower

`pip install flower` · installs (wheel) · licence: BSD License · rank 1366 · last release 2026-09-22 · [PyPI](https://pypi.org/project/flower/)

<details><summary>README extract</summary>

Flower is an open-source web application for monitoring and managing Celery clusters.
It provides real-time information about the status of Celery workers and tasks.

Features:
- Real-time monitoring using Celery Events
 - View task progress and history
 - View task details (arguments, start time, runtime, and more) ...

Sections: Flower, Features, Usage, API, Documentation

</details>

### dramatiq

Background Processing for Python 3.

`pip install dramatiq` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 2892 · last release 2026-09-02 · [PyPI](https://pypi.org/project/dramatiq/) · [docs](https://dramatiq.io) · [source](https://github.com/Bogdanp/dramatiq)

_README extract left out: share-alike licence._

### submitit

"Python 3.8+ toolbox for submitting jobs to Slurm

`pip install submitit` · installs (wheel) · licence: MIT License · rank 3643 · last release 2025-12-17 · [PyPI](https://pypi.org/project/submitit/) · [source](https://github.com/facebookincubator/submitit)

<details><summary>README extract</summary>

Submitit is a lightweight tool for submitting Python functions for computation within a Slurm cluster.
It basically wraps submission and provide access to results, logs and more.
Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. ...

Example:
```python
import submitit

def add(a, b):
    return a + b

# executor is the submission interface (logs are dumped in the folder)
executor = submitit.AutoExecutor(folder="log_test")
# set timeout in min, and partition for running the job
executor.update_parameters(timeout_min=1, slurm_partition="dev")
...
```

Sections: Submit it!, What is submitit?, Documentation, Goals, Non-goals, Comparison with dask.distributed

</details>

### c7n

Cloud Custodian - Policy Rules Engine

`pip install c7n` · installs (wheel) · licence: Apache-2.0 · rank 3804 · last release 2026-10-01 · [PyPI](https://pypi.org/project/c7n/) · [docs](https://cloudcustodian.io/docs) · [source](https://github.com/cloud-custodian/cloud-custodian)

<details><summary>README extract</summary>

Cloud Custodian, also known as c7n, is a rules engine for managing
public cloud accounts and resources. It allows users to define
policies to enable a well managed cloud infrastructure, that\'s both
secure and cost optimized. ...

</details>

### faktory

Python worker for the Faktory project

`pip install faktory` · installs (wheel) · licence: BSD License · rank 4851 · last release 2022-04-30 · [PyPI](https://pypi.org/project/faktory/)

### celery_once

Allows you to prevent multiple execution and queuing of celery tasks.

`pip install celery_once` · installs from source (sdist only) · licence: BSD License · rank 7250 · last release 2019-08-21 · [PyPI](https://pypi.org/project/celery_once/)

<details><summary>README extract</summary>

Celery Once allows you to prevent multiple execution and queuing of celery tasks.

Example:
```python
from celery import Celery
from celery_once import QueueOnce
from time import sleep

celery = Celery('tasks', broker='amqp://guest@localhost//')
celery.conf.ONCE = {
  'backend': 'celery_once.backends.Redis',
  'settings': {
    'url': 'redis://localhost:6379/0',
    'default_timeout': 60 * 60
  }
}

@celery.task(base=QueueOnce)
def slow_task():
...
```

Sections: Celery Once, Requirements, Usage, `graceful`, `keys`, `timeout`, `unlock_before_run`, Backends, Redis Backend, File Backend, Flask Intergration, Custom Backend

</details>

### thespian

Python Actor concurrency library

`pip install thespian` · installs from source (sdist only) · licence: MIT License · rank 7392 · last release 2025-03-12 · [PyPI](https://pypi.org/project/thespian/)

<details><summary>README extract</summary>

Thespian is a Python library providing a framework for developing
concurrent, distributed, fault tolerant applications.

Thespian is built on the Actor Model which allows applications to be
written as a group of independently executing but cooperating
"Actors" which communicate via messages. ...

</details>

### faust-streaming

Python Stream Processing. A Faust fork

`pip install faust-streaming` · installs (wheel) · licence: BSD License · rank 7463 · last release 2026-10-28 · [PyPI](https://pypi.org/project/faust-streaming/) · [docs](https://faust-streaming.github.io/faust/) · [source](https://github.com/faust-streaming/faust)

<details><summary>README extract</summary>

Features:
We have decided to fork the original `Faust` project because there is a critical process of releasing new versions which causes uncertainty in the community. Everybody is welcome to contribute to this `fork`, and you can be added as a maintainer. ...

Example:
```python
# Python Streams
# Forever scalable event processing & in-memory durable K/V store;
# as a library w/ asyncio & static typing.
import faust
```

Sections: Python Stream Processing Fork, Documentation, Why the fork, Usage, Faust key points, Simple, Highly Available, Distributed, Fast, Flexible, Bundles, Faust with extras, Stores, RocksDB

</details>

### yarn-api-client

Python client for Hadoop® YARN API

`pip install yarn-api-client` · installs (wheel) · licence: BSD License · rank 8242 · last release 2021-11-16 · [PyPI](https://pypi.org/project/yarn-api-client/)

<details><summary>README extract</summary>

Python client for Apache Hadoop® YARN API

Package documentation:
yarn-api-client-python.readthedocs.org

REST API documentation: hadoop.apache.org

Warning: CLI is outdated & broken. Please don't use CLI. This will be resolved in future releases.

| yarn-api-client-python | Apache Hadoop |

| 1.0.2 | 3.2.1 |
| 1.0.3 | 3.3.0, 3.3.1 | ...

Example:
```python
from yarn_api_client import ApplicationMaster, HistoryServer, NodeManager, ResourceManager
am = ApplicationMaster('
app_information = am.application_information('application_id')
```

Sections: hadoop-yarn-api-python-client, Compatibility Matrix, Usage, CLI interface, Programmatic interface, Team

</details>

### mitogen

Library for writing distributed self-replicating programs.

`pip install mitogen` · installs (wheel) · licence: BSD-3-Clause · rank 10056 · last release 2026-10-07 · [PyPI](https://pypi.org/project/mitogen/)

### mrjob

Python MapReduce framework

`pip install mrjob` · installs (wheel) · licence: Apache Software License · rank 11317 · last release 2020-09-17 · [PyPI](https://pypi.org/project/mrjob/)

<details><summary>README extract</summary>

mrjob is a Python 2.7/3.4+ package that helps you write and run Hadoop
Streaming jobs.

Stable version (v0.7.4) documentation

Development version documentation

mrjob fully supports Amazon's Elastic MapReduce (EMR) service, which allows you
to buy time on a Hadoop cluster on an hourly basis. ...

Example:
```python
"""The classic MapReduce job: count the frequency of words.
"""
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))
...
```

...

</details>

### tooz

Coordination library for distributed systems.

`pip install tooz` · installs (wheel) · licence: Apache-2.0 · rank 11335 · last release 2026-10-30 · [PyPI](https://pypi.org/project/tooz/) · [source](https://opendev.org/openstack/tooz)

<details><summary>README extract</summary>

The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

* Free software: Apache license

Sections: Tooz, Join us

</details>

## Also in this topic

- [cloudpickle](scientific-engineering.md#cloudpickle) - Pickler class to extend the standard pickle.Pickler functionality
- [execnet](software-development-libraries.md#execnet) - execnet: rapid multi-Python deployment
- [smart-open](database-front-ends.md#smart-open) - Utils for streaming large files (S3, HDFS, GCS, SFTP, Azure Blob Storage, gzip, bz2, zst...)
- [billiard](software-development-libraries.md#billiard) - Python multiprocessing fork with improvements and bugfixes
- [kombu](communications.md#kombu) - Messaging library for Python.
- [celery](software-development-object-brokering.md#celery) - Distributed Task Queue.
- [portalocker](software-development-libraries.md#portalocker) - Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks
- [dask](scientific-engineering.md#dask) - Parallel PyData with Task Scheduling
- [dask-expr](scientific-engineering.md#dask-expr) - High Level Expressions for Dask
- [rq](internet.md#rq) - RQ is a simple, lightweight, library for creating background jobs, and processing them.
- [locust](software-development-testing.md#locust) - Developer-friendly load testing framework
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [autobahn](communications.md#autobahn) - WebSocket client & server library, WAMP real-time framework
- [django-celery-beat](communications.md#django-celery-beat) - Database-backed Periodic Tasks.
- [celery-redbeat](software-development-object-brokering.md#celery-redbeat) - A Celery Beat Scheduler using Redis for persistent storage
- [ndg-httpsclient](internet.md#ndg-httpsclient) - Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
- [distributed](scientific-engineering.md#distributed) - Distributed scheduler for Dask
- [arq](internet.md#arq) - Job queues in python with asyncio and redis
- [django-celery-results](communications.md#django-celery-results) - Celery result backends for Django.
- [kazoo](communications.md#kazoo) - "Higher Level Zookeeper Client"
- [pywinrm](software-development-libraries.md#pywinrm) - Python library for Windows Remote Management
- [pyvmomi](software-development-libraries-2.md#pyvmomi) - VMware vSphere Python SDK
- [coredis](software-development-libraries-2.md#coredis) - Fast, async, fully-typed Redis client with support for cluster and sentinel
- [skypilot](software-development-libraries-2.md#skypilot) - SkyPilot: Manage all your AI compute.
- [faststream](software-development.md#faststream) - A thin, typed Python client for Kafka, RabbitMQ, NATS, Redis and MQTT — with AsyncAPI docs and in-memory testing.
- [rpyc](internet.md#rpyc) - Remote Python Call (RPyC) is a transparent and symmetric distributed computing library
- [django-rq](internet.md#django-rq) - An app that provides django integration for RQ (Redis Queue)
- [pottery](database-front-ends.md#pottery) - Redis for Humans.
- [flameprof](internet.md#flameprof) - cProfile flamegraph generator
- [django-q2](internet-www-http.md#django-q2) - A multiprocessing distributed task queue for Django
- [mpi4py](scientific-engineering.md#mpi4py) - Python bindings for MPI
- [cityhash](scientific-engineering-information-analysis.md#cityhash) - Python bindings for CityHash and FarmHash
- [pgqueuer](database.md#pgqueuer) - PostgreSQL-backed background job and task queue for Python.
- [mooncake-transfer-engine-cuda13](scientific-engineering-artificial-intelligence.md#mooncake-transfer-engine-cuda13) - A KVCache-centric Disaggregated Architecture for large-scale LLM inference and training. (CUDA 13 version)
- [django-celery-email](communications.md#django-celery-email) - An async Django email backend using celery
- [rq-dashboard](internet.md#rq-dashboard) - rq-dashboard is a general purpose, lightweight, web interface to monitor your RQ queues, jobs, and workers in realtime.
- [saq](internet.md#saq) - Distributed Python job queue with asyncio and redis
- [python-etcd](database-front-ends.md#python-etcd) - A python client for etcd
- [celery-batches](software-development-object-brokering.md#celery-batches) - Experimental task class that buffers messages and processes them as a list.
- [DIRAC](scientific-engineering.md#dirac) - DIRAC is an interware, meaning a software framework for distributed computing.
- [iLCDirac](scientific-engineering.md#ilcdirac) - iLCDirac is the iLC/CLIC/FCC extension of DIRAC
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [zenml](software-development-libraries-3.md#zenml) - ZenML: MLOps for Reliable AI: from Classical AI to Agents.
- [cwl-utils](file-formats.md#cwl-utils) - 
- [salt](system-clustering.md#salt) - Portable, distributed, remote execution and configuration management system
- [vmware-vapi-runtime](software-development-libraries-3.md#vmware-vapi-runtime) - VMware vAPI Runtime
- [h2o-wave](communications-chat.md#h2o-wave) - Python driver for H2O Wave Realtime Apps
- [vmware-vapi-common-client](software-development-libraries-3.md#vmware-vapi-common-client) - VMware vAPI Common Services Client Bindings
- [Pyro5](software-development-object-brokering.md#pyro5) - Remote object communication library, fifth major version
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [vineyard](software-development-libraries-3.md#vineyard) - An in-memory immutable data manager
- [vineyard-bdist](software-development-libraries-3.md#vineyard-bdist) - An in-memory immutable data manager
- [bernstein](software-development.md#bernstein) - The open-source governance layer for AI agents. No model in the coordination loop, so replaying a plan reproduces its task graph byte-identically, and run receipts are byte-identical across independent builds. Signed lineage plus an opt-in HMAC audit chain a reviewer checks offline, without rerunning it. Runs Claude Code, Codex, Gemini CLI, and 50+ CLI agents; governs any deliverable from code to research to audit evidence packs. Cluster mode, air-gap deploy.
- [epicscorelibs](scientific-engineering.md#epicscorelibs) - The EPICS Core libraries for use by python modules
- [vmware-vcenter](software-development-libraries-4.md#vmware-vcenter) - Client library for vmware-vcenter APIs
- [pvxslibs](scientific-engineering.md#pvxslibs) - PVXS libraries packaged for python
- [p4p](scientific-engineering-2.md#p4p) - Python interface to PVAccess protocol client
- [Pyro4](software-development-object-brokering.md#pyro4) - distributed object middleware for Python (RPC)
- [IxNetwork](software-development-libraries-4.md#ixnetwork) - IxNetwork Low Level API
- [skypilot-nightly](software-development-libraries-4.md#skypilot-nightly) - SkyPilot: Manage all your AI compute.
- [lithops](scientific-engineering-2.md#lithops) - Run unmodified Python code at massive scale on any cloud, with no servers to manage
- [tensorizer](internet.md#tensorizer) - A tool for fast PyTorch module, model, and tensor serialization + deserialization.
- [pysphere](software-development-libraries-4.md#pysphere) - Python API for interacting with the vSphere Web Services SDK
- [cloudml-hypertune](internet.md#cloudml-hypertune) - A library to report Google CloudML Engine HyperTune metrics.
- [taskflow](software-development-libraries-4.md#taskflow) - Taskflow structured state management library.
- [ClusterShell](software-development-libraries-4.md#clustershell) - ClusterShell library and tools
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [mooncake-transfer-engine](scientific-engineering-artificial-intelligence.md#mooncake-transfer-engine) - A KVCache-centric Disaggregated Architecture for large-scale LLM inference and training.
- [torchmonarch](scientific-engineering-artificial-intelligence.md#torchmonarch) - Monarch: Single controller library
- [qctrl-client](internet-www-http-2.md#qctrl-client) - Q-CTRL Client
- [pydsdl](scientific-engineering-2.md#pydsdl) - Cyphal DSDL processing frontend
- [nunavut](scientific-engineering-2.md#nunavut) - Generate code from DSDL using Jinja2 templates.
- [cachekit](database-database-engines-servers.md#cachekit) - Backend-agnostic caching for Python — intent-based decorators with circuit breaker, distributed locking, Prometheus metrics, and optional zero-knowledge AES-256-GCM encryption, on a Rust-powered core. Zero-config L1 in-memory; scales to Redis, Memcached, File, or CachekitIO.
- [covalent](adaptive-technologies.md#covalent) - Covalent Workflow Tool
- [dask-geopandas](scientific-engineering-2.md#dask-geopandas) - Parallel GeoPandas with Dask
- [Spark](software-development-libraries-5.md#spark) - An easy to use actor model framework in Python
