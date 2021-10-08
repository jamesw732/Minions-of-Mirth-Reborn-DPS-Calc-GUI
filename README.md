# Minions-of-Mirth-Reborn-DPS-Calc

This is probably the worst written GUI program ever created (my first time using tkinter).

## Some notes on use
1. This program may not work if your name has the word "for" at the end of it. This might be a simple fix.
2. If you're trying to track the dps with a name that has more than one word, only put the first word of the name in the "Name" box. Getting around this is annoying and will create more problems similar to the "for" issue.
3. If your name is the same as the monster you're fighting, your stats will just be added together, and there's no way around this.
4. Logs are not quite updated in real time, which means that it is very easy to lose data, which can be catastrophic if you are only trying to see your stats for a short encounter. The best way around this would probably be to not use real time for the time (use regex instead), and also to only start and stop when the logs file is updated. Both of these are probably above my level at this point, but perhaps in the future I will change this.
5. You should be able to start/stop the dps tracking without relaunching the program, but I haven't bug tested this a whole lot yet.

I have no idea if the video works and I don't really care enough to test it.
