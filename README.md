# Python Video Converter 

## Pre-requisitory
Pyhon3.8.2 and ffmpeg3.4.8

## Install Dependencies
Build VirtualEnv with require python version(optional)

pip install -r requirements.txt

## Command guide

### To convert single file 

```
python3 rescale_video.py -f="./videos/OneRepublic - Counting Stars (Official Music Video).mp4" -o="filepath/filename" (Dont need to specify .mp4)
```

-f command for desire filepath(relative or full path)
-o to save output file.

### To convert all videos from desire folder 

```
python3 rescale_video.py -d="./videos" -o="./output"
```
-d for folderpath to convert files.
-o for folderpath to save output files. 
Note: You dont need specify filename in both -f and -o for -d command.