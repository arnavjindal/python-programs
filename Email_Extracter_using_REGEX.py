import re

str =''' 
Paying for cell phone service can be expensive. Especially if you have a really high-end phone, the bill for monthly service can be way out of your price range.
 So what are you supposed to do if you want to own a nice cell phone, but don’t want to pay for service? One solution is to get your texting and calling done by other means.

There are apps you can download that will allow you to text and call for free, but not all phones support these apps and you might be limited in the amount of call time you get or the amount of texts you can send.
 Thankfully there is one completely free way you can send text messages that doesn’t require any other downloads or services, texting via email.

Many people are completely unaware that almost every mobile company has an email address for texting that you can use your own email address to send texts to,
 thus effectively sending a text message from your email account directly to someone’s cell phone inbox.
 Let’s take a more in-depth look at just how you can accomplish this, and what the pros and cons are of texting via email, especially if you are trying to text many people at once.

How Can You Text via Email?
Texting via email is unbelievably simple, you simply type in the email to SMS gateway for whatever carrier your recipient uses, and punch in their cell phone number in front of the “@” sign.
For example if your recipient’s cellphone number is 1-123-456-7891 and their carrier is AT&T, you would type in the following address in the “send to” box: “11234567891@txtatt.net”.
Almost every single carrier has its own address for this specific purpose, here is a list of all the major carriers’ email to sms gateways:

T-Mobile – number@tmomail.net
Virgin Mobile – number@vmobl.com
AT&T – number@txt.att.net
Sprint – number@messaging.sprintpcs.com
Verizon – number@vtext.com
Tracfone – number@mmst5.tracfone.com
Ting – number@message.ting.com
Boost Mobile – number@myboostmobile.com
U.S. Cellular – number@email.uscc.net
Metro PCS – number@mymetropcs.com
One of the advantages to sending texts via email is the fact that it’s completely free.
You could however incur some charges if you send too many texts within a short time frame,
 as the mobile carrier might block or limit your domain from sending messages and you will have to pay a fee on a per-message basis if you want to keep sending texts at your current rate. 
We will discuss other services  which are superior to email texting if you are trying to communicate with many people at once or provide other options to them such as polls and surveys.

Cons of Texting via Email
Cons of Texting via Email
While this is a neat little trick you can use if you ever find yourself out of service or without a cell phone, texting via email does have its drawbacks.
Unlike normal mail, email will never be a guaranteed delivery service. There can be problems with the network or any number of issues that prevent your text from being sent on time.

As stated above, if you are trying to send a lot of messages with this method, you could find your domain blocked within a very short period of time.
Mobile carriers have every incentive to limit this type of communication and they can do so at their own discretion.
If they think you are spamming or getting too much use out of this free texting loophole, they will not hesitate to throttle your traffic or block your messages entirely.

Another downfall to texting via email is the fact that you are limited to a certain character length. If you go over that character length, your message will be chopped up into pieces or it might not get to its recipient in its entirety. 
The caller Id from an email text message is also very long.

Superior Texting Alternatives
Superior Alternatives
If you’re looking for a better way to communicate with many people at once and even be able to conduct things like surveys and send custom voice messages, you should look into mass notification services such as DialMyCalls.
DialMyCalls is a much more efficient method for mass communication and notification, and it’s perfect for sending updates to your contacts.

You won’t have to worry about chopped up messages, limited sending capacity or other troubles with DialMyCalls.
Whether you are organizing a party or event, or looking to keep in touch with many employees or contacts at once for any reason, DialMyCalls’ web-based software is the perfect solution to your mass notification needs.

In Conclusion
If you are ever in a pinch and need a way to communicate for free via text, you can send text messages to any major mobile service provider by using the guidelines in this article.
This is very useful information to know in case of financial emergency, and if you are just planning to send a few texts here and there you will have no problem at all getting your message across within a decent amount of time.'''

pattern =(r'\w+@\w+\.[a-z]+\S*\b')
result = re.findall(pattern, str)

with open("email_extracter.txt","w") as filee:
    for i,j in  enumerate(result) :
         filee.write(f"Email {i}- {j}\n")




#Harry's Code -
# email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
email = re.findall(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+",str)

print(email)