from pandas import read_excel
from pandas import concat
import os
import datetime


def readname(filePath):
    #     filePath = 'G:\\workplace\\first\\SamplingAlgorithm\\datasets\\'
    name = os.listdir(filePath)
    return name


def psum(a, b):
    hs = ['H', 'h']
    nons = ['无', '/', '—', '未', '-', '不']
    s = 0
    a = list(a)
    b = list(b)
    for j in range(len(a)):
        a1 = str(a[j])
        k = sum(b)
        #         b1=b[i]
        a1 = a1.strip('>')
        a1 = a1.strip('<')
        if any(h in a1 for h in hs):
            a1 = a1.strip('H')
            a1 = a1.strip('h')
            a1 = float(a1)
            s = a1 * 60 * b[j] + s
            # print(a1)
            # print('现在的值:',s)
        elif any(non in a1 for non in nons):
            k = k - b[j]
            k = k - b[j]
        else:
            a1 = a1.strip('min')
            a1 = a1.strip('mins')
            a1 = a1.strip('分钟')
            a1 = float(a1)
            # print(a1)
            # print('现在的值s:', s)
            s = s + a1 * b[j]

    m = s / k
    # print(s)
    # print(k)
    return m


time = input()
filePath = 'D:/苏嘉豪/善诊项目/数据项目/健康顾问/数据统计/c/'
outputPath = 'D:/苏嘉豪/善诊项目/数据项目/健康顾问/数据统计/output/' + str(datetime.date.today())
name = readname(filePath)
# name = name.remove('dataC.xlsx')
# name = name.remove('healthstats.py')
print(name)
order1 = ['日期', '顾问', '添加用户量', '服务用户量', '前期用户', '老用户', '已完成问题数', '待完成问题数', '咨询医生量', '医生平均回复时间', '疾病咨询', '疫情症状咨询',
          '疫情防护',
          '其他咨询', '用户平均服务时长', '医生服务状态', '备注']
order2 = ['日期', '顾问', '添加用户量', '服务用户量', '前期用户', '老用户', '已完成问题数', '待完成问题数', '咨询医生量', '医生平均回复时间', '疾病咨询', '疫情症状咨询',
          '疫情防护',
          '其他咨询', '用户平均服务时长', '医生服务状态', '邮件标题准确率', '备注']
order = ['日期', '顾问', '是否排班', '实际工作时间', '添加用户量', '服务用户量', '前期用户', '老用户', '已完成问题数', '待完成问题数', '疾病咨询', '疫情症状咨询', '疫情防护',
         '其他咨询',
         '用户平均服务时长（min）', '咨询医生量', '医生平均回复时间', '医生服务状态', '邮件标题错误数', '备注']

i = 0
for s in name:
    i += 1
    path = filePath + s
    # print(path)
    try:
        df1 = read_excel(path, sheet_name='顾问日报')
    except:
        df1 = read_excel(path)
    # df1.dropna(axis='columns', thresh=8, inplace=True)
    try:
        df1.columns = order
        df1 = df1.drop(index=[0])
    except:
        df1.coloumns = order1
    #     print(df1)
    if i == 1:
        df = df1
    else:
        df = concat([df, df1], ignore_index=True)
df = df[order]
df = df.loc[df['日期'] == time]
df = df.fillna(0)
df = df.replace('反馈医学部', 0)
df = df.replace('-', 0)
df = df.replace('今日未上线', 0)
df = df.replace('轮休', 0)
df = df.replace('服务结束', 0)

df_b = df.query('顾问 == ["韩晓颖","陈胜","古亦斌","姜姗姗","刘青青","孙曼","宋晓妍"]')
df_c = df.query('顾问 != ["韩晓颖","陈胜","古亦斌","姜姗姗","刘青青","孙曼","宋晓妍"]')


# df = df[order]
def calcu(df):
    a = len(df)
    df.loc['new'] = 0
    for i in range(20):
        if i < 3:
            df.iloc[a, i] = df.iloc[0, i]
        # elif i < 10:
        #
        #     df.iloc[3, i] = sum(df.iloc[0:3, i])
        elif i > 3:
            if i == 14:
                try:
                    df.iloc[a, i] = psum(df.iloc[0:a, i], df.iloc[0:a, 5])
                except:
                    print(df.iloc[0:a, 1])
            elif i < 16 or i == 18:
                try:
                    df.iloc[a, i] = sum(df.iloc[0:a, i])
                except:
                    print(i)
                    print(df.iloc[0:a, i])
            elif i == 16:
                try:
                    df.iloc[a, i] = psum(df.iloc[0:a, i], df.iloc[0:a, i - 1])
                except:
                    print(i)
                    print(df.iloc[0:a, i])
    return df


df = calcu(df)

df.to_excel(outputPath + 'data.xlsx', encoding='gbk')
df_c = calcu(df_c)
df_c.to_excel(outputPath + 'datac.xlsx', encoding='gbk')
df_b = calcu(df_b)
df_b.to_excel(outputPath + 'datab.xlsx', encoding='gbk')


# df2 = read_excel('D:/苏嘉豪/善诊项目/数据项目/健康顾问/email.output.xlsx')
