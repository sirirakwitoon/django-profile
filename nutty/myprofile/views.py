from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.


# returns JSON object as
# a dictionary


def index(request):
    f = open('./myprofile/backgroundbase64.json',)
    data = json.load(f)

    print(data["image"])
    return HttpResponse('''
   <!DOCTYPE html>
<html>

<head>
    <style>
        .wfull {
            width: 100%;
        }
        
        .w4 {
            width: 1rem;
        }
        
        .w6 {
            width: 1.5rem;
        }
        
        .hscreen {
            height: 100vh;
        }
        
        .flex {
            display: flex;
        }
        
        .flexcol {
            flex-direction: column;
        }
        
        .flexrow {
            flex-direction: row;
        }
        
        .justifybetween {
            justify-content: space-between;
        }
        
        .px8 {
            padding-right: 2rem;
            padding-left: 2rem;
        }
        
        .pt10 {
            padding-top: 2.5rem;
        }
        
        .fontbold {
            font-weight: bold;
        }
        
        .textyellow500 {
            color: rgb(245, 158, 11);
        }
        
        .ml2 {
            margin-left: 0.5rem;
        }
        
        .mb8 {
            margin-bottom: 2rem;
        }
        
        .grid {
            display: flex;
        }
        
        .gridcols4 {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }
        
        .gap4 {
            gap: 1rem;
        }
        
        .cursorpointer {
            cursor: pointer;
        }
        
        .hoverunderline:hover {
            text-decoration: underline;
        }
        
        .pb10 {
            padding-bottom: 2.5rem;
        }
        
        .pt3 {
            padding-top: 0.75rem;
        }
        
        .itemsend {
            align-items: flex-end;
        }
        
        .itemscenter {
            align-items: center;
        }
        
        .rotate90 {
            rotate: 90deg;
        }
        
        .mybackground {
            background-image: url("data:image/png;base64,'''+data['image']+'''");
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
        }
        .sirirak{
            font-size:72px;
        }
        .nutsrk{
            font-size:32px;
        }
        .itemsbaseline{
            align-items: baseline;
        }
    </style>
</head>

<body style="margin: 0px !important;">

    <div class="hscreen flex flexcol justifybetween px8 mybackground">
        <div class="flex flexrow justifybetween pt10">
            <div class="flex fontbold itemsbaseline">
                <h1 class="textyellow500 sirirak">Sirirak </h1>
                <h1 class="ml2 sirirak ">Witoon</h1>
                <h1 class="ml2 textyellow500 nutsrk">  (Nutsrk) </h1>

            </div>
            <div class="grid gridcols4 gap4 fontbold">
                <h3 class="cursorpointer hoverunderline">
                    Home
                </h3>
                <h3 class="cursorpointer hoverunderline">
                    Resume
                </h3>
                <h3 class="cursorpointer hoverunderline">
                    Works
                </h3>
                <h3 class="cursorpointer hoverunderline">
                    Contacts
                </h3>
            </div>
        </div>
        <div class="pb10 flex flexrow justifybetween itemsend ">
            <div class="flex flexcol">
                <div class="flex">
                    <h3 class="fontbold">Email </h3>
                    <h3 class="ml2">nutsrk@odds.team</h3>
                </div>
                <div class="flex">
                    <h3 class="fontbold">Phone </h3>
                    <h3 class="ml2">092-772-5330</h3>
                </div>
            </div>

        </div>
    </div>

</body>

</html>

    ''')
