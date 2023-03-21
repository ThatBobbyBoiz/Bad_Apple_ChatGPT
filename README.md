# Bad Apple ChatGPT
Bad Apple On ChatGPT

Table of conent:

1) Code explanation
2) Tutorial on how to recreate Bad Apple on ChatGPT

=========================================================

1) Code explanation

All these codes were written mostly by ChatGPT, I only made some slight modification to make the code works properly

a) create_ascii_art.py

- This python code will generate ascii art of every single frame of Bad Apple video 
(*) Require a full directory of extracted Bad Apple video frames (6571 frames to be exact)

b) run_bad_apple_chatgpt.js

- This javascript code will first fetch the ascii art from your github repo (must be public) in a set of range
- Then display all the fetched ascii frame in the message box on ChatGPT page
(*) Require:
+ A public Github repo with pre-generated Bad Apple frames
+ Edit the HTML code of ChatGPT page (more information in the tutorial part)

2) Tutorial on how to recreate Bad Apple on ChatGPT

Before doing this, it's advised to have some basic coding knowledge. Also, keep in mind that this is how I create the project, there is definitely better and more optimized way to do this, so feel free to do so (if possible also share it to others people who also want to achive this)

Firstly, you must download a Bad Apple video then extract the video into individual frames (around 6571 frames)
You can use many public code online to do this, personally, I would recommend this one "https://pypi.org/project/videotoframes/", and save all the extracted frames in a directory (e.g: Bad Apple Frames)

Secondly, you run "create_ascii_art.py" (remember to change the varible I specified in the code before running it) to convert all the Bad Apple frames into ascii art and save them in a specified directory

Thirdly, uploads all your ascii art file into your personal Github repo, and make it public

Ok, so the preparation is done, now let's log into your ChatGPT account (Note: I do this on ChatGPT web version, so app version may not work)

First, create a new chat or use your old chat (both works fine). Then enable Web Developer Tool (by pressing F12 key), and go to Inspector tab
In "Search HTML" box, type in "textarea", find one that looks like this:

<textarea tabindex="0" data-id="//ID" style="max-height: 200px; height: 24px; overflow-y: hidden;" rows="1" class="m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0"></textarea>

===========================================

Then right click the element and choose "Edit as HTML", then change the HTML code of textarea element into this:

<textarea tabindex="0" data-id="//ID" style="max-height: 200px; height: auto; overflow-y: hidden; font-size: 3px; white-space: pre-wrap; line-height: 6px; font-family: monospace;" rows="60" class="m-0 w-full resize-none border-0 bg-transparent p-0 pl-2 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent md:pl-0"></textarea>

===========================================

If you see the message box (the one you type your question to ask ChatGPT) has become bigger then you are set to go

Now, go to the Console tab and paste the content of the code "run_bad_apple_chatgpt.js" (remember to change the variable I specified in the code) into the console (if pasting is disabled, you can try typing "allow pasting" into the console)

Now the ascii art should be displayed in the message box, now I recommend waiting the code done fetching the ascii art from your Github repo, after it done fetching, click anywhere in the message box and the Bad Apple visual will be displayed (in loop)
