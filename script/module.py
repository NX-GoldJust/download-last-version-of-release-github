def install_package(packages: list):
    from os import system
    for p in packages:
        system(f"pip install {p}")
        



    
def extract_file(file: str):
    
    
    import os
    from zipfile import ZipFile 
    from colorama import Fore
    print(Fore.GREEN+f"Extraction de {file} ...")
    with ZipFile(file, 'r') as zip: 
        zip.extractall()
    #supprime le rip
    os.remove(file)
    
def telecharge_file(url: str, e: bool=None):

    from requests import get
    import colorama, os
    from colorama import Fore
    
    name=os.path.basename(url)
    
    colorama.init(autoreset=True)
    if e:
        print(Fore.GREEN+f"Téléchargement en cours de {name} ...")
    file = get(url, allow_redirects=True)
    open(name, 'wb').write(file.content)
    
    
    try:
        
        
        if name[-4:] == ".zip":

            extract_file(name)
            
    except:
        pass
    
def get_link(url: str):
    import os, json
    telecharge_file(url)
    if os.path.exists("latest.json"):
        os.remove("latest.json")
    os.rename("latest", "latest.json")    
    with open('latest.json') as json_file:
        data = json.load(json_file)
    
    lien = []
    for asset in data["assets"]:
        lien.append(asset["browser_download_url"]) 
    os.remove("latest.json")
    #print(lien)
    for li in lien:
        
        telecharge_file(li, e=True)

def transforme_link(url: str):

    import os
    
    htt, fin = url.split("github.com")
    new = htt+"api.github.com/repos"+fin+"/releases/latest"
    
    get_link(new)

