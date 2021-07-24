import os
def move(foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


def createIfnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir()
files.remove("clear.py")

createIfnotexist('Images')
createIfnotexist('Docs')
createIfnotexist('Videos')
createIfnotexist('Others')
createIfnotexist('Music')
createIfnotexist('Executable Files')

imgExts = [".jpg",".png",".jpeg"]
docsExts = [".docx",".pdf",".txt",".ppt",".pptx"]
videoExts = [".mpeg",".mp4",".mkv"]
musicExts = [".mp3"]
exExts = [".exe"]

Images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]
video = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]
music = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]
executableFiles = [file for file in files if os.path.splitext(file)[1].lower() in exExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in musicExts) and (ext not in videoExts) and (ext not in docsExts) and (ext not in imgExts) and (ext not in exExts) and os.path.isfile(file):
        others.append(file)

move("Images", Images)
move("Docs", docs)
move("Videos", video)
move("Others", others)
move("Music", music)
move("Executable Files", executableFiles)


