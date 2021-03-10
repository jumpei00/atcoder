def snuke_prime(N, C, event):
    event.sort()
    sum_fee = 0
    # この1日に払う料金はサブスクをしなかった時の一日あたりの料金を表す
    one_day_fee = 0
    day = 0
    for now_day, event_fee in event:
        # イベントの切り替わりの時に過去を振り返って、minを評価している
        # 1日ごとに支払った方がよかったか？それともサブスクが良かったか？を評価している
        sum_fee += min(C, one_day_fee) * (now_day - day)
        # 例えサブスクの方が良くても、1日ごとに支払うべき料金を計算していく
        # この値は次のイベント時にサブスク料金と比較される
        one_day_fee += event_fee
        day = now_day
    print(sum_fee)


N, C = map(int, input().split())
event = []
for _ in range(N):
    a, b, c = map(int, input().split())
    # a日目に料金が上がり、b+1日目に料金が下がる
    event.append((a, c))
    event.append((b + 1, -c))
snuke_prime(N, C, event)
