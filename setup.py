import subprocess

def install_bs4():
    print("*****Using pip3 to install beatiful soup.*****\n\n")
    return subprocess.check_call(list(["pip3", "install", "bs4"]))

def install_htmltab_reqs():
    print("*****Installing htmltab requirements.*****\n\n")
    return subprocess.check_call(["pip3", "install", "-r", "src/htmltab/requirements.txt"])

def install_htmltab():
    print("*****Installing htmltab.*****\n\n")
    return subprocess.check_call(["pip3", "install", "-e", "src/htmltab"])     

def main():
    install_bs4()
    install_htmltab_reqs()
    install_htmltab()

main()
