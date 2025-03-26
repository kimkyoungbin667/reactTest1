# 베이스 이미지
FROM python:3.9

# 컨테이너 안에 작업 디렉토리 생성
WORKDIR /app

# requirements.txt 복사 & 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 전체 소스 코드 복사
COPY . /app

# 컨테이너 실행 시 실행할 명령어
CMD ["python", "app.py"]
