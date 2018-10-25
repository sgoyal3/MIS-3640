<!DOCTYPE html>
<html>

<head>
        <meta charset="UTF-8">
        <meta name="description" content="Beauty Boss: Sharing stories from beauty entrepreneaurs from around the world />
        <meta name="author" content="Parina Daswaney">
        <title>BeautyBoss</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <style type="text/css">
        
        body{
        
                text-color: black;
                text-align: center;
                background-color: white;
                overflow: hidden;
              }

                
        #p1{
                margin-top: 70px;
                font-size: 20px;
                letter-spacing: 4px;
        }
        p.info{
                text-align: justify;
                padding:0px 50px 0px 50px;
                font-size: 30px;
                text-indent: 50px;
                font-weight: bold;
        }
        td{
                background-color: white;
                color: black;
                opacity: 0.7;
        }
        table :hover{
                opacity: 1;
        }
        table{
                margin: 70px 170px 30px 170px;
        }
        a#low{
            font-size: 30px;
            text-decoration: none;
            color: black;  
            font-weight: bold;  
        }
        img#img1{
                width:30%;;
                height: 300px;
                border: 5px ridge black;
        }
        p#imgtitle{
                margin-left: auto;
                margin-right: auto;
                font-weight: bolder;
                font-size: 30px;

        }

        ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color:#dd0072;
    text-align: left  ;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 12px 12px;
    text-decoration: none;
}

li a:hover {
    background-color: #111;
}

.navbar {
  overflow: hidden;
  background-color: #333;
  font-family: Arial;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}


.dropdown .dropbtn {
  font-size: 16px; 
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit; 
  margin: 0; 
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}


.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

        </style>
        <script type="text/javascript">
            var slides=new Array ("divya.png","victoria.png","clare.png",);
            var description=new Array("Divya Gugnani","Victoria Tsai","Clare McGrowdie",);
            var i=0;
            function slideshow(){
                var x=document.getElementById("img1");
                var y=document.getElementById("imgtitle");
                
                if (i==slides.length){
                    i=0;
                }
                x.src=slides[i];
                y.innerHTML=description[i];
                i++;
                setTimeout("slideshow()", 1000);
            }

        </script>
</head>

<body onload="slideshow()">

<ul>
  <li class="nav" id="active"><a href="index1.htm">Home</a></li>
  <li class="nav"><a href="ContactUs.htm">Contact Us</a></li>
  <li class="nav"><a href="AboutMe.htm">About Me <Menu></Menu></a></li>
  <div class="dropdown">
        <button class="dropbtn"><a href="BeautyBosses.htm">BeautyBoss</a></li>
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
                <a class="nav" href="USA.htm">USA</a>
                         <a class="nav" href="India.htm">India</a>
                         <a class="nav" href="Australia.htm">Australia</a>
                        </div></div>
        

                
</li>
</ul>

<img src="1.jpg" alt="logo" title="logo"> 

<table>
        <tr>
                <td>
                        <p class="info">
                Hi everyone! Welcome to my blog Beauty Boss. Beauty Boss is a collective of beauty entrepreneurs, a platform to share stories and experiences,  and a collaborative center that brings these “bosses” together. Taking after the name, Beauty Boss, we created this platform to be a space where anyone interested in the beauty industry can come and find inspiration and advice,  through browsing our archive of our Beauty Bosses. Each week, we will be featuring a series of beauty entrepreneurs around the world through full length and mini interviews about their passions, businesses, talents, and goals. As these beauty boss’ change the world one lipstick at a time, we hope to highlight their stories and bridge the gap between the lovers of the beauty industry and entrepreneurs within the field.
                </p>
        </td>
</tr>
</table>

<img src="Images/oya.jpg" id="img1" title="">
<p id="imgtitle">O Ya</p>

<p><audio controls="controls" loop="loop">
        <source src="homemusic.mp3" type="audio/mp3"> 
</audio>
</p>

</body>

</html>