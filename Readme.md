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

- Kobart
- Hyper clova(Kogpt)

## 평가 지표 설정 & 함수 만들기

- 기본적으로 정답 label 은 title로 설정
- ROUGE
- RDASS (https://kakaoenterprise.github.io/deepdive/210729)

## train 코드 짜고 tuning

- Fine Tuning!!!
- Matchsum 이 되어야 할 듯

1. 비교적 간단한 구현
2. 만약에 여러 문장을 하나의 문장으로 바꾸는 paraphrase가 가능하다면 abstractive도 가능할지도?

- (https://arxiv.org/pdf/1909.08752.pdf)

3. but, 각 문장 별로 분리하는 전처리 필요!

## 모델에 따른 성능 비교

- wandb 를 활용한 비교 예상

## 추가적으로 필요하다고 느끼는 문제점들

- 형태소 단위의 띄어쓰기에서 문제가 생김-> 직접 라벨링 또는 정제
