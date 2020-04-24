score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 100", file=score_file)
print("영어 : 100", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf=8")
print(score_file.readline(), end="")
print(score_file.read())
score_file.close()

print()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = tuple(score_file.readlines()) #list 형태로 저장한거야 list는 [] 요거겠지?
print(lines)
for line in lines:
    print(line)

score_file.close()