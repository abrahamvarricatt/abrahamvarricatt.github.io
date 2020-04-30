:title: Showing asterisks in terminal
:date: 2020-04-30

It is very useful to see ``***`` symbols appearing I type passwords in the
terminal window. Sadly, the feature is not enabled by default when using 
``sudo`` in Ubuntu. Thankfully, it is simple to activate!

.. PELICAN_END_SUMMARY 

Just open a new terminal and run the following command,

```
$ sudo visudo
```

It should open a file in a text editor (Nano at the time of typing). We need to
change the following line from,

```
Defaults env_reset
```

to

```
Defaults env_reset,pwfeedback
```

Press ``Ctrl + X`` followed by ``Y`` to save the file. Voila! We will now have
asterisks when typing passwords in our terminal. 
