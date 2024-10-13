# import gtts
from playsound import playsound 
# good_job = gtts.gTTS("Good Job my dear !").save("good_job_audio.mp3")
# ooops = gtts.gTTS("ooops! Try again please!").save("try_again_audio.mp3")

def input_str(name='parsa'):
    str = input(f'please type the name "{name}" : \n')
    if str.lower() == name :
        playsound('good_job_audio.mp3')
    else:
        playsound('try_again_audio.mp3')
        input_str(name)

input_str()