# import tkinter as tk
# import requests
# from PIL import Image,ImageTk
# root=tk.Tk()
# root.title('Check Weather')
# root.geometry('600x600')
# def format_response(weather):
#     try:
#         city=(weather['name'])
#         condition=(weather['weather'][0]['description'])
#         temp=(weather['main']['temp'])
#         final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
#     except:
#         final_str='Error'
#     return final_str

# def gets(city):
#     weather_key='0fecc68658de6ebc1257a738a307885b'
#     url='https://api.openweathermap.org/data/2.5/weather'
#     params={'APPID':weather_key,'q':city,'units':'imperial'}
#     response=requests.get(url,params)
#     # print(response.json())
#     weather=response.json()
#     print(weather['name'])
#     print(weather['weather'][0]['description'])
#     print(weather['main']['temp'])
    
#     result['text']=format_response(weather)

# img=Image.open('./pic.jpg')
# img=img.resize((600,600),Image.ANTIALIAS)
# img_photo=ImageTk.PhotoImage(img)

# bg_lb1=tk.Label(root,image=img_photo)
# bg_lb1.place(x=0,y=0,width=600,height=600)

# heading_title=tk.Label(bg_lb1,text="Find weather",fg='white',bg='dark blue',font=('times new roman',18,'bold'))
# heading_title.place(x=200,y=18)

# frame_1=tk.Frame(bg_lb1,bg="white",bd=5)
# frame_1.place(x=80,y=50,width=450,height=50)

# text1=tk.Entry(frame_1,font=('times new roman',25),width=15)
# text1.grid(row=0,column=0,sticky='w')

# btn=tk.Button(frame_1,text='get weather',fg='black',font=('times new roman',16,'bold'),command=lambda:gets(text1.get()))
# btn.grid(row=0,column=1,padx=10)

# frame_2=tk.Frame(bg_lb1,bg="white",bd=5)
# frame_2.place(x=80,y=130,width=450,height=300)

# result=tk.Label(frame_2,font=40,bg='white',justify='left')
# result.place(relwidth=1,relheight=1)

# root.mainloop()


# z=7
# def func(y):
#     global z
#     z=z+2
#     print(y,z)
# func(0)


n=12
l=[]
k=0
for i in range(2,52):
    for j in range(2,i//2):
        if i%j==0:
            k=1
    if k==0:
        l.append(i)
    k=0
print(l)
        



