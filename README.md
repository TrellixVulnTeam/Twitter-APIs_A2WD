# Twitter-APIs

All the large social networks generate business thanks to the REST system, and Twitter, was not going to be left behind. 
Twitter’s API contains a set of APIs that can be combined to create an application for your business so you can benefit from the data offered.

Without REST APIs, horizontal growth would be much more complicated. 
As for Twitter, its REST API allows you to read and write Twitter data; in other words, it can be used to create new tweets, 
read user profiles and the data of followers (among other data from each profile), since it identifies the various Twitter applications and the users 
who register using OAuth authentication and authorization. The replies from the Twitter REST API are in JSON format.



Basic features of the Twitter API

●      The Twitter API has four main “objects”: Tweets, Users, Entities and Places.

●      It has daily restrictions for calls and changes in the API to protect Twitter from abuses. Specifically, the restriction is set up by the user, or better said, by a user access token. The frequency restrictions are divided into 15-minute intervals and all the evaluation criteria require authentication so unauthenticated calls cannot be made to the API.

●      The API is based on HTTP (over SSL), so the processes that require a specific HTTP method will return an error if the request is not correct.

●      There are specific parameters for requests to the API, generated paging and library restrictions to adapt API operation to this social network.

In addition to the REST API, the public Twitter API has an API for streaming that provides access to a high volume of tweets with low latency. 
Most developers mix and combine both APIs to generate their own application.
