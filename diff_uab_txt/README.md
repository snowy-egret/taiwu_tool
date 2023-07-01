## diff\_uab\_txt

구버전/신버전 게임의 uab 파일에서 내보낸 textasset을 대조하여 어떤 라인이 추가/삭제됐는지 알려줍니다.

폴더 내 복수의 파일들 일괄처리가 가능합니다.

### 사용법

*   일반적인 실행 방법

1.  **txt\_files\_old**에 구버전 텍스트, **txt\_files\_new**에 신버전 텍스트를 넣은 후
2.  main.py를 더블클릭하여 실행

*   cmd를 이용하는 방법

1.  **txt\_files\_old**에 구버전 텍스트, **txt\_files\_new**에 신버전 텍스트를 넣은 후
2.  cmd/powershell을 열어서 main.py가 있는 폴더까지 이동하고
3.  명령어 실행: **python main.py**

### input/output 형식

<table><tbody><tr><td rowspan="2"><p>input 1</p><p>(구버전에서 내보낸 원문 txt)</p></td><td>파일명 형식:&nbsp;</td><td>AvatarHairColors_language-CAB-{번들}-{pathid}.txt</td></tr><tr><td><p>내용 형식:&nbsp;</p><p>(일반 텍스트)</p></td><td>test1<br>test2<br>test3<br>test4<br>test5<br>test6<br>test7</td></tr><tr><td rowspan="2"><p>input 2</p><p>(신버전에서 내보낸 원문 txt)</p></td><td>파일명 형식:&nbsp;</td><td>AvatarHairColors_language-CAB-{번들}-{pathid}.txt</td></tr><tr><td><p>내용 형식:&nbsp;</p><p>(일반 텍스트)</p></td><td>test1<br>test2-edit<br>test3<br>test4<br>test6<br>test7<br>test8</td></tr><tr><td>output 1</td><td colspan="2"><p>파일 이름: AvatarHairColors_language<br>&nbsp; &nbsp; &nbsp; &nbsp;구버전에만 있는 텍스트:<br>&nbsp; &nbsp; &nbsp; &nbsp;test2<br>&nbsp; &nbsp; &nbsp; &nbsp;test5</p><p>&nbsp; &nbsp; &nbsp; &nbsp;신버전에만 있는 텍스트:<br>&nbsp; &nbsp; &nbsp; &nbsp;test2-edit<br>&nbsp; &nbsp; &nbsp; &nbsp;test8</p></td></tr><tr><td><p>output 2</p><p>(log.txt)</p></td><td colspan="2"><p>파일 이름: AvatarHairColors_language<br>&nbsp; &nbsp; 구버전에만 있는 텍스트:<br>&nbsp; &nbsp; test2<br>&nbsp; &nbsp; test5</p><p>신버전에만 있는 텍스트:<br>&nbsp; &nbsp; test2-edit<br>&nbsp; &nbsp; test8</p><p>&nbsp;</p></td></tr></tbody></table>