// 챗봇용 코드

function response(room, msg, sender, isGroupChat, replier, ImageDB, packageName) {
  if (msg == "안녕") {
      var ments = ['숙제는 다 했어?', '좋은 하루 보내!', '오늘 하루도 화이팅:)', '포기하지마!', '날이 참 좋다~~~~~~']
      var num = Math.floor(Math.random()*5);
      replier.reply('안녕, ' + sender + '아, ' + ments[num]);
  }
}