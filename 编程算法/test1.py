#

import sys

if __name__ == "__main__":
    list_uid = []
    count = 0
    while True:
        input_uid = int(raw_input())
        if input_uid == 0:
            break
        # if input_uid not in list_uid:
        #     list_uid.append(input_uid)
        flag = True
        for i in list_uid:
            if len(list_uid) == 0:
                count += 1
                break
            else:
                if input_uid == i:
                    flag = False
                    break

        if flag:
            list_uid.append(input_uid)
            count += 1


    sys.stdout.write("%s" % count)
