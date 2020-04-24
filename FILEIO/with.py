import pickle
#With를 통하여 file IO 를 간편하게 할 수 있습니다. 


#파일 알아서 꺼줘
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 힘들다 체력딸려")

with open("study.txt", "r", encoding="utf8") as read_file:
    print(read_file.read())