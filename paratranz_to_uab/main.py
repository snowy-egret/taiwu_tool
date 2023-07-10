import csv
import os


def printwrite(text):
    log.write(f"{text}\n")
    print(text)


def patchfile(txt_file, csv_file, edited_file):
    # uab txt 원문 읽어서 리스트화
    with open(f"txt_files_original/{txt_file}", "r", encoding="utf-8") as f:
        txt_data = f.readlines()
        txt_data = [i.strip() for i in txt_data]
        txt_data = [i for i in txt_data if i != ""]

    # paratranz csv 번역문 읽어서 리스트화
    with open(f"paratranz_csv/{csv_file}", "r", encoding="utf-8-sig") as f:
        csv_data = csv.reader(f)
        csv_data = list(csv_data)

        # csv 파일이 비어있거나 BOM sig만 있을 경우 패스
        if len(csv_data) == 0 or csv_data[0][0] == "\ufeff":
            printwrite(f"[WARN] {csv_file} 파일이 비어있습니다. 파일을 건너뜁니다.")
            return None

        # 번역이 있는 행만 추출 (col:2)
        new_csv = []
        for i in csv_data:
            try:
                if i[1].strip() != "" and i[2].strip() != "":
                    new_csv.append([i[0], i[1], i[2]])
            except:
                pass
        csv_original = [i[1] for i in new_csv]
        csv_translated = [i[2] for i in new_csv]

    # 의미없는 코드지만 일단 냅둠.
    if len(csv_original) != len(csv_translated):
        printwrite(f"[WARN] {csv_file} 파일의 번역된 문장 개수가 원본 문장 개수와 다릅니다. 파일을 건너뜁니다.")
        return None

    # uab txt 원문과 paratranz csv 번역문 비교해서 import용 txt 파일 출력
    with open(
        f"txt_files_edited/{edited_file}", "w", encoding="utf-8", newline="\n"
    ) as f:
        for line in txt_data:
            stripped_line = line.strip()
            if stripped_line in csv_original:
                index = csv_original.index(line.strip())
                f.write(csv_translated[index] + "\n")
            else:
                f.write(stripped_line + "\n")
        printwrite(f"[----] {txt_file} 작업 완료")


# txt와 csv 파일 개수가 같은지 확인 (필요시 사용)
def check_files(txt_path, csv_path):
    txt_list = [
        os.path.splitext(i)[0].split("-CAB")[0]
        for i in os.listdir(txt_path)
        if i.endswith(".txt")
    ]
    csv_list = [
        os.path.splitext(i)[0] for i in os.listdir(csv_path) if i.endswith(".csv")
    ]
    if txt_list == csv_list:
        print("txt/csv 동일")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # 폴더관리
    if not os.path.exists("txt_files_original") or not os.path.exists("paratranz_csv"):
        print("txt_files_original 또는 csv_files 폴더가 없습니다.")
        input("엔터 키를 눌러 종료하세요...")
        exit()
    if not os.path.exists("txt_files_edited"):
        print("txt_files_edited 폴더가 없습니다. 폴더를 생성합니다.")
        os.mkdir("txt_files_edited")

    # 파일리스트 작성
    txt_list = [i for i in os.listdir("txt_files_original") if i.endswith(".txt")]
    csv_list = [i for i in os.listdir("paratranz_csv") if i.endswith(".csv")]
    if len(txt_list) != len(csv_list):
        print("txt 파일과 csv 파일의 개수가 다릅니다.")
        input("엔터 키를 눌러 종료하세요...")
        exit()

    log = open("log.txt", "w", encoding="utf-8")

    for i in range(len(txt_list)):
        try:
            patchfile(txt_list[i], csv_list[i], txt_list[i])
        except Exception as e:
            print(e)
            print(f"txt_files_original/{txt_list[i]}")
            print(f"paratranz_csv/{csv_list[i]}")
            exit()

    log.close()

    input("작업이 완료되었습니다. 엔터 키를 눌러 종료하세요...")
