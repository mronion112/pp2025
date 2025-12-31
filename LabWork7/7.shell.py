import os

while True:

    pRead, pWrite = os.pipe()


    cmd = input("Your command : ")
    if cmd == 'exit':
        break
    if '|' in cmd:
        print("There have |")
        cmd = cmd.split('|')
        cmd1 = cmd[0].strip().split(' ')
        cmd2 = cmd[1].strip().split(' ')
    


        pid: int = os.fork()
        if pid == 0:
            os.close(pRead)
            os.dup2(pWrite, 1)
            os.close(pWrite)
            os.execvp(cmd1[0], cmd1)

        else:
            os.close(pWrite)
            os.dup2(pRead,0)
            os.close(pRead)
            os.execvp(cmd2[0], cmd2)

    elif '>' in cmd:
        print("There hava >")
        cmd = cmd.split('>')
        cmd1 = cmd[0].strip().split(' ')
        fileName = cmd[1].strip()
    


        pid: int = os.fork()
        if pid == 0:
            file = os.open(fileName, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
            os.dup2(file, 1)
            os.close(file)
            os.execvp(cmd1[0], cmd1)

        else:
           os.wait()
    elif '<' in cmd:
        print("There hava <")
        cmd = cmd.split('<')
        cmd1 = cmd[0].strip().split(' ')
        fileName = cmd[1].strip()
    


        pid: int = os.fork()
        if pid == 0:
            file = os.open(fileName, os.O_RDONLY)
            os.dup2(file, 0)
            os.close(file)
            os.execvp(cmd1[0], cmd1)

        else:
           os.wait()
    else:
        cmd = cmd.strip().split(" ")
        pid: int = os.fork()
        if(pid == 0):
            os.execvp(cmd[0], cmd)

        os.wait()
        


    







