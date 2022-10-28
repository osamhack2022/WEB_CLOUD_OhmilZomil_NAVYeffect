
PART_NAME = {
    'rank_tag' : 'level_tag',
    'neckerchief' : 'neck',
}

def worker_2_front(msg:dict):
    # 이름 변경 및 숫자를 문자로 변경
    result = msg.copy()
    for part_name in msg.keys():
        if part_name in PART_NAME.keys():
            result[PART_NAME[part_name]] = result.pop(part_name)


    return result
    