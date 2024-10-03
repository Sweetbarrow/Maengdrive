# Maengdrive
# This project will be merged to other project. Please refer to [IMX](https://github.com/Fradhyle/IMX) Project
## Django 기반 웹사이트 및 예약 일정 관리 시스템 구축 프로젝트
### 환경
- Anaconda (최신 버전 유지)
- Django (최신 버전 유지)
### 목표
#### 최소 기능 제품 구현
##### 디자인은 최대한 나중에
- [ ] 데이터베이스 구성
    - [ ] 이용자 데이터베이스
        - [ ] 한 테이블에서 직원과 회원 정보를 모두 관리
        - [ ] 지점별 그룹 또는 직원 여부 Boolean으로 접근 권한 분리
    - [ ] 지점 데이터베이스
        - [ ] 지점명, 주소, 전화번호만 들어가면 됨
        - [ ] 운영 시간은 일정 테이블에서 관리  
            클래스 분리로 가능함
    - [ ] 일정 데이터베이스
        - [ ] 시간표, 지점 운영 시간 등이 포함되어야 함
        - [ ] 평일과 주말 및 공휴일 시간 별도
- [ ] 웹 프론트
    - [ ] 시스템 내에서 정보 편집 기능
    - [ ] 회원 계약 정보 및 진행 상황 보기
- [ ] 일정 관리
    - [ ] 현행 스프레드시트처럼 보이게
    - [ ] 일정 클릭하면 회원 정보 불러오기
    - [ ] 일정 추가, 편집, 삭제 기능
### 주의사항
1. ```whitenoise```는 테스트 환경 구성을 위한 것이므로, 실환경에서는 HTTP 서버 구축을 통해 static 파일을 서비스할 것
2. Azure Web App의 경우 DB로 SQLite를 사용할 수 없음. 실환경에서 다른 DBMS 사용을 고려할 것
3. HTML 작성시 속성 입력 순서는 다음에 따를 것  
https://codeguide.co/#attribute-order  
