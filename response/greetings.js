const scriptName = 'greetings';

/*
* (string) room
* (string) sender
* (boolean) isGroupChat
* (void) replier.reply(message)
* (boolean) replier.reply(roo, message, hideErrorToast = False)
  // 전송 성공 시 true, 실패 시 false 반환
* (string) imageDB.getProfileBase64()
* (string) packageName
*/

function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
  // 기본인사
  // sender에는 보낸사람 이름이 저장되어 있다.
  if ('안녕' in msg) {
    const greets = ['안녕', '하이하이', '할루~~~'];
    const ments = ['좋은 하루 보내!', '날이 참 좋다~~!', '오늘은 네 인생의 최고의 날이야!', 'ㅎㅎ']
    let num1 = Math.floor(Math.random()*length(greets))
    let num2 = Math.floow(Math.random()*length(ments))
    replier.reply(greets[num1] + ' ' + sender + ' ' + ments[num2])
  } else if ('하이' in msg) {
    replier.reply(sender + "하이")
  } else if ('Hi' in msg) {
    replier.reply(sender + "Hi")
  } else if ('hi' in msg) {
    replier.reply(sender + "hi")
  } else if ( msg === '헤이' ) {
    replier.reply("왜!!")
  } else if ( msg === 'Hey' ) {
    replier.reply("What!!")
  } else if ( msg === 'hey' ) {
    replier.reply("hey why!")
  } 

  // 기본대화
  else if ( msg === '뭐해' ) {
    replier.reply("너랑 노는중~~")
  } else if ( msg === '바보' ) {
    replier.reply("나는 사랑해")
  } 

  // 정보
}

function onCreate(savedInstanceState, activity) {
  const textView = new android.widget.TextView(activity)
  textView.setText("Hellow World!")
  textView.setTextColor(android.graphics.Color.DKGRAY)
  activity.setContentView(textView)
}
function onStart(activity) {

}
function onResume(activity) {
  
}
function onPause(activity) {
  
}
function onStop(activity) {
  
}