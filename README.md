# Vaidu_Doctor
This is an AI & AR based platform for diagnosing & consulting heath issues.
Here 3 categories are available. 
1. Diagnose plant leaves in your garden or farms. 
2. Diagnose you using chest x-rays.
3. You can ask/consult Vaidu for health problem your are facing.

First two things are done using Deep learning model and third one is done using augmented reality where you will have doctor right at your place through mobile camera by which you will have good experience at home with ease and comfort.
                
## Inspiration
From last one year whole world is facing pandemic of covid-19, people cant step out from their home and everywhere mainly Covid fight is seen. Almost every hospital was engaged in fighting corona. But there are various other diseases also not for humans but plants also. At many places farmers cant reach to doctor and citizens also cant reach out to doctor for enquiry and consultancy due to pandemic. So this project is approach for this to use modern technologies of "Deep learning" & "Augmented reality" to help doctors to reach out patients and farmers and also proving medical facility right on your device. 

## What it does
1. Diagnose plant leaves from your garden or farm to know if any disease is present from over 38 different kind of diseases and if yes then which one.
2. Diagnose human chest related diseases providing chest c-ray over 14 kinds of diseases.
3. You can meet a virtual doctor using AR to know remedy or solution for health problem you may be facing.

## How we built it
For this first deep learning model was was made using "Transfer learning" as training whole model takes too much time. Datasets of chest x-rays & plant leaves were taken from internet and then build a "Flask web app". Meeting vaidu ar app is made with the help of unity where 3D model of medical worker doctor is being taken as 'Vaidu' and given some animation to it along with facility of interacting with doctor using canvas and voice.

## Challenges we ran into
Deep learning model were not working well in JavaScript using "TFJS" and were giving errors so I shift to flask app.
In AR part giving animation to prefab model was going difficult where if I put model as prefab then I cant add animation further to default animation which is not nice for interaction so I put that model in scene and gave animation. Now it works fine.

## Accomplishments that we're proud of
This can do diagnosis using plant leaf & chest x-ray images which will be really helpful to patients and farmers in pandemic situation where meeting people and also it will facilitate not just for covid situation but otherwise too that we can diagnose from our device mobile or pc.
Also By this you can meet a doctor right at your place and convey your health problem. This is very much useful approach in such pandemic situation, where many people can't step out of their home and in other situations also. Using "Augmented reality" user will have nice experience of this.


## What we learned
I learn how to make flask app. Also I learn about augmented reality and how to much useful apps from it.

## What's next for Vaidu Doctor
Next I will include more facilities like giving voice recognition of user in ar app so that interaction can happen totally by voice.
Also include other kind of diagnosis with very much less error rate.
