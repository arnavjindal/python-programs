from pygame import mixer
import time


mixer.init()
inpu_start_ = str(input("Enter \"start\" to initiate the program: "))

def getdate():
    return str(time.strftime("%a, %d %b %Y %I:%M:%S %p ", time.localtime()))


done="done"

def main():
    code_breaker_counter=time.perf_counter() #28800
    glasses_of_water_drank = 0
    water_brk_time = 1500  #1500 ~~20mis
    eyes_brk_time = 1800    #1800 ~~30mis
    phy_brk_time = 2700     #2700 ~~45mis
    water_drank_time= time.perf_counter()
    eyes_roll_time= time.perf_counter()
    phy_workout_time= time.perf_counter()
    while (time.perf_counter()-code_breaker_counter) <= 60 :

        if (time.perf_counter()-water_drank_time) >= water_brk_time:
            play_water()
            if input("please enter \"Done\" if u done with drinking water: ") == done.lower():
                glasses_of_water_drank += 1
                mixer.music.stop()
                water_drank_time = time.perf_counter()
                var = "Drank the "+str(glasses_of_water_drank)+"th glass of water"
                Logger("Drank Water")
                print(var)


        if (time.perf_counter() - eyes_roll_time) >= eyes_brk_time :
            play_eyes()
            if input("please enter \"Done\" if u are done rolling your eyes: ") == done.lower():
                mixer.music.stop()
                eyes_roll_time= time.perf_counter()
                Logger("rolled the eyes")


        if (time.perf_counter()-phy_workout_time) >= phy_brk_time:
            play_physical()
            if input("please enter \"Done\" if u have done some workout: ") == done.lower():
                mixer.music.stop()
                phy_workout_time = time.perf_counter()
                Logger("Did Some Workout")
    print('')
    print("\nITS TIME TO GO HOME :)")





# def sleep_25():
#     tic =time.perf_counter()
#     time.sleep(25)
#     tok =time.perf_counter()
#     current_time=(tok-tic)
#
# def sleep_30():
#     tic =time.perf_counter()
#     time.sleep(25)
#
#     tok =time.perf_counter()
#     current_time=(tok-tic)
# def sleep_45():
#     tic =time.perf_counter()
#     time.sleep(45)
#
#     tok =time.perf_counter()
#     current_time=(tok-tic)

def Logger(log_message):

    with open("LOG_Healthy_Pro.txt", "a" ) as Log:
        Log.write("\n[")
        Log.write(getdate())
        Log.write("]  ")

        Log.write(log_message)

def play_water():
    mixer.music.load("Water.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()
def play_eyes():
    mixer.music.load("Water.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()
def play_physical():
    mixer.music.load("Water.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()

# def list_gen():
#     num3=0
#     num2=0
#     num1=0
#     num4={0}
#     list_= []
#     while num1 & num2 & num3 <475:
#         num1+=25
#         list_.append(num1)
#         num2+= 30
#         num3+= 45
#         list_.append(num2)
#         list_.append(num3)
#
#     list_.sort()
#     for j in list_ :
#         if j <480:
#             num4.add(j)
#         else:
#             continue
#     num5 = sorted(num4)
#     num5.remove(0)



if inpu_start_ == "":
    print("GET READY BY DRINKING WATER")
    time.sleep(0)
    print("THEN GET READY BY ROLLING YOUR EYES")
    time.sleep(0)
    print("NOW DO SOME STRETCHING BEFORE STARTING TO CODE")
    time.sleep(0)
    main()






















#
# mixer.init()
# mixer.music.load("song.mp3")
# mixer.music.set_volume(0.7)
# mixer.music.play()
#
# mixer.music.unpause()
# mixer.music.stop()
# mixer.music.pause()
