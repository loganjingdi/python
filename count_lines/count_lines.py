#!/usr/bin/env python3

import os

def count_lines(file_name):
    
    f = open(file_name)
    count = 0

    while True:
        line = f.readline()
        
        if not line:
            break
        
        count = count + 1

    f.close()

    return count


def count_dir_lines(dir_name):

    total_lines = 0

    file_nums = 0

# the function of os.walk is to 
    for root, dirs, files in os.walk(dir_name):

        for file in files:
            file_type = file.split('.')

            if len(file_type) > 1:
                
                # the value can be adjusted to yourself
                if file_type[1] not in ["c", "h"]:
                    continue
            
            else:
                continue
            
            file_name = root + "/" + file

            lines = count_lines(file_name)
            print(file_name + " : contains lines:" + repr(lines))

            file_nums = file_nums + 1
            total_lines = total_lines + lines

    print("total files: " + repr(file_nums))
    print("tatal lines: " + repr(total_lines))


if __name__ == '__main__' :
    
    # in the current path
    cur_path = os.path.split(os.path.realpath(__file__))[0]

    count_dir_lines(cur_path)

    input("press key to exit")

