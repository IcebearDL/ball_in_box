import sys
import os
with open('id.txt', 'r') as fp:
    idlist = fp.readlines()
    idlist = [line.rstrip('\n') for line in idlist]

os.system("rm result;touch result")
# 准备运行文件

for id in idlist:
    os.system("mkdir "+id)
    print("Cloning "+id)
    os.system("cd "+id+";if cd ball_in_box; then git pull; else git clone --depth=1 https://github.com/"+id+"/ball_in_box.git; fi")  # 这里的cd只影响当前行代码
    os.system("cp area_sum(gitclone).py "+id+"/ball_in_box/ball_in_box")
    os.system("cp validate.py "+id+"/ball_in_box/ball_in_box")
    os.system("cp __init__.py "+id+"/ball_in_box/ball_in_box")

#记录运行结果

for id in idlist:
    print("testing "+id)
    os.system("cd "+id+"/ball_in_box; python ball_in_box/area_sum.py ")
    print(id+" finished")
    
# 排序
with open('result', 'r') as fp:
    resultlist = fp.readlines()
    # resultlist = [line.rstrip('\n') for line in resultlist] 
    # 不用去除换行符,等会还要打出来


failee = []
succee = []
for res in resultlist:
    res = res.split(' ')
    if len(res) == 5:
        succee.append(res)
    else:
        failee.append(res)

succee.sort(key=lambda x:x[2],reverse=True)
with open('re-result','w') as re:
    for id in succee+failee:
        re.write(' '.join(id))
        