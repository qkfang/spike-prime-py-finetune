from gpt import chat
import os
import sys



def Run(model, systemPrompt, message, roboConnected):
    # message = sys.argv[1]
    gptCmd = chat(model, systemPrompt, message)

    # cleanup ````
    gptCmd = gptCmd.replace("```python", "")
    gptCmd = gptCmd.replace("```", "")

    with open("code-template.py", "rt") as fin:
        with open("code.py", "wt") as fout:
            for line in fin:
                fout.write(line.replace('###code###', gptCmd))

    if(roboConnected):
        ampyPath = '/Library/Frameworks/Python.framework/Versions/Current/bin/ampy'
        usbPort = '/dev/tty.usbmodem204D367C4D501'
        scriptFile = '/users/dai/Desktop/finetune/repo/lego/code.py'
        cmd = f'{ampyPath} --port {usbPort} run {scriptFile}'
        os.system(cmd)



