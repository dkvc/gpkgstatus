## FAQs
**1. What does gpkgstatus mean?**

**A:** **gpkgstatus** stands for *Get Package Status*, since we are getting status of packages from Fedora Updates System.

**2. Why are you not using the [Official Bodhi API](https://fedora-infra.github.io/bodhi/7.1/python_bindings.html) mantained by Bodhi Team?**

**A:** There are few reasons for this. When this project was in early stages of development, I had less idea of development processes based on APIs. While searching for API on Bodhi, I found three packages [Bodhi](https://pypi.org/project/bodhi/) ,[Bodhi client](https://pypi.org/project/bodhi-client/) and [Bodhi messages](https://pypi.org/project/bodhi-messages/). While it is clear now that Bodhi client needs to be used, back then I had no idea whether Bodhi client and Bodhi messages are related to Bodhi update notifications since unlike Bodhi, they had less description on what it is. Moreover, I've also assumed that Bodhi client required authentication to get messages, which I wasn't able to implement perfectly at that time.

**3. Do you have any plans on using Bodhi API in future?**

**A:** Yes, I do. If there is going to be a next major release of gpkgstatus, then it will use [Official Bodhi API](https://fedora-infra.github.io/bodhi/7.1/python_bindings.html), which is maintained by Bodhi Team.

**4. If you know that testing is hitting limits of robots.txt (or almost DDoSing) the site, why didn't you stop it earlier?**

**A:** I apologize for oversight on my part. I had no idea that testing was DDoSing the site until I found that tests are failing for some reason on Github. I started tracking the issue down and it appears that testing across multiple python versions are DDoSing the site. I tried to add a sleep timer to avoid DDoSing based on *Crawl Delay* field of [robots.txt](https://bodhi.fedoraproject.org/robots.txt) on site temporarily. Since the next major update changes crawling to API, *the testing is no longer done automatically by Actions as well as no longer mantained*.

**5. Is there any significance of [this project](https://github.com/dkvc/gpkgstatus) when there is [Bodhi CLI](https://bodhi.readthedocs.io/en/stable/man_bodhi.html)?**

**A:** Based on Bodhi docs, it is stated that "*bodhi is the command line interface to bodhi, Fedora’s update release management system. It can be used to create or modify updates and overrides.*". While it can do everything this project does, I needed a CLI that is read only and cross platform for Bodhi. 
<br>Whenever there is a package that breaks any functionality of Fedora, it won't be long for fix since the next update fixes it. To check whether package has updated, I have to check use package manager or [Bodhi](bodhi.fedoraproject.org) to check if update is available when I'm not using Fedora system.
To make this process easier, I had written a CLI to check Fedora updates that is read-only and cross-platform.

**6: Does this mean this project no longer receives updates?**

**A:** **gpkgstatus** will receive only one major update (as of date this page was written) that changes crawling algorithm to using official API. Then, this project will continue with minor updates, with no major refactors.

**7. Are there any plans for the project in future other than change to API or minor updates?**

It is highly probable that project will be moved from Python to a language that doesn't need dependencies or interpreter/compiler to run the program. This allows the program to run on embedded systems and also prevents systems from [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).

**8. Does this mean end of python package on PyPI and Conda-Forge?**

While I have no plans on deprecating python package right now, it is quite possible that they might get deprecated. The deprecation notice will be given earlier than 3 months.
