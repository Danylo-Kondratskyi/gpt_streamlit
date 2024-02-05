css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-message.user {
    background-color: #000000;
    text-color: #000000;
}
.chat-message.bot {
    background-color: #000000;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #11E8CF;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/jgKNgj3/Leonardo-Creative-ABSTRACT-A-pie-chart-showing-the-breakdown-a-2.jpg" >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/x5mM5dK/TER-Riu-the-boy-in-the-dark-sky-night-edfa2078-01e0-424d-8409-f01497bf6522.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''