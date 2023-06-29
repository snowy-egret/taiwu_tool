import os


def difffile(old, new):
    with open(f"txt_files_old/{old}", "r", encoding="utf-8") as f:
        old_lines = f.readlines()
        old_lines = [i.strip() for i in old_lines]
        old_lines = [i for i in old_lines if i != ""]

    with open(f"txt_files_new/{new}", "r", encoding="utf-8") as f:
        new_lines = f.readlines()
        new_lines = [i.strip() for i in new_lines]
        new_lines = [i for i in new_lines if i != ""]

    only_old = [i for i in old_lines if i not in new_lines]
    only_new = [i for i in new_lines if i not in old_lines]

    if len(only_old) == 0 and len(only_new) == 0:
        return None
    try:
        filename = os.path.splitext(new)[0].split('-CAB')[0]
        log.write(f"파일 이름: {filename}\n")
        print(f"파일 이름: {filename}")
        
    except:
        filename = os.path.splitext(new)[0]
        log.write(f"파일 이름: {filename}\n")
        print(f"파일 이름: {filename}")
    if len(only_old) != 0:
        log.write("\t구버전에만 있는 텍스트:\n")
        print("\t구버전에만 있는 텍스트:")
        for i in only_old:
            log.write(f"\t{i}\n")
            print(f"\t{i}")
        log.write("\n")
        print("")
    if len(only_new) != 0:
        log.write("\t신버전에만 있는 텍스트:\n")
        print("\t신버전에만 있는 텍스트:")
        for i in only_new:
            log.write(f"\t{i}\n")
            print(f"\t{i}")
    log.write("\n\n")
    print("\n")

log = open("log.txt", "w", encoding="utf-8")

old_list = [i for i in os.listdir("txt_files_old") if i.endswith(".txt")]
new_list = [i for i in os.listdir("txt_files_new") if i.endswith(".txt")]

if len(old_list) != len(new_list):
    print("파일 개수가 다릅니다.\n")
    print(f"구버전: {len(old_list)}개\n")
    print(f"신버전: {len(new_list)}개\n")
    input("아무 키나 눌러 종료하세요...")
    log.close()
    exit()

for i in range(len(old_list)):
    difffile(old_list[i], new_list[i])



log.close()
input("작업을 완료했습니다. 종료하려면 엔터를 누르세요...")