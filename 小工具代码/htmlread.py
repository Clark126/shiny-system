import re
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def contact(s,k,K):
    for k1 in range(k, K):
        if k1 == k:
            ss = s[k1]
        else:
            ss = ss + '\n' + s[k1]
    return ss


soup = BeautifulSoup(open('D:/苏嘉豪/善诊项目/数据项目/健康顾问/问题/test.html',encoding='utf-8'),features='html.parser')
# print(type(soup))
# print(type(soup.select('div.wiki-content')[0]))
tag = soup.select('div.wiki-content')[0]
# print(type(tag))
# for child in tag.children:
#     if isinstance(child,bs4.element.Tag):
#         print('------分隔符---------')
#         print(child)
title = list()
answer = list()
remark = list()
my_dict = dict()
for i in range(11):
    que = list()
    ans = list()
    h1 = tag.select('h2')[i]
    que.append(h1.get_text())
    # print(que)
    # print(tag.select('h1')[i].get_text())
    while h1.next_sibling.name !='h2':
        # print(h1.next_sibling.get_text())
        if isinstance(h1.next_sibling, bs4.element.Tag):
            ans.append(h1.next_sibling.get_text())
        else:
            break
        h1=h1.next_sibling
    # print(ans)
    title.append(que[0])
    k = 0
    K = len(ans)
    a = ans[0]
    while a.startswith('出处：') is False and k<K-1:
        k = k + 1
        a = ans[k]
    answ = contact(ans,0,k)
    rem = contact(ans,k,K)
    # while
    answer.append(answ)
    remark.append(rem)
# print(title)
# print(answer[0])
# print(answer)
# print(remark)
my_dict = dict()
my_dict['问题']= title
my_dict['答案']= answer
my_dict['备注']= remark
# print(my_dict)
df = pd.DataFrame(my_dict)
df.to_excel('D:/苏嘉豪/善诊项目/数据项目/健康顾问/问题/文本5.xlsx',encoding='gbk')
# print(df)
# my_dict = dict()
# k=0
# K=len(answer[0])
# a = answer[0][k]
# while a.startswith('出处：') is False:
#     k=k+1
#     print(a)
#     a = answer[0][k]


# for i in range(11):
#     if i==0:
#         my_dict['问题']=title[i]
#         my_dict['答案']=answer[i]
#     else:
#         my_dict['问题'] = my_dict['问题'].append(title[i])
#         my_dict['答案'] = my_dict['答案'].append(answer[i])
# print(my_dict)
#
# df = pd.DataFrame(my_dict)
# print(df)
# # print(s[15].prettify())
# # print(title)
# # print(answer)