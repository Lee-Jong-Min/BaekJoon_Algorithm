# 그리디 알고리즘

* 그리디 알고리즘(탐욕법)은 **현재 상황에서 지금 당장 좋은 것**만 고르는 방법
* 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
* 그리디 해법은 **정당성 분석**이 중요 
  * Why? <br/>
  단순히 가장 좋아 보이는 것을 반복적으로 선택할 시 최적의 해가 보장되는지 알 수 없기 때문
* **코딩 테스트 => 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 이를 추론해야 함**

### 예제 1 : 거스름돈
* 문제<br/>
  당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원,
  10원짜리 동전이 무한히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러
  주어야 할 동전의 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.<br/><br/>
* 문제 해결 아이디어<br/>
  * **가장 큰 화폐 단위**부터 돈을 거슬러 주면 됨
  * Why?<br/>
    * 화폐 단위에서 **큰 단위가 항상 작은 단위의 배수가 되는 경우** 작은 단위의 동전들을 종합해 다른
  해가 나올 수 없기 때문<br/>
    * **만약 큰 단위가 작은 단위의 배수가 아닌 경우 다른 해법을 생각해야 한다.**<br/>
    * ex) 800원을 거슬러 줘야하는 상황에서 500원, 400원, 100원이 존재한다.<br/>
      * case1) 가장 큰 화폐 단위부터 거슬러 주는 경우<br/>
      
        **화폐 단위**|500원|400원|100원
        ---|---|---|---|
        손님이 받은 개수|1개|0개|3개|

      * case2) 가장 큰 화폐 단위를 안 줄 경우<br/>
        
        **화폐 단위**|500원|400원|100원
        ---|---|---|---|
        손님이 받은 개수|0개|2개|0개|
        
* 코드 예시(Python)<br/>
  ~~~python
  n = 1260
  count = 0
  array = [500,100,50,10]
  for coin in array:
      count += n // coin
      n %= coin
  print(count)
  ~~~
* 시간 복잡도 분석<br/>
  * 화폐의 종류가 K라고 할때, **시간 복잡도는 O(K)**
  * 코드에서 반복문이 화폐의 종류만큼 실행되기 때문
  * 거슬러 줘야하는 금액과는 무관하며 **동전의 총 종류**에만 영향을 받음

### 예제2 : 1이 될 때까지
* 문제
  * 어떠한 수 **N이 1이 될 때까지** 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고
  합니다. 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
     1. N에서 1을 뺍니다.
     2. N을 K로 나눕니다.
  * 예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다. 이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다. 이는 N을 1로 만드는 최소 횟수입니다.
  * N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 **과정을 수행해야 하는 최소 횟수**를 구하는 프로그램을 작성하세요.
* 문제 조건
  * 난이도 🔵⚪⚪ |  풀이 시간 15분  |  시간제한 2초  |  메모리 제한 128MB
  * 입력 조건
    * 첫째 줄에 N(1 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백을 기준으로 하여 각각 자연수로
    주어집니다.
  * 출력 조건
    * 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다.
* 입력 예시
  ~~~
  25 5
  ~~~
* 출력 예시
  ~~~
  2
  ~~~
  
