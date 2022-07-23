Question : Create a web application backend in any of your desired
framework of python which should be having
● An api endpoint to receive video file
● Add validation in length, type and size of video file
● The video cannot exceed 10 min of length, 1GB of size and it
should be either mp4 or mkv
● Another api endpoint which can respond with a list of videos
being uploaded.
● You are free to add filters like get the video uploaded in a
particular date, or size range. We leave this creativity to you.
● Treat this application like a video storing application, so also add
one another api which will take video size, length and type as
input, do validation and return charges to the user as applicable.
● Charges : 5$ for video below 500MB and 12.5$ above 500MB.
Additional 12.5$ if the video is under 6 minutes 18 second and
20$ if above.


Solution:

● api endpoint which can respond with a list of videosbeing uploaded {http://127.0.0.1:8000/videos/}
● api endpoint to receive video file {http://127.0.0.1:8000/videos/uploads/}
●  filters like get the video uploaded in aparticular date      {http://127.0.0.1:8000/videos/date/}
●  video cannot exceed  1GB of size and itshould be either mp4 or mkv
● do validation and return charges to the user as applicable in the terminal while uploading
