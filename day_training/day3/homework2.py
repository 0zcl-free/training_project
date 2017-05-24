#
# def gain(backend):
#     """
#     获得对应backend的记录
#     :param backend: backend
#     :return: 返回列表
#     """
#     result = []           #创建空列表
#     with open('work', 'r+', encoding='utf-8') as f:
#         flag = False              #标志置为False
#         for line in f:
#             if line.strip().startswith('backend') and line.strip() == 'backend ' + backend:
#                 flag = True            #读到对应backend时，将标志置为True,再往下读有两种可能，一种读记录，一种是再次遇到backend
#                 continue
#             if flag and line.strip().startswith('backend'):      #再次遇到别的backend
#                 flag = False                         #将标志置为False,则不往下读
#                 break
#             if flag and line.strip():                #标志为True，则读记录
#                 result.append(line.strip())           #将记录添加到内存列表
#
#     return result          #返回列表
#
#
#
# def add(backend, record):
#     """
#     添加对应 backend记录
#     :param backend: backend
#     :param record: 要添加的记录
#     :return:
#     """
#     record_list = gain(backend)              #获得对应 backend记录，将记录存在列表
#     if not record_list:                     #若 列表为空，即backend 的记录不存在
#         with open('work', 'r+',encoding='utf-8') as old, open('work2', 'r+', encoding='utf-8') as new:
#             for line in old:
#                 new.write(line)       #先把旧的写到新的
#             new.write('\nbackend ' + backend + '\n')        #再将新添加的记录写到后面
#             new.write(' ' * 8 + record)
#
#     else:    #backend的记录存在
#         if  record in record_list:         #若记录已经存在，则不增加，直接把旧的复制到新的
#             import shutil
#             shutil.copy('work', 'work2')
#
#         else:                              #记录不存在，则增加
#             record_list.append(record)     #列表有对应backend所有记录
#             with open('work', 'r+', encoding='utf-8') as old, open('work2', 'r+', encoding='utf-8') as new:
#                 flag = False
#                 for line in old:
#                     if line.strip().startswith('backend') and line.strip() == 'backend ' + backend:
#                         flag = True
#                         new.write(line)
#                         for new_line in record_list:
#                             new.write(' ' * 8 + new_line +'\n')
#                         continue
#
#                     if flag and line.strip().startswith('backend'):
#                         flag = False
#
#                     if not flag and line.strip():
#                         new.write(line)
#
#
#
# bk = 'www.oldboy.org'
# #rd = 'server 100.1.2.2 100.1.2.2 weight 20 maxconn 30'
# #add(bk,rd)
#
#
#
# ret = gain('www.oldboy.org')
# print(ret)         #打印对应backend的记录
