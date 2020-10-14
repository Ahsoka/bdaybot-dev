# Plan to Order via Amazon
Dr. Neat has given us the ambitious goal to send a candy bar via a program by 10/20.  There are two options in achieving this goal, discussed in detail below.

## [Selenium](https://www.selenium.dev/)
### Background
Selenium is a package that allows you to control a web browser with code.  We could use this technology to control a web browser to visit Amazon, login with the given login information and purchase the item.

### Pros
* Relatively quick to setup given the time constraints.  There is not barrier to entry unlike the option below.
* Already (sort of) know how to use Selenium

### Cons
* Running this on the Linux server might prove a challenge, but this might more of a challenge due to ignorance as opposed to technical feasibility (Not necessarily a con but thought it was good idea to mention this)
* This solution seems a bit unconventional, which is not necessarily a con in itself, however, this raises the issue of possible unreliability.  However, in order to full validate this more testing will need to be conducted.
* Might be difficult to scale Selenium, but once again this might be more related to ignorance than technical feasibility.
* CAPTCHAs or any other "are you robot" detection tool will be nearly impossible to evade using Selenium, thus making this option **literally impossible**.

## [Zinc]
### Background
Zinc is REST API (fancy talk for an API you access data from and interacting with by visiting a website using either GET requests, POST requests, or other types of requests not mentioned here) that allows you to purchase items off of Amazon.

### Pros
* This method is highly reliable and proven.  It used by many companies and appears to be highly trustworthy.

### Cons
* In order to be verified by Zinc it takes an unknown amount of time, which most likely exceeds 1 week, thus making this solution impossible to execute on within the 1 week deadline.
* For conventional use cases, the monthly order minimum is $100, which is below the order limit for the current use case.  Unless this scales to the entire school, we will most likely be under the $100 monthly order minimum.  This issue might go away due to a recent message sent to the [Zinc] team asking if we could arrange a custom payment structure that would allow use the service without the $100 minimum.



## Implementation Details
For this particular project, I will be using Selenium, however, it is definitely worth keeping an eye on [Zinc].  [Zinc] is definitely a possible option to consider when the scaling the project.

The first step in using Selenium will be accessing the Amazon and logging with a given set of credentials.  The next step is accessing an item's page, given some unique identifier for an item.  After this we will need to order the aforementioned item, given some address.

[Zinc]: https://zincapi.com/
