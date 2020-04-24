# for i in range(1,51):
#     file_name = str(i)+"주차.txt"
#     report = open(file_name, "w", encoding="utf8")
#     print("- {0} 주차 주간보고 -".format(i), file=report)
#     print("부서 : 글쎼다" ,file=report)
#     print("이름 : 조영상" ,file=report)
#     print("업무 요약 : SO FAR SO GOOD" ,file=report)
#     report.close()

for i in range(1,2):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
