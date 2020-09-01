import moviepy
import moviepy.editor as mp
import cv2
import argparse
import glob

def compress_480(file,output):
    video = mp.VideoFileClip(file)
    resize_video = video.resize(height=480)
    resize_video.write_videofile(f"{output}_480.mp4")

def compress_720(file,output):
    video = mp.VideoFileClip(file)
    resize_video = video.resize(height=720)
    resize_video.write_videofile(f"{output}_720.mp4")

def check_dimension(file):
    vid = cv2.VideoCapture(file)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    # print(width,height)
    return width,height

if __name__=="__main__":

    parser = argparse.ArgumentParser(description="Video Compressor")

    parser.add_argument("-d","--dir_path",type=str,action="store", help="Convert all videos in disire folder")
    parser.add_argument("-f","--file_path",type=str , action="store",  help="File path to video")
    parser.add_argument("-o","--output_path",type=str,action="store", help="Directory you want to save")
    parser.add_argument("-c","--check_resolution",type=str,action="store",help="To check Resolution of video file")
    # filepath = "./videos/OneRepublic - Counting Stars (Official Music Video).mp4"
    args = parser.parse_args()

    if args.file_path:
        width , height = check_dimension(args.file_path)
        print(f"Original resolution : {int(width)}x{int(height)}")
        if int(height) <= 720:
            print("false")
        else:
            print("")
            compress_480(file=args.file_path,output=args.output_path)
            compress_720(file=args.file_path,output=args.output_path)
            
    if args.dir_path:
        for video in glob.glob(f"{args.dir_path}/*.mp4"):
            print(video)
            filename = video.split("/")[-1]
            filename = filename.replace(".mp4","")
            output_file = f"{args.output_path}/{filename}"
            width , height = check_dimension(file=video)
            print(f"Original resolution : {int(width)}x{int(height)}")
            if int(height) <= 720:
                print("false")
            else:
                compress_480(file=video,output=output_file)
                compress_720(file= video,output=output_file)


    if args.check_resolution:
        width,height = check_dimension(args.check_resolution)
        print(f"Resolution of video file : {int(width)}x{int(height)}")


