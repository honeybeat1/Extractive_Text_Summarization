## Intro

대략 2주간의 시간 동안 스포츠 기사를 summarization 하는 project 를 진행하였습니다. 학습 데이터셋은 약 6개월 간의 축구 뉴스 기사 데이터로 기사 제목, 기사 내용, 그리고 기사의 발행일이 정리되어 있었습니다.

## True Summary를 생성한 방식 및 근거

1. 데이터셋에서 주어진 제목

- ROUGE score 로 점수를 매길 경우 summarization 방식과 관계없이 점수가 낮을 가능성이 높음

2. pretrained Kobart로 생성한 문장들

- 모델이 생성한 라벨을 True label로 두기에는 신뢰도의 문제가 있을 수 있음

## 기본적인 전처리

- 쓸모없는 문구 제거 및 Okt를 활용한 형태소 단위로 분리
- text 내용을 문장단위로 분리 후 list로 저장

## 평가 지표 함수-RDASS

- 유사도 추론 모델을 활용해 text-answer , answer-label 사이의 코사인 유사도를 평균냄
- 의미론적인 접근이 가능하나 긴 inference time과 기준 모델의 부재라는 단점도 존재함

## 선정된 모델-MATCHSUM

- Extractive
- Encoder 는 KoBART
- summarization 가능성이 높은 5개의 문장을 탐색하고 그 중 2,3 개를 조합하여 정답 문장을 생성
- 평가 기준을 rdass로 바꾼 것에 따라 5개의 문장 탐색 기준도 rdass로 바꿈 -> 모델은 train 중인 encoder(KoBART)
- 메모리 부족의 이유 + 선정되는 5개의 문장이 훈련 됨에 따라 학습하기를 바람

## 모델 훈련 과정

- optimizer : AdamW
- lr : 1e-4
- scheduler : Cosine Annealing LR -> 홀수 epoch 마다 lr가 1/10이 됨

## 최종 결과

- 제목 라벨 모델의 Score: 평균 = 0.91, 표준편차 = 0.01438
- KoBart로 생성된 라벨 모델의 Score: 평균 = 0.93, 표준편차 = 0.01513

## 추가적인 결과 분석

- 두 라벨로 생성된 결과 모두 비교적 높은 score가 나온 것으로 인해 서로가 서로의 이유를 보완해준다고 느꼈다.
- 제목 또한 훌륭한 summarization 이 가능하다
- KoBART로 생성한 문장들이더라도 결국엔 모델에 차이가 있으므로 어느 정도 편차가 있게 결과물이 생성되었다.
- 유사도 모델(RoBERTa-small)에 기초한 RDASS 가 훈련에 전혀 참여하지 않았음에도 불구하고 높은 결과를 얻어서 놀라웠다.
