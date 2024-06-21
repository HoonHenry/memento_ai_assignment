## 과제: URL 단축 서비스 구현

### 개요
백엔드 직군 지원자: 송동훈

이메일: dreampath88@gmail.com

python version: 3.11

Docker version: 26.1.4

기타 라이브러리 버전은 `./config/server/requirements.txt` 참고

### 프로젝트 설명

본 프로젝트는 `description.md`를 바탕으로 만들어진 프로젝트입니다. 데이터베이스로는 PostgreSQL를 선택했고
선정 이유는 회원관리를 감안하여 선택했습니다. 관계형 데이터베이스를 사용함으로써 유저가 어떤 url에 대한 단축 url을
부여받았는지 확인하기 용이하고 얼마나 자주 조회를 했는지 확인하기 쉬울 것이라고
판단했다.
기본 요구사항을 포함하여 보너스 기능까지 구현했으며 단축 url 생성 라이브러리로는 `tsidpy`를 사용했다.
`tsidpy`를 사용한 이유는 timestamp를 기준으로 random bit를 사용함으로써 보안성을 높일 수 있고
중복 가능성 최소화할 것으로 판단했다.

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
   
