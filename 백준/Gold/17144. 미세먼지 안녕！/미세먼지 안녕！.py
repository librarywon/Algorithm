from collections import deque

R, C, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
air_cleaner = []
for i in range(R):
    if m[i][0] == -1:
        air_cleaner.append(i)

# 동, 서, 남, 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 미세먼지 확산 처리
def spread_dust():
    new_m = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if m[i][j] > 0:
                spread_amount = m[i][j] // 5
                spread_count = 0
                for direction in range(4):
                    ny, nx = i + dy[direction], j + dx[direction]
                    if 0 <= ny < R and 0 <= nx < C and m[ny][nx] != -1:
                        new_m[ny][nx] += spread_amount
                        spread_count += 1
                new_m[i][j] += m[i][j] - spread_amount * spread_count
            elif m[i][j] == -1:
                new_m[i][j] = -1
    return new_m

# 공기청정기의 위쪽 바람 (반시계 방향)
def circulate_up():
    top = air_cleaner[0]
    # 왼쪽 세로
    for i in range(top - 1, 0, -1):
        m[i][0] = m[i - 1][0]
    # 위쪽 가로
    for i in range(C - 1):
        m[0][i] = m[0][i + 1]
    # 오른쪽 세로
    for i in range(top):
        m[i][C - 1] = m[i + 1][C - 1]
    # 아래쪽 가로
    for i in range(C - 1, 1, -1):
        m[top][i] = m[top][i - 1]
    m[top][1] = 0  # 공기청정기에서 나온 바람은 미세먼지가 없다

# 공기청정기의 아래쪽 바람 (시계 방향)
def circulate_down():
    bottom = air_cleaner[1]
    # 왼쪽 세로
    for i in range(bottom + 1, R - 1):
        m[i][0] = m[i + 1][0]
    # 아래쪽 가로
    for i in range(C - 1):
        m[R - 1][i] = m[R - 1][i + 1]
    # 오른쪽 세로
    for i in range(R - 1, bottom, -1):
        m[i][C - 1] = m[i - 1][C - 1]
    # 위쪽 가로
    for i in range(C - 1, 1, -1):
        m[bottom][i] = m[bottom][i - 1]
    m[bottom][1] = 0  # 공기청정기에서 나온 바람은 미세먼지가 없다

# 시뮬레이션 실행
for _ in range(T):
    m = spread_dust()  # 미세먼지 확산
    circulate_up()     # 위쪽 공기청정기 작동
    circulate_down()   # 아래쪽 공기청정기 작동

# T초가 지난 후 남아있는 미세먼지의 양 계산
answer = 0
for i in range(R):
    for j in range(C):
        if m[i][j] > 0:
            answer += m[i][j]

print(answer)
