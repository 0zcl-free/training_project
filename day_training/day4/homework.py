#
#
# def gain(backend):
#     result_list = []
#     with open('work', 'r+', encoding='utf-8') as f:
#         flag = False
#         for line in f:
#             if line.strip().startswith('backend') and line.strip() == 'backend ' + backend:
#                 flag = True
#                 continue
#             if flag and line.strip().startswith('backend'):
#                 flag = False
#                 break
#             if flag and line.strip():
#                 result_list.append(line.strip())
#     return result_list
#
#
# def add(record, bk):
#     ret_list = gain(bk)
#     with open('work', 'r+', encoding='utf-8') as old, open('work2', 'r+', encoding='utf-8') as new:
#         flag = False
#         if not ret_list:
#             for line in old:
#                 new.write(line)
#             new.write('\nbackend ' + bk + '\n')
#             new.write(' ' * 8 + record)
#         else:
#
#             if record in ret_list:
#                 import shutil
#                 shutil.copy('work', 'work2')
#
#             else:
#                 ret_list.append(record)
#                 for line in old:
#                     if line.strip().startswith('backend') and line.strip() == 'backend ' + bk:
#                         flag = True
#                         new.write(line)
#                         for new_line in ret_list:
#                             new.write(' ' * 8 + new_line + '\n')
#                         continue
#                     if flag and line.strip().startswith('backend'):
#                         flag = False
#                     if not flag and line.strip():
#                         new.write(line)
#
#
#
#
# def main():
#     backend = "www.oldboy.org"
#     ret = gain(backend)
#     print(ret)
#
#     record = 'server 100.1.7.29 100.1.7.29 weight 20 maxconn 3000'
#     bk = 'buy.oldboy.org'
#     add(record, bk)
#
#
# main()