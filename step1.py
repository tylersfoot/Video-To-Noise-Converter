import moviepy.editor as mp
import numpy as np
import os
from PIL import Image

def video_to_bw(video, threshold=128):
    '''
    converts the video to grayscale, which turns each frame from a 3d array (with color values) to a 2d array (with only brightness values)
    it then uses fl_image() to run a function on each frame, and ours takes the brightness of each pixel, and if it is above or below the threshold
    brightness, sets the pixel to pure black or pure white
    '''
    
    video_bw = video.fx(mp.vfx.blackwhite)
    
    def apply_threshold(frame):
        return (frame > threshold) * 255

    video_bw = video_bw.fl_image(apply_threshold)
    return video_bw

def print_video_info(video):
    # prints basic information about the video
    print(
    f'''
===================
Video Information:
FPS: {video.fps}
Dimensions: {video.size}
Duration: {video.duration} seconds
Number of Frames: {int(video.fps * video.duration)}
===================
    '''
    )
    
def generate_noise_image(video):
    '''
    creates a randomly generated image of colored noise
    it's the same dimensions as the input video
    '''
    
    width, height = video.size
    noise_array = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    noise_image = Image.fromarray(noise_array)

    return noise_image

# def create_noise_video(output_video_path, noise_image, video_duration, fps):
#     '''
#     this function creates a video the same length, dimensions, and fps as the original video
#     and sets each frame to be the random noise image we generated earlier
#     '''
#     # convert the noise image (PIL Image) to a numpy array and then to RGB format
#     noise_array_rgb = np.array(noise_image.convert('RGB'))

#     # create an array of noise images with the same dimensions as the original video
#     noise_images_rgb = [noise_array_rgb for _ in range(int(fps * video_duration))]

#     # create the ImageSequenceClip using the list of random images
#     noise_clip = mp.ImageSequenceClip(noise_images_rgb, fps=fps)

#     noise_clip.write_videofile(output_video_path, codec='libx264')

def combine_videos(output_video_path, bw_video, noise_image):
    '''
    combines the black and white video and the noise image
    for each frame in the black and white video, if the pixel is black (brightness is 0),
    it inverts the color of the corresponding pixel in the noise image
    '''
    # save the black and white video frames as an array
    bw_video_frames = list(bw_video.iter_frames())

    def combine_frames(bw_frame, noise_frame):
            # Convert the numpy array of the bw_frame to a PIL Image
            bw_image = Image.fromarray(bw_frame)

            # Convert the noise frame (PIL Image) to a numpy array
            noise_array = np.array(noise_frame)

            # Iterate through each pixel in the bw_frame
            for y in range(bw_image.height):
                for x in range(bw_image.width):
                    # Check if the pixel in the bw_frame is black (pixel value is 0)
                    if bw_image.getpixel((x, y)) == 0:
                        # Invert the color of the corresponding pixel in the noise image
                        noise_array[y, x] = 255 - noise_array[y, x]

            # Convert the numpy array back to a PIL Image
            combined_frame = Image.fromarray(noise_array)

            return np.array(combined_frame)

    # Create the final combined frames by iterating through each frame of bw_video and using the noise_image
    combined_frames = [combine_frames(bw_frame, noise_image) for bw_frame in bw_video_frames]

    # Create the final video using the combined frames
    combined_clip = mp.ImageSequenceClip(combined_frames, fps=bw_video.fps)

    # Write the combined clip to the output video file
    combined_clip.write_videofile(output_video_path, codec='libx264')

def main():
    output_folder = './videos/'
    input_video_name = 'input.mp4'
    bw_video_name = 'bw.mp4'
    noise_image_name = 'noise.png'
    # noise_video_name = 'noisevideo.mp4'
    final_video_name = 'finalvideo.mp4'
    
    # elete all files in the output folder except for input.mp4
    files_to_keep = ['input.mp4']
    for file in os.listdir(output_folder):
        if file not in files_to_keep:
            file_path = os.path.join(output_folder, file)
            os.remove(file_path)

    # load the video
    video = mp.VideoFileClip(output_folder + input_video_name)

    # print video information
    print_video_info(video)

    # convert the video to pure black and white
    print('Converting input video to pure black and white...')
    video_bw = video_to_bw(video, threshold=128)

    # save the black and white video
    video_bw.write_videofile(output_folder + bw_video_name, codec='libx264')
    print('Black and white video generated and saved!\n')
    
    # generate and save the noise image
    print('Generating noise image...')
    noise_image = generate_noise_image(video)
    noise_image.save(output_folder + noise_image_name)
    print('Noise image generated and saved!\n')
    
    # create the noise video with the same duration as the original video
    # print('Generating noise video...')
    # create_noise_video(output_folder + noise_video_name, noise_image, video.duration, video.fps)
    # print('Noise video generated and saved!\n')
    
    # combine the black and white video and the noise video
    print('Combining videos...')
    combine_videos(output_folder + final_video_name, video_bw, noise_image)
    print('Final video generated and saved!\n')

if __name__ == "__main__":
    main()
