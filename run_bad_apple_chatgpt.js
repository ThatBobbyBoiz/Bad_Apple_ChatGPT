// Before running this code, you must edit the HTML code of <textarea>
// in the page code of ChatGPT, more information will be on README.md

{
  const startFrame = //num1;  //change this
  const endFrame = //num2;  //change this
  const messageBox = document.querySelector('[data-id="//ID"]');  //change this
  let currentFrame = 0;
  let asciiFrames = [];

  // Load all ASCII frames from the GitHub repository
  const loadAsciiFrames = async () => {
    try {
      for (let i = startFrame; i <= endFrame; i++) {
        const frameNumber = i.toString().padStart(3, '0');
        const frameURL = `https://raw.githubusercontent.com/username/username_repo/path/to/file/frame${frameNumber}.txt`; //change this (username/username_repo/path/to/file/)
        const response = await fetch(frameURL);
        const data = await response.text();
        asciiFrames.push(data);
        if (i === startFrame) {
          messageBox.innerHTML = asciiFrames[0];
        }
        await new Promise(resolve => setTimeout(resolve, 400));
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Load and display the next ASCII frame
  const loadAsciiFrame = () => {
    currentFrame = (currentFrame + 1) % asciiFrames.length;
    messageBox.innerHTML = asciiFrames[currentFrame];
  };

  // Add event listener to the message box to start the animation
  messageBox.addEventListener('click', () => {
    setInterval(loadAsciiFrame, 40);
  });

  // Load all ASCII frames and start the animation
  loadAsciiFrames();
}
