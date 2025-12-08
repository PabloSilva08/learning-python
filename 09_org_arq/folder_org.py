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
               print(f'Criando ==>> {tmp}')
            return(fold)
    if not (os.path.isdir(tmp := os.path.join(path_main, "Others_p"))):
       os.makedirs(tmp)
    return("Others_p")

def mv_arq(path_main, folder, target):
    path_old = os.path.join(path_main, target)
    path_new = os.path.join(path_main, folder, target)
    idx = 1
    while (os.path.isfile(path_new)):
        target_tmp = f"0{idx}_{target}"
        path_new = os.path.join(path_main, folder, target_tmp)
        idx += 1
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
###############################################################################
   >> """
    return(input(menu))

def ft_constructor_path(path_main: str) -> str:
    option = ft_menu()
    print('-'*40)
    if option == '1':
        if tmp := os.path.isdir(os.path.join(path_main, 'Desktop')):
            return(tmp)
        else:
            path_main = os.path.join(path_main, 'Área de trabalho')
            if not (os.path.isdir(path_main)):#Colocar uma exception
                print('Não foi encontrado Desktop')
    elif option == '2':
        path_main = os.path.join(path_main, 'Downloads')
    elif option == '3':
        partes = input("Digite o caminho a partir do home/: ")
        partes = partes.split(os.sep)
        for parte in partes:
            path_main = os.path.join(path_main, parte)
    elif option == 'diretorio atual':
        path_main = os.path.abspath('.') #Comando Oculto
    else:
        print(':D')
        return
    return(path_main)

def main() -> int:
    list_folder ={
        'Documentos_p':['.pdf', '.txt', '.odt', '.doc', '.docx', '.ppt', '.pptx'],
        'Imagem_p':['.jpg', '.jpeg', '.img', '.png', '.gif'],
        'Videos_p':['.mp4', '.flv', '.mov', '.mkv'],
        'Audio_p':['.mp3', '.wav'],
        'Code_p':['.py', '.html', '.c', '.c++', '.js', '.css'],
        'Compact_p':['.zip', '.rar', '.gz', '.7z', '.xz', '.bz2']
    }
    path_main = os.path.expanduser('~')
    path_main = ft_constructor_path(path_main)

    target_string = os.listdir(path_main)

    for target in target_string:
        if os.path.isdir(os.path.join(path_main,target)):
           continue 
        extension = str.lower(capture_extension(target))
        folder = create_folder(path_main, extension, list_folder)
        mv_arq(path_main, folder, target)
    print('-'*40)
    return(0)

if '__main__' == __name__:
    main()
