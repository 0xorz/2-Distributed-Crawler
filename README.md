# Distributed-Crawler

```

   _____                   _   _____  _     _     _
  / ____|                 | | |  __ \| |   (_)   | |
 | (___   __ _ _   _  __ _| |_| |__) | |__  _ ___| |__
  \___ \ / _` | | | |/ _` | __|  ___/| '_ \| / __| '_ \
  ____) | (_| | |_| | (_| | |_| |    | | | | \__ \ | | | - Crawler
 |_____/ \__, |\__,_|\__,_|\__|_|    |_| |_|_|___/_| |_|
            | |
            |_|

```

Welcome to SquatPhish-Crawler. It is part of SquatPhish project to crawler the squatting domains for phishing pages detection.

A distributed crawler to capture screenshots and log the redirection 

- [x] web-based crawling
- [x] mobile-based-crawling
- [x] distributed-crawling using shared memory counter
- [ ] add JS tracking
- [ ] auto submitting forms and loggin


## Set up

```
bash install.sh
```

## Distributed Crawling :rocket: :rocket: :rocket:

We provide a distributed crawling framework to crawl a large number of URLs.

The idea borrows from Hadoop with MapReduce. We separate the URL list into different chunks (stored under chunk folder), we then apply
task dispatch for each sublist with a chunk ID.

<img src="https://github.com/SquatPhish/2-Distributed-Crawler/blob/master/test/Framework.png" width="600" height="200" />

### Instructions

The demo provides a step-by-step instruction to crawl FB squatting domains.
How to detect squatting domains can be referred to [SquatPhish-1](https://github.com/SquatPhish/1-Squatting-Domain-Identification)

We use the data test/crawl_demo_url_list.txt as an example:

1. Clean chunks and create data folder:
```
rm -rf chunks/*
```

2. Split the list into chunks: The first argument is the file. The second argument is the number of chunks.
urls.csv will be splited in 10 csv files under chunks/.

```
python3 split.py urls.csv 10
```


3. Compile the task dispatch:  You could define your PROC_MAX in task_dispatcher.c

```
## define PROC_MAX 5  //The maximum processes the machine can tolerate
gcc task_dispatcher.c --std=c99
```

4. Run jobs with an index range:
```
./a.out 0 10
```
You could separate tasks among different servers, e.g.,
```
server 1 >> ./a.out 0 2
server 2 >> ./a.out 3 4
server 3 >> ./a.out 5 10
```

5. Get results in a new data folder


## Disclaimer and Reference

This is a research prototype, use at your own risk.

If you feel this tool is useful, cite the tool as :dog2: SquatPhish :dog2: is highly appreiciated.