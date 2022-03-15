# 해야할 일 list

- 전처리
- 모델 찾기
- 평가 지표 설정 & 함수 만들기
- train 코드 짜고 tuning
- 모델에 따른 성능 비교

## 전처리

- 패턴을 찾을 수 있는 불용어, 특수문자 제거
- 크롤링하면서 생긴 불필요한 워딩 제거
- \n 제거
- 형태소 단위의 띄어쓰기 적용(https://needjarvis.tistory.com/645)

## 모델 찾기

- Hyper clova(Kogpt)
- ???

## 평가 지표 설정 & 함수 만들기

- 기본적으로 정답 label 은 title로 설정
- ROUGE
- RDASS (https://kakaoenterprise.github.io/deepdive/210729) (꽤나 오랜 시간 소요 될 것으로 예상)

## train 코드 짜고 tuning

## 모델에 따른 성능 비교

- wandb 를 활용한 비교 예상

## 추가적으로 필요하다고 느끼는 문제점들

- 형태소 단위의 띄어쓰기에서 문제가 생김-> 직접 라벨링 또는 정제
-
