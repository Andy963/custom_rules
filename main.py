#!/usr/bin/python
# coding:utf-8


import os
import sys


# from parser import parse_logs, write_hosts_deny
# from custom_rules.parser import parse_logs
print(sys.path)
import par

def get_ips(f: str):
    """从文件中获取ip列表
    f: 文件路径
    """
    with open(f, 'r') as f:
        for line in f.readlines():
            if line.startswith('sshd:'):
                ip = line.split(':')[1].strip()
                yield ip


def get_cur(cur_file: str):
    """获取当前已有列表
    """
    cur_list = []
    for ip in get_ips(cur_file):
        cur_list.append(ip)
    return cur_list


def get_new(src_dir: str, cur_list: list):
    """获取新的列表"""
    new_list = []
    for f in os.listdir(src_dir):
        f_path = os.path.join(src_dir, f)
        for ip in get_ips(f_path):
            if ip not in cur_list:
                new_list.append(f"sshd:{ip}\n")
    return new_list


def start_new_line(f: str):
    """在文件末尾添加一个空行"""
    with open(f, 'a') as f:
        f.write('\n')


def append_file(f: str, new_list: list):
    """将新的列表追加文件"""
    with open(f, 'a') as f:
        f.writelines(new_list)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tar = os.path.join(base_dir, 'hosts.deny')
    cur_list = get_cur(tar)
    cur_count = len(cur_list)
    print(f'cur banned {cur_count} ips')
    block_ips = par.parse_logs()
    par.write_hosts_deny(block_ips)
    src_dir = os.path.join(base_dir, 'src')
    new_list = get_new(src_dir, cur_list)
    new_count = len(new_list)
    start_new_line(tar)
    append_file(tar, new_list)
    print(f"new banned {new_count} ips")
    print('Done!')
