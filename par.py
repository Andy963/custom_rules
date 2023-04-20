#!/usr/bin/python
# coding:utf-8
import os
import random
import re
from collections import defaultdict

PAT = re.compile(r'(?<=Invalid|Unable ).*?(\d+.\d+.\d+.\d+) port.*')


def list_logs(log_dir: str = './logs'):
    """获取日志文件列表"""
    for f in os.listdir(log_dir):
        f_path = os.path.join(log_dir, f)
        yield f_path


def get_invalid_ips(log_file: str):
    """分析日志得出不合法的ip"""
    with open(log_file, 'r') as f:
        for line in f.readlines():
            if 'Invalid' in line or 'Unable' in line:
                ip = PAT.search(line).group(1)
                yield ip


def parse_logs(log_dir: str = './logs'):
    """解析日志"""
    ip_counter = defaultdict(int)
    block_ips = []
    for log_file in list_logs(log_dir):
        for ip in get_invalid_ips(log_file):
            if ip not in block_ips:
                ip_counter[ip] += 1
                if ip_counter[ip] >= 5:
                    block_ips.append(ip)
    return block_ips


def write_hosts_deny(block_ips: list, hosts_deny: str = './src/hosts.deny'):
    """写入hosts.deny"""
    if os.path.exists(hosts_deny):
        name, ext = os.path.splitext(hosts_deny)
        new_hosts_deny = f'{name}{random.randint(1, 100)}{ext}'
        with open(new_hosts_deny, 'w', encoding='utf-8') as fp:
            for ip in block_ips:
                fp.write(f'sshd:{ip}')
