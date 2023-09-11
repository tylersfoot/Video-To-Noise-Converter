import moviepy.editor as mp
import numpy as np
import os
import cv2
import time

def combine_frames(bw_frame, noise_image):
    # Create a copy of the noise image to avoid modifying the original
    noise_array = noise_image.copy()

    # Create a boolean mask for pixels that are black in the bw_frame
    mask_black_pixels = bw_frame[:, :, 0] == 0

    # Invert the color of the corresponding pixels in the noise image using the mask
    noise_array[mask_black_pixels] = 255 - noise_array[mask_black_pixels]

    return noise_array

def combine_videos(output_video_path, video, noise_image):
    # convert the video to grayscale and apply the threshold
    def apply_threshold(frame):
        bw_frame = (frame > 128) * 255
        return combine_frames(bw_frame, noise_image)

    # apply the combined transformation to each frame
    combined_clip = video.fl_image(apply_threshold)

    # write the combined clip to the output video file
    combined_clip.write_videofile(output_video_path, codec='libx264', verbose=False)

def main():
    output_folder = './videos/'
    input_video_name = 'input.mp4'
    final_video_name = 'output.mp4'

    start_time = time.time()
    
    # clean output folder
    files_to_keep = ['input.mp4']
    for file in os.listdir(output_folder):
        if file not in files_to_keep:
            file_path = os.path.join(output_folder, file)
            os.remove(file_path)

    # load input video
    video = mp.VideoFileClip(output_folder + input_video_name)
    
    print(
    f'''
===================
Video Information:
FPS: {video.fps}
Dimensions: {video.size}
Duration: {video.duration} seconds
Number of Frames: {int(video.fps * video.duration)}
Total Number of Pixels: {(int(video.fps * video.duration))*(video.size[0]*video.size[1])}
===================
    '''
    )

    # generate noise image using OpenCV
    noise_image = np.random.randint(0, 256, size=(video.size[1], video.size[0], 3), dtype=np.uint8)

    # combine the black and white video and the noise video
    combine_videos(output_folder + final_video_name, video, noise_image)
    
    total_time = time.time() - start_time
    print(f'Total time taken: {total_time:.2f} seconds')

if __name__ == "__main__":
    main()
