설명
이 스크립트는 큰 텍스트 파일을 작은 청크 단위로 분할하여 관리 및 처리를 용이하게 합니다.

사용 방법
python split_text_file_v2.0.py <원본 파일> <청크 크기_MB>

예시
python split_text_file_v2.0.py sample_org_file.txt 10

출력
스크립트는 원본 파일과 같은 이름의 폴더를 만들고 그 안에 청크 파일을 저장합니다. 청크 파일은 "원본 파일 이름" + 번호 + 확장자 형식으로 이름이 지정됩니다. 
예시: sample_org_file_0.txt, sample_org_file_1.txt 등

주의 사항
청크 크기는 메가바이트(MB) 단위로 지정됩니다.
스크립트는 원본 파일이 스크립트와 같은 디렉토리에 있다고 가정합니다. 
원본 파일이 다른 디렉토리에 있는 경우 스크립트를 적절하게 수정해야 합니다.

제작자: JaySon
도구: Llama3 70B

**Large Text File Splitter**
===========================

**Description**
This script splits a large text file into smaller chunks, making it easier to manage and process.

**Usage**
python split_text_file_v2.0.py <original_file> <chunk_size_mb>

**Example**
python split_text_file_v2.0.py sample_org_file.txt 10

**Output**
The script will create a folder with the same name as the original file, and save the chunk files inside it. 
The chunk files will be named as "original file name" + number + extension, for example: `sample_org_file_0.txt`, `sample_org_file_1.txt`, etc.

**Note**
* The chunk size is specified in megabytes (MB).
* The script assumes that the original file is in the same directory as the script. 
If the original file is in a different directory, you'll need to modify the script accordingly.

