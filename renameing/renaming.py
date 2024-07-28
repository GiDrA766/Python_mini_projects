import os 

Path = 'Your Directory'

def rename_excels(Path:str):
    for root, directory, files in os.walk(Path):
        for name in files:
            rename_files(root, name)
            
def rename_files(root:str, name:str):
    new_name = ''
    if name.startswith('Tableau_') is False:
        new_name = 'Tableau_' + name
    new_path = os.path.join(root, new_name)
    old_path = os.path.join(root, name)
    print(new_path)
    os.rename(old_path, new_path)

if __name__ == '__main__':
        print(4)
        rename_excels(Path)