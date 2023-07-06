## FAQs
**1. Why are you not using the [Official Bodhi API](https://fedora-infra.github.io/bodhi/7.1/python_bindings.html) mantained by Bodhi Team?**

**A:** There are few reasons for this. When this project was in early stages of development, I had less idea of development processes based on APIs. While searching for API on Bodhi, I found three packages [Bodhi](https://pypi.org/project/bodhi/) ,[Bodhi client](https://pypi.org/project/bodhi-client/) and [Bodhi messages](https://pypi.org/project/bodhi-messages/). While it is clear now that Bodhi client needs to be used, back then I had no idea whether Bodhi client and Bodhi messages are related to Bodhi update notifications since unlike Bodhi, they had less description on what it is. Moreover, I also assumed that Bodhi client required authentication to get messages, which I wasn't able to implement perfectly at that time.

**2. Do you have any plans on using Bodhi API in future?**

**A:** Yes, I do. If there is going to be a next major release of gpkgstatus, then it will use [Official Bodhi API](https://fedora-infra.github.io/bodhi/7.1/python_bindings.html), which is maintained by Bodhi Team.

**3. Is there any significance of [this project](https://github.com/dkvc/gpkgstatus) when there is [Bodhi CLI](https://bodhi.readthedocs.io/en/stable/man_bodhi.html)?**

**A:** Based on docs, *bodhi is the command line interface to bodhi, Fedora’s update release management system. It can be used to create or modify updates and overrides.*. While it can do everything this project does, I needed a CLI that is read only and cross platform for Bodhi. 
<br>Whenever there is a package that breaks any functionality of Fedora, it won't be long for fix since the next update fixes it. To check whether package has updated, I have to check use package manager or [Bodhi](bodhi.fedoraproject.org) to check if update is available when I'm not using Fedora system.
To make this process easier, I had written a CLI to check Fedora updates that is read-only and cross-platform.

**4: Does this mean this project no longer receives updates?**

**A:** **gpkgstatus** will receive only one major update (as of date this page was written) that changes scraping to API. Then, this project will continue with minor updates, with no major refactors.

**5. Are there any plans for the project in future other than API or minor updates?**

It is highly probable that project will be moved from Python to a language that doesn't need dependencies or interpreter/compiler to run the program. This allows the program to run on embedded systems and also prevents systems from [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).
