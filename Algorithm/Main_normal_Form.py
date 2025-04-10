import easygui as eg
import re
from prettytable import PrettyTable
msg="您可以选择复制下列标准逻辑运算符号进行输入：\n非：﹁\n合：∧\n析取：∨\n条件：→\n双条件：↔\n\
为了保证识别正确请按照标准符号格式输入。\n本页面仅提供提醒，\
建议进行复制（ctrl+c）后粘贴 "
'''eg.textbox(msg=)'''
 
print(msg)
    
def sift(string):
    find=re.compile(r"[(]+(.*)")
    #re.compile(pattern[,fiags])找相关符号，编译成正则表达式对象，方便后续调用及提高效率
    f=find.findall(string)
    return(f)
def judgment(string):#做真值表
    patten=re.compile(r"[(](.*?)[)]")
    fuhao=patten.findall(string)
    for i in range(len(fuhao)): #对所有元素进行遍历过滤掉括号
        if fuhao[i].startswith("("):#判断字符串是否以（开头
            fuaho[i]=sift(fuaho[i])
    a=re.compile("[a-zA-Z]")#匹配字符集，即提取变量
    attain=a.findall(string)
    l=attain+fuhao
    ls=[]
    for i in l:
        if i not in ls:
            ls.append(i)
    ls.append(string)
    ls.sort(key=len)
    return([ls,attain])
def priority(operator):#根据符号判定运算优先级
    p=-1
    if operator=="(":
        p=5
    elif operator=="﹁":
        p=4
    elif operator=="∧":
        p=3
    elif operator=="∨":
        p=2
    elif operator=="→":
        p=1
    elif operator=="↔":
        p=0
    return(p)
def operation(a,operator,b):#运算的表达
    if operator =="﹁":
        bool= not a
    elif operator =="∧":
        bool= a and b
    elif operator =="∨":
        bool= a or b
    elif operator =="→":
        bool= (not b) or a
    elif operator =="↔":
        bool= ((not a) and (not b)) or (a and b)
    else:
        print("运算符不合法，请重新尝试。")
        return(None)
    if(bool):#真值表初步
        return(1)
    else:
        return(0)
def compute(changeipt,m):
    i=0#准备建立栈
    digit_ls=[]
    symbol_ls=[]
    while i<len(changeipt) or len(symbol_ls)!=0:
        if i<len(changeipt):
            j=changeipt[i]
        else:
            j=""
        if j.isalpha():#判断字符串是否只由字母组成,返回布尔值
            digit_ls.append(m[j])
            i=i+1
        else:
            if len(symbol_ls)==0 or(j!=")"and symbol_ls[-1]=="(")or priority(j)>=priority(symbol_ls[-1]):#判断之二
                symbol_ls.append(j)
                i=i+1
                continue
            if  j==")" and symbol_ls[-1]=="(":
                symbol_ls.pop()
                i=i+1
                continue
            if (i>=len(changeipt)and len(symbol_ls)!=0)or(j==")"and symbol_ls[-1]!="(")or priority(j)<=priority(symbol_ls[-1]):
                opt=symbol_ls.pop()
                if opt!="﹁":
                    result=operation(digit_ls.pop(),opt,digit_ls.pop())
                elif opt=="﹁":
                    result=operation(digit_ls.pop(),opt)
                digit_ls.append(result)
    return(digit_ls[0])#为范式基础
def makels(x):#初步做出真值表
    number=len(x)
    ls=[]
    for i in range(2**number):
        Set=bin(i)[2:].zfill(number)
        downls=list(map(lambda j:int(j),list(Set)))
        ls.append(dict(zip(x,downls)))
    return(ls)
def Total(downls,top):#算出真值表的数据
    Tot=[]#接收数据
    for truelin in downls:
        every=[]
        for L in top:
            truth=compute(L,truelin)
            every.append(truth)
        Tot.append(every)
    return(Tot)
def Minimal(t):#极小项
    if len(t)!=0:
        return("("+"∧".join(t)+")")
    else:
        return("")
def bigger(t):#极大项
    if len(t)!=0:
        return("("+"∨".join(t)+")")
    else:
        return("")
def Or(y,x):
    w=makels(x)
    minterms=[]
    alline=Total(w,y)
    for liname in range(2**len(x)):
        ls=[]
        if alline[liname][-1]==1:#该行值使表达式为1
            for t in w[liname]:
                if w[liname][t]==1:
                    ls.append(t)
                else:
                    ls.append('﹁'+t)
        minterm=Minimal(ls)   #表达式为1,加入极小项列表
        if minterm!='':
            minterms.append(minterm)
    return("∨".join(minterms))
def adn(y,x):
    w=makels(x)
    maxsetpuls=[]
    alline=Total(w,y)
    for liname in range(2**len(x)):
        ls=[]
        if alline[liname][-1]==0:#该行值使表达式为0
            for t in w[liname]:
                if w[liname][t]==0:
                    ls.append(t)
                else:
                    ls.append('﹁'+t)
        maxset=bigger(ls)  #表达式为1,加入极大项列表
        if maxset!='':
            maxsetpuls.append(maxset)
    return("∧".join(maxsetpuls))
getin=input("请输入需要计算的式子\n：")
change=judgment(getin)[0]
q=judgment(getin)[1]
x=[]
for i in q:
    if i not in x:
        x.append(i)
w=makels(x)
alline=[]
for realine in w:
    every=[]
    for K in change:
        truth=compute(K,realine)
        every.append(truth)
    alline.append(every)  
form=PrettyTable(change)
for line in alline:
    form.add_row(line)
print(form)
print("主析取范式为: "+Or(change,x))
print("主合取范式为: "+adn(change,x))