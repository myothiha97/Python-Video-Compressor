# Python Video Compressor

## Pre-requisite
Pyhon3.8.2 , ffmpeg3.4.8 and pip

## Install Dependencies
Build VirtualEnv with require python version(optional)

To install dependencies , use the following command

```
pip install -r requirements.txt
```
## Command guide

### To convert single file 

```
python3 rescale_video.py -f="filepath/filename.mp4" -o="filepath/filename" (Dont need to specify .mp4 file extension for -o command)
```

-f command for desire filepath(relative or full path)
-o to save output file.

### To convert all videos from desire folder 

```
python3 rescale_video.py -d="input_filepath" -o="output_filepath"
```
-d for folderpath for input files
-o for folderpath to save output files. 
Note: You dont need specify filename in both command.