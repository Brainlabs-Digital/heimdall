# Introduction

Heimdall is a python library that makes it very straightforward to quickly and easily create screenshots from web pages.

Heimdall knows about lots of common devices, and can simulate them (their resolution and user agent) when you request a screenshot. For example, you could take a screenshot as an original iPad might see a page. However, you can also specify resolution and user agent yourself.

You can also specify what format you'd like the output in, and whether you want to crop the image based on the display size, or if you would rather get the whole webpage.

# Installing Heimdall

Firstly, you need to install [phantomjs](http://phantomjs.org/):

	npm install phantomjs

Then simply install Heimdall via pip:

	pip install heimdall

You should now be good to go.

# Using Heimdall

Quick and easy:

	import heimdall

	heimdall.png("https://www.distilled.net/", device="Kindle Fire")
	heimdall.jpeg("https://www.facebook.com/", device="iPhone") # Will use iPhone 6
	heimdall.pdf("http://news.ycombinator.com", device="iPhone 3") # Specify a device version

	heimdall.png("http://www.apple.com/", full_page=True) # Don't crop the image
	heimdall.png("http://www.tomanthony.co.uk/", width=1440, height=900) # Specify own display size

If you want to would like to pass the file type in as a parameter for whatever reason, then that is easy:

	heimdall.save("https://www.distilled.net/", format="PNG", device="Galaxy S3")

# To Do

- Lots

# Why Heimdall?

Heimdall is the all seeing god of Norse mythology, and this was a hackday project so we got stuck there. :)

# Thanks

We are using Johan Dahlberg's fantastic [optparse-js library](https://github.com/jfd/optparse-js/blob/master/lib/optparse.js).

Thanks to [Raphaël Goetter](https://twitter.com/goetter) for (http://mydevice.io/), which we used to get some device resolutions.

# Contributing

See CONTRIBUTING file.

# License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License

See LICENSE file.