## TAIWU\_TOOL

태오회권의 한글화 작업에 사용하기 위해 만든 간단한 툴 모음입니다.

.py 파일 실행을 위해 최신 버전의 Python이 필요합니다. ([다운로드](https://www.python.org/downloads/))

> 폴더 / 주석 / README.md에서 사용되는 용어
> 
> *   paratranz: paratranz에서 사용되는 형식의 csv. (형식: col1:key, col2:원문, col3:번역문, col4:비고)
> *   uab: .uab 파일에 들어있는 txt (형식: 줄 단위 구분 일반 txt파일, EOL:LF)
> *   event:

### diff\_uab

구버전/신버전 게임의 uab 파일에서 내보낸 textasset을 대조하여 어떤 라인이 추가/삭제됐는지 알려줍니다.

폴더 내 복수의 파일들 일괄처리가 가능합니다.