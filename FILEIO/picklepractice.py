import pickle
#프로그램 파일형식으로
profile_file = open("profile.pickle","wb") #writing binary
profile = {"이름":"박명수","나이":30, "취미":["축구", "골프"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()