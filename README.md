## 과제: URL 단축 서비스 구현

### 개요
백엔드 직군 지원자: 송동훈

이메일: dreampath88@gmail.com

python version: 3.11

Docker version: 26.1.4

기타 라이브러리 버전은 `./config/server/requirements.txt` 참고

### 프로젝트 설명

본 프로젝트는 `description.md`를 바탕으로 만들어진 프로젝트이다. 데이터베이스로는 PostgreSQL를 선택했고
선정 이유는 다른 속성들과 쉽게 관계를 파악할 수 있을 것이라고 판단하여 선택했다. 유저를 기준으로 데이터를 선택적으로 정규화할 수 있고
데이터를 정규화하게 된다면 유저마다 어떤 url로부터 단축 url을 부여받았는지 확인하기 용이하고
얼마나 자주 조회를 했는지 확인하기 쉬울 것이라고 판단했다. 뿐만 아니라 유저로부터 얻을 수 있는 다른 데이터들과 join 연산을 통해 관계를 파악하기 용이할 것 같았다.
기본 요구사항을 포함하여 보너스 기능까지 구현했으며 단축 url 생성 라이브러리로는
`tsidpy`[링크](https://pypi.org/project/tsidpy/)를 사용했다.
`tsidpy`를 사용한 이유는 timestamp를 기준으로 random bit 등을 포함하여 hashing함으로써 보안성을 높일 수 있고
중복 가능성을 최소화할 것으로 판단했다.

   * (만약 단순히 url 단축을 목적으로 한다면 MongoDB를 선택하는 것이 속도나 확장성면에서 최선이다. 다만, 프로젝트 진행에 있어 초기에 DB 스택을 잘못 선택하여 과제 제출 마감 시간을 초과하여 dev 브랜치에 따로 개발을 진행했다.)

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
