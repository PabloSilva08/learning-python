import os

def capture_extension(target :str) -> str:
    index = target.rfind('.')
    if (index < 0):
        return('-1')
    return(target[index:])
    
def create_folder(path_main, extension, list_folder) -> str:
    for fold, ext in list_folder.items():
        if extension in ext:
            if not (os.path.isdir(tmp := os.path.join(path_main, fold))):
               os.makedirs(tmp)
            return(fold)
    if not (os.path.isdir(tmp := os.path.join(path_main, "Others"))):
       os.makedirs(tmp)
    return("Others")

def mv_arq(path_main, folder, target):
    path_old = os.path.join(path_main, target)
    path_new = os.path.join(path_main, folder, target)
    print(f'{target} -> {folder}')
    os.rename(path_old, path_new)

    
def main() -> int:
    list_folder ={
        'Documentos':['.pdf', '.txt', '.odt', '.doc', '.docx', '.ppt', '.pptx'],
        'Imagens':['.jpg', '.jpeg', '.img', '.png', '.gif'],
        'Videos':['.mp4', '.flv', '.mov', '.mkv'],
        'Audio':['.mp3', '.wav'],
        'Code':['.py', '.html', '.c', '.c++', '.js', '.css'],
        'Compact':['.zip', '.rar', '.gz', '.7z', '.xz', '.bz2']
    }
#    path_main = '/home/pablo/Downloads'
    path_main = os.path.abspath('.') #Para teste, retirar depois
    target_string = os.listdir(path_main)

    for target in target_string:
        if os.path.isdir(os.path.join(path_main,target)):
           continue 
        extension = str.lower(capture_extension(target))
        folder = create_folder(path_main, extension, list_folder)
        mv_arq(path_main, folder, target)
    return(0)

if '__main__' == __name__:
    main()
