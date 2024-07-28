import os
import eyed3
import translit
import mutagen

Directory = 'D:\\matlog'

def tagging(Directory : str):
    for root, directory, filenames in os.walk(Directory):
        for names in filenames:
            set_tags(os.path.join(root,names))
            
def set_tags(filename : str):
    if filename.endswith('.mp4'):
        mp = mutagen.mp4.MP4(filename)
        mp.tags['\xa9nam'] = 'Yourname'
        mp.tags['\xa9ART'] = 'Artist'
        mp.tags['\xa9alb'] = 'favorite album'
        mp.tags['\xa9day'] = '?????'
        mp.save()
    print(__name__)
    tagging(Directory)
