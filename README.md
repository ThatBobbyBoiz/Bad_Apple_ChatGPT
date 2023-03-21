# Bad Apple On ChatGPT

## Table of Contents

- [Overview](#overview)
- [Code Explanation](#code-explanation)
- [Tutorial on How to Recreate Bad Apple on ChatGPT](#tutorial-on-how-to-recreate-bad-apple-on-chatgpt)

## Overview

This repository contains the code and instructions to recreate the Bad Apple video as ASCII art on ChatGPT. The process involves extracting frames from the original video, converting them into ASCII art, and displaying them in the ChatGPT message box.

## Code Explanation

The code for this project is divided into two parts:

### create_ascii_art.py

This Python code generates ASCII art of every frame of the Bad Apple video. It requires a full directory of extracted Bad Apple video frames (6571 frames to be exact).

### run_bad_apple_chatgpt.js

This JavaScript code fetches the ASCII art frames from your public GitHub repository and displays them in the message box on the ChatGPT page. It requires a public GitHub repository with pre-generated Bad Apple frames and editing of the HTML code of the ChatGPT page (more information in the tutorial).

## Tutorial on How to Recreate Bad Apple on ChatGPT

Before starting, it's advised to have some basic coding knowledge. Also, keep in mind that this is how I achieved this, and there may be better and more optimized ways to do it.

1. Download the Bad Apple video and extract it into individual frames (around 6571 frames). You can use many public code online to do this, personally, I would recommend this one: https://pypi.org/project/videotoframes/. Save all the extracted frames in a directory (e.g., Bad Apple Frames).

2. Run the `create_ascii_art.py` code (remember to change the variable I specified in the code before running it) to convert all the Bad Apple frames into ASCII art and save them in a specified directory.

3. Upload all your ASCII art files to your personal GitHub repository and make them public.

4. Log in to your ChatGPT account (Note: these instructions are for the ChatGPT web version, so the app version may not work).

5. Create a new chat or use an old chat. Then enable Web Developer Tool (by pressing F12 key) and go to the Inspector tab. In the "Search HTML" box, type "textarea" and find one that looks like this:

```html
<textarea tabindex="0" data-id="//ID" style="max-height: 200px; height: 24px; overflow-y: hidden;" rows="1" class="m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0"></textarea>```

6. Right-click on the element and choose "Edit as HTML." Then change the HTML code of the `textarea` element to this:

```html
<textarea tabindex="0" data-id="//ID" style="max-height: 200px; height: auto; overflow-y: hidden; font-size: 3px; white-space: pre-wrap; line-height: 6px; font-family: monospace;" rows="60" class="m-0 w-full resize-none border-0 bg-transparent p-0 pl-2 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent md:pl-0"></textarea>```

If you see your message box has become bigger, then you are good to proceed to the next step

7. Switch to the Console tab
