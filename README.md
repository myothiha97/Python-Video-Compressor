# Python Video Compressor

## Pre-requisite
Pyhon3.8.2 , ffmpeg3.4.8 and pip

## Install Dependencies
Build VirtualEnv with require python version(optional)

To install dependencies , use the following command

```
pip install -r requirements.txt
```

If above command doesnt work , use following command

```
pip3 install -r requirements.txt
```

## Commandline Arguments

### To convert single file 

```
python3 compress_video.py -f="filepath/filename.mp4" -o="filepath/filename" (Dont need to specify .mp4 file extension for -o command)
```

-f for desire filepath(relative or full path) and -o to save output file.

### To convert all videos from desire folder 

```
python3 compress_video.py -d="input_folderpath" -o="output_folderpath"
```
-d for folderpath for input files and -o for folderpath to save output files.
Note: You dont need specify filename in both command arguments.

### To check resolution of video file 

```
python3 compress_video.py -c="filepath/filename.mp4"
```
