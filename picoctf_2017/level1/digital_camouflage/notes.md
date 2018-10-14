## 11 Oct 2018
I'm initially opening the clue.  It states the following:
> **Digital Camouflage**
> We need to gain access to some routers.  Let's try and see if we can find the password in the captured network data: data.pcap.
Attached to this clue was (Surprise!) a pcap file.  Now to find a way to examine pcaps in Linux.

---

Looks like tcpdump might be my best bet for a native kali package that understands pcaps.  Hmmm.  This landing is gonna get pretty interesting.

---

Wait!  Holy fins, Batman!  Kali has Wireshark!

---

This seems simple enough.  It's a basic capture between a client `10.0.0.5` and a web server `10.0.0.1`.  The client requests a web page.  The server returns a web form with username and password fields.  The client responds with the fields filled out.
```
Key: pswrd
Value: dEo2NFpxYmRMdw==
```

---

Well, that value didn't work.  I checked the rest of the pcap.  No other passwords.  Checked the hint.  It said that the password might be encrypted.  Hmm, but with what?

---

Well, now, we might be on to something.  I right-clicked on the first GET request packet and selected `Follow -> HTTP Stream`.  Next thing you know, I've got an HTML document sitting right in front of me.

Client packet:
```
GET /index.html HTTP/1.1
User-Agent: Wget/1.16 (linux-gnu)
Accept: */*
Host: 10.0.0.1:8080
Connection: Keep-Alive
```

Server packet:
```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>NET-LINK Router - Log In</title>
<link href="styles.css" rel="stylesheet" type="text/css" />
</head>


<body>


<div class="container">
  <div class="header"><a href="index.html"><img src="images/netlink_logo.png" alt="Netlink Logo" width="180" height="90" style="display:block;" /></a> 
  </div>
  <div class="sidebar1">
    <ul class="nav">
      <li><a href="index.html">Log In</a></li>
      <li><a href="pages/pictures.html">Pictures</a></li>
      <li><a href="pages/about.html">About</a></li>
      <li><a href="pages/help.html">Help</a></li>
    </ul>
    <div id = "sidebarbox">
     <p>Please log in.</p>
    </div>
</div>
  <div class="content">
    <h1>Log In </h1>
    <form name="login" class="contentstuff" method="post" action="pages/main.html" onsubmit="modifyPass()">
    <table>
     <tr>
         <td>Username</td>
            <td><input type="text" name="userid"/></td>
        </tr>
        <tr>
         <td>Password</td>
            <td><input type="password" name="pswrd"/></td>
        </tr>
    </table>


    <button type="submit">Submit</button>
<input type="reset" value="Cancel"/>
    </form>
    
    <script>
  function modifyPass(){
   document.login.pswrd.value = btoa(document.login.pswrd.value);
  }
</script>
  </div>
  <div class="footer">
    <p>NET-LINK Router Administration &copy; 2016 by PPP</p>
  </div>
  </div>
</body>
</html>
```

---

And there it is, the clue I needed. `<form name="login" class="contentstuff" method="post" action="pages/main.html" onsubmit="modifyPass()">`. So, the password is being modified by the modifyPass() function before being sent to the server.

## 14 Oct 2018
I've decided that the following code deserves a closer look.
```
<script>
  function modifyPass(){
    document.login.pswrd.value = btoa(document.login.pswrd.value);
  }
</script>
```
I've found that typically the `<script>` tag refers to javascript when no other language is specified.  Doing a search turned up [information about the `btoa()` function in javascript](https://www.w3schools.com/jsref/met_win_btoa.asp).  It looks like I can use the `atob()` function to decode it.

---

I created a simple html page to decode the password.  I'm not very good at javascript, so it needs a bit of work.  At this point, it prints nothing out.

---

Alright, that took a bit of work, but I finally got a [working script][./decode.html]. The decrypted password is `tJ64ZqbdLw`.

---

Entered the code.  SUCCESS!
