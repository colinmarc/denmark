denmark - open markdown files in your browser
=============================================

This is a quick utility that lets you open markdown files in your default web browser:

![markdown!](http://www.colinmarc.com/denmark.png)

installation
------------

First you need markdown2:

```
sudo pip install markdown2
```

then just run `sudo setup.py install` from the source directory.

usage
-----

to open a markdown file in your default browser, just do:

```
denmark readme.md
```

bonus: double click to open
---------------------------

I've only tested this on ubuntu 11.04.

First, you need to create an Overrides.xml file in the mime/packages directory (if you already have an Overrides.xml, you'll have to copy the entry in instead):

```
sudo cat markdown.xml > /usr/share/mime/packages/Overrides.xml
```

And update the mimetypes database:

```
sudo update-mime-database /usr/share/mime
```

Finally, add a line in your defaults file (again, may differ based on distro):

```
sudo echo "text/x-web-markdown=denmark.desktop" >> /etc/gnome/defaults.list
```

You'll probably need to re-open nautilus before the changes will take hold, but then you should be able to double click markdown files to open them.

notes
-----

* The css I used to make it all pretty is [markdown.css](http://kevinburke.bitbucket.org/markdowncss/). 
* It works by creating temp html files in /tmp or your distro equivalent. In ubuntu, these are cleaned up on startup, but if they're not for you, you might have to clean them up manually. For some reason deleting during the process was too fast for my browser to load the file.
