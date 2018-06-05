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

## How to Use

Run the demo:

```
node demo.js
```
<p float="left">
 <img src="https://github.com/SquatPhish/2-Distributed-Crawler/blob/master/test/fb-signin.screen.png" width="500" height="250" />
 <img src="https://github.com/SquatPhish/2-Distributed-Crawler/blob/master/test/fb-signin.screen.mobile.png" width="150" height="250" />
</p>


You will get a web version and a mobile version screenshot, their redirections and HTML source in test folder.


## Distributed Crawling :rocket: :rocket: :rocket:

We provide a distributed crawling framework to crawl a large number of URLs.

The idea borrows from Hadoop with MapReduce. We separate the URL list into different chunks (stored under chunk folder), we then apply
task dispatch for each sublist with a chunk ID.

<img src="https://github.com/SquatPhish/2-Distributed-Crawler/blob/master/test/Framework.png" width="600" height="200" />


The demo provides a step-by-step instruction to crawl FB squatting domains.
How to detect squatting domains can be referred to [SquatPhish-1](https://github.com/SquatPhish/1-Squatting-Domain-Identification)



## Disclaimer and Reference

This is a research prototype, use at your own risk.

If you feel this tool is useful, cite the tool as :dog2: SquatPhish :dog2: is highly appreiciated.


## Acknowledgement

Core contributor: ke tian @ririhedou

Thanks hang hu @0xorz for reproduction testing.

Current version is 0.0.2, updated at June 04 2018
