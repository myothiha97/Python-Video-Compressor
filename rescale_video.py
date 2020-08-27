import cv2
import numpy
import csv
import time
import argparse
import glob

def convert_480_300(file,save_dir):
    cap = cv2.VideoCapture(file)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(f'{save_dir}_480.mp4',fourcc, 20.0, (480,300))
    print("Video resolution rescale to 480x300")
    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame,(480,300),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("------------------>Finished Rescaling <----------------------")

def convert_720_400(file,save_dir):
    cap = cv2.VideoCapture(file)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(f'{save_dir}_720.mp4',fourcc, 20.0, (720,400))
    print("Video resolution rescale to 720x400")
    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame,(720,400),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("------------------>Finished Rescaling <----------------------")

def check_dimension(file):
    vid = cv2.VideoCapture(file)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    # print(width,height)
    return width,height

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Video Converter")
    
    parser.add_argument("-d","--dir_path",type=str,action="store", help="Convert all videos in disire folder")
    parser.add_argument("-f","--file_path",type=str , action="store",  help="File path to video")
    parser.add_argument("-o","--output_path",type=str,action="store", help="Directory you want to save")
    # filepath = "./videos/OneRepublic - Counting Stars (Official Music Video).mp4"
    args = parser.parse_args()

    if args.dir_path:
        for video in glob.glob(f"{args.dir_path}/*.mp4"):
            print(video)
            filename = video.split("/")[-1]
            filename = filename.replace(".mp4","")
            output_file = f"{args.output_path}/{filename}"
            width , height = check_dimension(file=video)
            print(f"Original resolution : {int(width)}x{int(height)}")
            if int(width) <= 720:
                print("Video resolution cannot be changed")
            else:
                convert_480_300(file=video,save_dir=output_file)
                convert_720_400(file= video,save_dir=output_file)

    if args.file_path:
        width , height = check_dimension(file=args.file_path)
        print(f"Original resolution : {int(width)}x{int(height)}")
        if int(width) <= 720:
            print("Video resolution cannot be changed")
        else:
            convert_480_300(file=args.file_path,save_dir=args.output_path)
            convert_720_400(file= args.file_path,save_dir=args.output_path)