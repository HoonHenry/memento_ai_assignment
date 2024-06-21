## 과제: URL 단축 서비스 구현

### 개요
백엔드 직군 지원자: 송동훈
이메일: dreampath88@gmail.com

python version: 3.11

Docker version: 26.1.4

기타 라이브러리 버전은 `./config/server/requirements.txt` 참고

### 작동 방법

- 참고: 해당 프로젝트는 과제 제출용이므로 환경변수 관련 정보가 노출되어 있습니다. `./config/**/.env` 참고

1. Docker Desktop 설치 ([링크](https://www.docker.com/products/docker-desktop/))
  - OS에 맞는 프로그램 설치
  - 설치 안내 메시지에 따라 설치
  - 설치 완료 확인
    ```sh
    # Check the version of Docker Desktop
    docker version
    ```
 
2. Source code 다운로드
   ```sh
   # Download the source code
   git clone https://https://github.com/HoonHenry/memento_ai_assignment

   # Move to the working directory
   cd memento_ai_assignment
   ```

3. Server 활성화
   ```sh
   # Move to the working directory
   cd memento_ai_assignment

   # Activate the server
   ./run_server.sh

   # Run the pytest
   # Plesase run this sh file in another terminal
   ./test_src.sh

   # Activate the server in background
   ./run_server.sh d

   # Restart the server, if necessary
   ./restart_server.sh
   ```
   
