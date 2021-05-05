import moviepy.editor as mp

def convert(file_name):
	clip = mp.VideoFileClip(file_name)
	clip.write_videofile("movie.mp4")
	return clip

#clip = convert("raw.gif")