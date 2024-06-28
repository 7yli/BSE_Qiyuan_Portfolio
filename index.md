# Automatic object detect and pickingup Robotic Arm 
Replace this text with a brief description (2-3 sentences) of your project. This description should draw the reader in and make them interested in what you've built. You can include what the biggest challenges, takeaways, and triumphs from completing the project were. As you complete your portfolio, remember your audience is less familiar than you are with all that your project entails!

You should comment out all portions of your portfolio that you have not completed yet, as well as any instructions:
```HTML 
<!--- This is an HTML comment in Markdown -->
<!--- Anything between these symbols will not render on the published site -->
```

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Qiyuan L | Novi High School | Computer Science | Incoming Junior

**Replace the BlueStamp logo below with an image of yourself and your completed project. Follow the guide [here](https://tomcam.github.io/least-github-pages/adding-images-github-pages-site.html) if you need help.**

![Headstone Image](logo.svg)
  
# Final Milestone

**Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q6KZG2lSe8Q?si=f2Eo0bzgJ-JA7GE2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For the final milestone of my project, I successfully integrated the object detection function into the arm control system. I also programmed a useful feature based on this detection: when users click on any objects boxed on my camera video, the robotic arm moves towards the selected object.

I started by researching and deciding to use object detection from the OpenCV library. The process begins with capturing the camera image from the Pi camera and feeding it into the object detection model. The model draws boxes around each detected object so that users can clearly see them. I used JavaScript to identify the position of the mouse whenever it clicks. The data regarding the mouse's position and the position of the objects is then shared. I created another Python thread to control the robotic arm based on the data shared from the website. This control thread calculates the horizontal and vertical angles needed to rotate the arm to center the selected object in the camera's view, based on the camera's field of view and the coordinates of the ideal point. The calculated commands are sent to the arm, which is accurately controlled by adjusting the servo's rotation duration.

At this stage, my main task is configuring different rotation durations for various angles. I need to test different durations and check how far the object strays from the center each time to determine the most accurate rotation time for the servo.

The most valuable experience for me at Bluestamp was working as a full-stack programmer for the first time. I learned front-end website design and interactive programming, as well as back-end arm control coding. This greatly improved my programming skills and my ability to manage my time across different tasks. I am extremely grateful for this experience and have realized how enjoyable it is to complete such a significant project independently. I plan to continue pursuing programming in all its aspects and hope to complete more projects like this in the future.




# Second Milestone

**Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/VXQh1fdUkY0?si=D53kk2Zu2pXkTLyG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For the second milestone of the project, I successfully integrated a Raspberry Pi with an Arduino board which controls a robotic arm. This setup also includes configuring a Pi camera and establishing a web-based arm controller. The website features real-time imaging from the camera and incorporates two virtual joysticks that facilitate wireless control of the arm.

To facilitate communication between the Raspberry Pi and the Arduino, I utilized a USB cable, enabling data transfer between the two devices. The control data for the joysticks is encoded into a 16-character string simulating the data range of the real joystick data: left vertical, left horizontal, right vertical, and right horizontal. The website, built using the Python Flask framework due to its compatibility with various code modules, streams video using the Picamera2 library, with modifications based on a GitHub Picamera project. Additionally, I integrated two virtual joysticks into the website using the nibblejs library, a Node.js library that supports joystick functionality on web pages. User interactions with the joysticks update the joystick data in the website's database in real-time. A separate Python thread reads this data, converts it into the required 16-character format, and sends it to the Arduino, which then controls the robotic arm based on this input.

During this phase, I encountered several challenges. Initially, I struggled with understanding how Arduino handles serial data reception. After extensive research and consultation of Arduino's API documentation, I managed to configure the Arduino to receive data of a specific length from the Raspberry Pi. Another issue was ensuring that the joystick data from the web program was effectively shared with the Raspberry Pi's data transmission script. This was resolved by implementing a shared database accessible by both programs, simplifying the data-sharing process. Lastly, I observed that data occasionally got mixed up during transmission, likely because the Arduino couldn't process the incoming data quickly enough. To address this, I introduced a delay of 0.01 seconds between sending data batches, which stabilized the communication.

With the arm now controllable remotely and the camera functional, the next step involves fully integrating the camera into the arm control system. I plan to add an object detection module to the Raspberry Pi and program the arm to move towards objects it recognizes, aiming to automate the process of picking up specified items.
 
# First Milestone

**Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/hY5DLFtaSV8?si=44JIhAG7N4h_ehvb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
For my first milestone, I successfully assembled the robotic arm and tested all the electrical components, including servos and joysticks. I also managed to control the arm using a joystick. The robotic arm consists of 4 servos, several bearings, and is controlled by an Arduino Nano board. Although I encountered some challenges during the process, I resolved them by reviewing the source code and experimenting with different configurations.

The Arduino board is crucial to the functionality of the robot. It processes signals from the joystick and sends commands to the robotic arm based on these inputs. When activated, the Arduino waits for joystick movements. Moving the joystick sends a signal to the Arduino, which then calculates the necessary adjustments to the servos, allowing the arm to move to the desired position.

During the build, I faced a significant issue where the arm began moving erratically and would return to its original position, even though it had previously been functioning correctly. Initially, I suspected a misconfiguration of the servos. However, after checking the code and monitoring the servo angles by printing out servo angle data in the arduino monitor, the data in the Arduino matched the actual angles. Which means that it's not the problem of mis configuration. I then observed that the arm functioned correctly when connected to a computer but not when powered by a battery. This led me to believe that the issue was related to insufficient battery voltage. Replacing the battery resolved the problem. In retrospect, I realized that the prolonged connection between the arm and the battery had likely depleted the battery’s charge.

Next, I plan to integrate a Raspberry Pi with the Arduino to handle tasks requiring higher computational power, while the Arduino will continue controlling the mechanical components. I will also implement object recognition software on the Raspberry Pi. Ultimately, I aim to combine control of the robotic arm with object recognition to enable automatic object pickup by the arm.

# Schematics 
Here's where you'll put images of your schematics. [Tinkercad](https://www.tinkercad.com/blog/official-guide-to-tinkercad-circuits) and [Fritzing](https://fritzing.org/learning/) are both great resoruces to create professional schematic diagrams, though BSE recommends Tinkercad becuase it can be done easily and for free in the browser. 

# Code
[Here's the code for the controlling part of the arm](https://github.com/Cokoino/CKK0006/blob/master/Lesson%207%20-%20Control%20The%20Robot%20Arm/Code/Arm/Arm.ino)

# Bill of Materials
Here's all the part I used in the project. 

| **Part** | **Note** | **Price** | **Link** |
|:--:|:--:|:--:|:--:|
| Robotic Arm Kit | the main structure of the project | $49.99 | <a href="https://www.amazon.com/LK-COKOINO-Compliment-Engineering-Technology/dp/B081FG1JQ1"> Link </a> |
| Servo Shield | control the servo in the arm | $10.99 | <a href="https://www.amazon.com/HiLetgo-Expansion-Sensor-Arduino-Duemilanove/dp/B07VQRCC8F/ref=sr_1_1_sspa?crid=IY8280UJPZ8D&dib=eyJ2IjoiMSJ9.gOnvWbSP2fpJyjlzThZoFsFPHoeaF2QpSk_jNdngKIr1twGn_LzcDoaoxYvFyCU-mVjs0xm0675XcM9jJCRLlzDOmjbGgP1sIqUhTjt4NviT5cbtoA-UvEYAIHWDWIfkb2aFMmhgHU544Wc7YJiipzzt3fuSGamCrVeh0ONFUE7GqEzOyVIpGdjm_kZqEYrk4l6Ol054nebh1I2eZg7hcYRPAX8iNqbzSBQnTX3EaUY.ewdYdtnT9O7qRCuhV_2P0vAhp7a5Ue2sdk1REW8_gKI&dib_tag=se&keywords=arduino+nano+servo+shield&qid=1716857827&s=toys-and-games&sprefix=arduino+nano+servo+shield%2Ctoys-and-games%2C85&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"> Link </a> |
| Screwdriver Kit | assembling the arm | $6.99 | <a href="https://www.amazon.com/Small-Screwdriver-Set-Mini-Magnetic/dp/B08RYXKJW9/"> Link </a> |
| Electronics Kit | What the item is used for | $13.99 | <a href="https://www.amazon.com/Smraza-Electronics-Potentiometer-tie-Points-Breadboard/dp/B0B62RL725/ref=sxts_b2b_sx_reorder_acb_business?content-id=amzn1.sym.f63a3b0b-3a29-4a8e-8430-073528fe007f%3Aamzn1.sym.f63a3b0b-3a29-4a8e-8430-073528fe007f&crid=2IC3T44H3U3WG&cv_ct_cx=breadboard+kit&dib=eyJ2IjoiMSJ9.TUd5tu2T8rmms7ZuJ0UzmbtpLL1zsu93bQM0PzwnP4E.sT0V0vL_QtbYv8ymVTCcRkhFNgBtRvRiT7G4FT1oGTE&dib_tag=se&keywords=breadboard+kit&pd_rd_i=B0B62RL725&pd_rd_r=67e1f4ff-e3b9-44e4-b441-b4ae282f036b&pd_rd_w=UjFaP&pd_rd_wg=0xRoC&pf_rd_p=f63a3b0b-3a29-4a8e-8430-073528fe007f&pf_rd_r=BFGP77H27ZN31W4PZAW6&qid=1715911733&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=breadboard+kit%2Caps%2C109&sr=1-2-9f062ed5-8905-4cb9-ad7c-6ce62808241a"> Link </a> |
| 9V barrel jack | What the item is used for | $5.99 | <a href="https://www.amazon.com/DZS-Elec-Connector-Experimental-5-5x2-1mm/dp/B07FDS11ZY/ref=sr_1_5?crid=2KDQRHR9QTG87&dib=eyJ2IjoiMSJ9.QXzrFs_APhSZ1IJhcXZvMQHwewvRuQ3vr1brQtDco3W0bnAprDG7jH7ie8dBlokDPWbOLcDtgbrHrNUzcyb61YgxbGO0UFeN6K8ktLZDkV3jlxoO940ZYOk8jrd3G8yxrkH-cUJgXaiOka1FWDDJJssGcdvyH2WlPRHUtZKQgBpoGa4M3j8wwx3yssPZrOJK32Pfs9ZLtCibGXHxhNbXOBuXOisFlpDByQ2NJcndu5iOa0dZ8jknYgybT1KOyzP9_lSVyQNCkcxcjanEjyf4Z6jMdRX-G08K6SY7IM-agSA.UzM8eWF_dtBmatnqwrbt1mCm8-reUmM7Mqm3SWpbviM&dib_tag=se&keywords=9v+to+barrel+jack&qid=1716857906&s=electronics&sprefix=9v+to+barrel+jack%2Celectronics%2C98&sr=1-5"> Link </a> |
| DMM | What the item is used for | $12.99 | <a href="https://www.amazon.com/AstroAI-Digital-Multimeter-Voltage-Tester/dp/B01ISAMUA6/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.e8da13fc-7baf-46c3-926a-e7e8f63a520b%3Aamzn1.sym.e8da13fc-7baf-46c3-926a-e7e8f63a520b&cv_ct_cx=digital+multimeter&dib=eyJ2IjoiMSJ9.5LQumrfBR8l0mKnJCJlRg73dxpou0gqYD_ffU3srgs0Utegwth8GcQCSVXVzeZeLSJx5J3itz5TLdmJHsrVITQ.-00jRPoT-bBy26YC4LzQ-S4cYdztgmSMGb83_WEm6HY&dib_tag=se&keywords=digital+multimeter&pd_rd_i=B01ISAMUA6&pd_rd_r=e1ff2570-7e4a-4906-bc55-6f819d48d1bc&pd_rd_w=h7HgL&pd_rd_wg=0ZcFH&pf_rd_p=e8da13fc-7baf-46c3-926a-e7e8f63a520b&pf_rd_r=R6YKX3NXTDQ1PQP4H8RM&qid=1715911879&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1-7efdef4d-9875-47e1-927f-8c2c1c47ed49-"> Link </a> |
| 9V batteries | providing power | $Price | <a href="https://www.amazon.com/PILOCEL-6LR61-Long-Lasting-Valentines-Leak-Proof/dp/B0BJ26CHZB/ref=sr_1_3_sspa?crid=3511SX6MYKKBL&dib=eyJ2IjoiMSJ9.Z-4XNUoLU7xDvPhZtJr843dKP65QhCM0ndq0FoyLTjkcnyo4IE_ILted5n4lbtQjcX8ddZkev1nkVFf5C1ZngeYC1UpSQLRS_Sgw4_CcQxxX0KvSPTY_cT2lo8NlYQDEt-btclbNtAsETMIgGgyHriu3iVgjKfCZb8I28yCNafXD8gVpdv-KxjMBj7xAKs6dBxNrXGKP0Qmq1rzM4X8t7wiU0d6CIPaX5GGWqEs5iYiTV4kG7uDI9fOd3TajdsPoGMtnccsLRyqZokEovVawlJrBHVgBGVdfvJ92Jtp40Eg.gPtYaMWAxQxlRXxK7-IKgNnGAMz5QwbPooetyMRjljE&dib_tag=se&keywords=9v+batteries+4&qid=1716301403&s=electronics&sprefix=9v+batteries+4%2Celectronics%2C78&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"> Link </a> |
| power banks | providing power | $15.99 | <a href="https://www.amazon.com/gp/product/B0C7PHKKNK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1"> Link </a> |
| pi camera | providing power | $8.99 | <a href="https://www.amazon.com/gp/product/B07RWCGX5K/ref=ox_sc_act_title_1?smid=A2IAB2RW3LLT8D&psc=1"> Link </a> |
| pi camera cable | providing power | $Price | <a href="https://a.co/d/0ca8Yb6N"> Link </a> |
| raspberry pi | providing power | $93 | <a href="https://www.amazon.com/Vemico-Raspberry-Starter-Heatsinks-Screwdriver/dp/B09QGZ94M8/ref=sr_1_20?crid=3EO43F1FEOV0O&dib=eyJ2IjoiMSJ9.ualQ11OTmi8CjjOvKHbGSeoxaNIDkPpfJZtZyzHol1FvvEglqiwyyx0fx51TZiZ1aBaberSc_J42HaMFrKc4G4wzNZJZEEpXeUe5uPFLGOfeZg1JiJOFIRBWErdjcMSJmt9OiXh3fiaEklJDqjCH8YliLFrOMz2gDd9N61tXfyLELptXi2DxstQVgqAxXv9vJnZG8mc1uPn3ogYVtajj4NEvfs_J7KSsaUplZk2LAkNdh8C7VZAVCj9KGMicav_2LQeL3moiJ-zNLr78csIQdysoo0AdWn9HClXObBEGA2A.R84P9iUHYtjBbieyHy8tFMnaqBUBiYhKHI1MA9uJP1A&dib_tag=se&keywords=raspberry%2Bpi%2Bkit&qid=1716420057&s=electronics&sprefix=raspberry%2Bpi%2Bki%2Celectronics%2C105&sr=1-20&th=1"> Link </a> |

# Other Resources/Examples
One of the best parts about Github is that you can view how other people set up their own work. Here are some past BSE portfolios that are awesome examples. You can view how they set up their portfolio, and you can view their index.md files to understand how they implemented different portfolio components.
- [Example 1](https://trashytuber.github.io/YimingJiaBlueStamp/)
- [Example 2](https://sviatil0.github.io/Sviatoslav_BSE/)
- [Example 3](https://arneshkumar.github.io/arneshbluestamp/)

To watch the BSE tutorial on how to create a portfolio, click here.
