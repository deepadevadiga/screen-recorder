import cv2, numpy as np, pyautogui, time

fps=10
seconds=int(input("Recording seconds: "))
size=pyautogui.size()
writer=cv2.VideoWriter("screen_recording.avi",
    cv2.VideoWriter_fourcc(*"XVID"),fps,size)

print("Recording...")
end=time.time()+seconds
while time.time()<end:
    frame=np.array(pyautogui.screenshot())
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    writer.write(frame)
    time.sleep(1/fps)
writer.release()
print("Saved screen_recording.avi")
