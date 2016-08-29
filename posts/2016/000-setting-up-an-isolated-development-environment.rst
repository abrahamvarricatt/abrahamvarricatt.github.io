.. title: Setting up an isolated development environment
.. date: 2016-08-29 20:06:00
.. tags:

I've lost count of how many times I've re-installed my operating system, just because of tool-bloat. For one project or the other, a tool or utility would be installed on my system, then another and before I knew it - either my computer would slow down or the different tools would have conflicts between themselves. Even if that didn't happen there were times when I would want to re-format my system, just to bring it to a 'fresh' state. 

This was a process that was proving to be very time-consuming - and often enough, risky as well. If I didn't have a spare internet connected device nearby, I might configure the installer to provide me with a brick! Surely, I could find a better use of my time than spending a significant portion of the month reinstalling my computer? Searching for a solution to this problem I came across,

##########
VirtualBox
##########

It seemed perfect for my needs - a relatively cheap way to bring up an experimental system, work with it and best of all - easy to destroy and recover from! I cannot describe how liberating it was to be able to create a virtual system for quick (and possibly destructive) experiment without worrying about damaging my host system!

Granted, there were a few drawbacks - I lost out a bit on performace - some compiles took longer to complete than before, but for testing functionality - it did the job. One thing that it didn't quite solve for me, was the issue of configuration.

Each and every time I needed to boot up a new virtual system, I would still have to spend a considerable effort just setting it up - root usernames, passwords, network settings, disk partitions . . . etc. And this doesn't quite cover the matter of sharing my work. Explaining to a collegue how to setup their own virtual enviroment meant writing a lot of documentation which was a pain to keep updated. 

Quite by accident I then discovered,

#######
Vagrant
#######

This is like a manager for virtual systems. It supports other virtulaization tools like vmware, but for my needs it acts as a wrapper around virtualbox. I like to think of it as a way to store my virtualbox settings in a textfile which I can add to the VCS. This makes it very easy to share with collegues and friends. Just send them the ``Vagrantfile`` configuration and ask them to run a single command,

.. code:: shell

    $ vagrant up

Because of the way vagrant works, it cannot use distribution ISO files directly. Instead, the project introduces something called Vagrant Boxes. These are a set of pre-build virutal images which can be used for testing. 

Recently, I encountered a very odd (and frustrating!) situation - Canonical or CentOS do not maintain updated versions of their operating systems in the vagrant-box archive. Sure, they publish the most recent builds to the archive, but after downloading, spending hours trying to fight against subtle bugs (eg: centos does not sync the ``/vagrant`` folder between guest and host very well - data just goes *missing* after a reboot!), I had enough. And it looks like I'm not alone. 

Fortunately, there is an open source movement working to keep stable vagrant-boxes in the archive - `the bento project <http://chef.github.io/bento/>`_\ . It's run by the folks behind Chef - a system provisioning tool (I perfer ansible). 

And this is what I use these days to setup an isolated environment,

.. code:: shell

    $ vagrant init bento/centos-7.2
    $ vagrant up

Change the init box to use whichever OS is needed. 


