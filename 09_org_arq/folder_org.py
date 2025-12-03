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

def ft_menu() -> str:
    menu = """
###############################################################################
    Você gostaria de:
    1 - Organizar o Desktop.
    2 - Organizar o Dowload.
    3 - Digitar o caminho do diretório.
    Ou digite qualquer coisa para sair.
##############################################################################
   >> """
    return(input(menu))

def ft_constructor_path(path_main: str) -> str:
    option = ft_menu()
    if option == '1':
        if os.path.isdir(os.path.join(path_main, 'Desktop')):
            print('Desk')
        else:
            path_main = os.path.join(path_main, 'Área de trabalho')
            if (os.path.isdir(path_main)):
                print('oooooooooooooooooooooook')
#        print(path_main)
    elif option == '2':
        path_main = os.path.join(path_main, 'Downloads')
 #       print(path_main)
    elif option == '3':
        partes = input("Digite o caminho a partir do home/: ")
        partes = partes.split(os.sep)
        for parte in partes:
            path_main = os.path.join(path_main, parte)
#        print(path_main)
    elif option == 'diretorio atual':
        path_main = os.path.abspath('.') #Para teste, retirar depois
#        print(path_main)
    else:
        print(':D')
        return
    return(path_main)

def main() -> int:
    list_folder ={
        'Documentos':['.pdf', '.txt', '.odt', '.doc', '.docx', '.ppt', '.pptx'],
        'Imagens':['.jpg', '.jpeg', '.img', '.png', '.gif'],
        'Videos':['.mp4', '.flv', '.mov', '.mkv'],
        'Audio':['.mp3', '.wav'],
        'Code':['.py', '.html', '.c', '.c++', '.js', '.css'],
        'Compact':['.zip', '.rar', '.gz', '.7z', '.xz', '.bz2']
    }
    path_main = os.path.expanduser('~')
    path_main = ft_constructor_path(path_main)
    print(f'O path_main é: {path_main}')

    target_string = os.listdir(path_main)
#    print(target_string)

#    for target in target_string:
#        if os.path.isdir(os.path.join(path_main,target)):
#           continue 
#        extension = str.lower(capture_extension(target))
#        folder = create_folder(path_main, extension, list_folder)
#        mv_arq(path_main, folder, target)
    return(0)

if '__main__' == __name__:
    main()
