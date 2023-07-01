import os


def printwrite(text):
    log.write(f"{text}\n")
    print(text)


def difffile(old, new):
    # 구버전 텍스트 파일 읽기
    with open(f"txt_files_old/{old}", "r", encoding="utf-8") as f:
        old_lines = [i.strip() for i in f.readlines()]
        old_lines = [i for i in old_lines if i != ""]

    # 신버전 텍스트 파일 읽기
    with open(f"txt_files_new/{new}", "r", encoding="utf-8") as f:
        new_lines = [i.strip() for i in f.readlines()]
        new_lines = [i for i in new_lines if i != ""]

    # 구버전에만 있는 텍스트 / 신버전에만 있는 텍스트 구하기
    only_old = [i for i in old_lines if i not in new_lines]
    only_new = [i for i in new_lines if i not in old_lines]

    # Error Handling: 차이점이 없을 경우 패스
    if len(only_old) == 0 and len(only_new) == 0:
        return None

    # 파일 이름 전처리
    try:
        filename = os.path.splitext(new)[0].split("-CAB")[0]
    except:
        filename = os.path.splitext(new)[0]

    # 로그 작성
    printwrite(f"파일 이름: {filename}")
    if len(only_old) != 0:
        printwrite("\t구버전에만 있는 텍스트:")
        for i in only_old:
            printwrite(f"\t{i}")
        printwrite("")
    if len(only_new) != 0:
        printwrite("\t신버전에만 있는 텍스트:")
        for i in only_new:
            printwrite(f"\t{i}")
    printwrite("\n")


if __name__ == "__main__":
    # 작업 디렉토리 설정
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    log = open("log.txt", "w", encoding="utf-8")

    # 구버전 / 신버전 텍스트 파일 목록 구하기
    old_list = [i for i in os.listdir("./txt_files_old") if i.endswith(".txt")]
    new_list = [i for i in os.listdir("./txt_files_new") if i.endswith(".txt")]

    # Error Handling: 파일 개수가 다를 경우
    if len(old_list) != len(new_list):
        printwrite("파일 개수가 다릅니다.")
        printwrite(f"구버전: {len(old_list)}개")
        printwrite(f"신버전: {len(new_list)}개")
        log.close()
        input("엔터 키를 눌러 종료하세요...")
        exit()

    for i in range(len(old_list)):
        difffile(old_list[i], new_list[i])

    log.close()
    input("작업이 완료되었습니다. 엔터 키를 눌러 종료하세요...")
