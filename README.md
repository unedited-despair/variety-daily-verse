# Description

This is a variety plugin. You need to install [variety](https://github.com/varietywalls/variety) first to make it work.

This simple script fetches a random verse from [bible-api.com](https://bible-api.com).
It is based on Xing Yi's [VOTD from BibleGateway](https://github.com/Crissium/variety-daily-verse).

So far, the only supported version is the American Standard Bible version from 1901.
It would be simple to support the other versions already supported by bible-api.com.
I just did not implement this yet.

# How to use

First download the script with the following command:

```bash
curl -o $HOME/.config/variety/plugins/verse-new.py https://raw.githubusercontent.com/unedited-despair/variety-daily-verse/master/verse.py
```

Then restart `variety` and go to Preferences > Quotes > Sources and Filtering,
uncheck all checkboxes except, of course, "bible-api.com's Verse of the Day".
The Tags and Authors fields are not in use.
Only one _random_ version is displayed at a time.

_NB: `variety` sets an upper limit of 250 on the length of the quote,
and sometimes the daily verse exceeds this.
If you see the message 'Could not find any quotes',
you could try increasing the limit in `~/.config/variety/variety.conf`
by setting `quotes_max_length` to 4096 or something._