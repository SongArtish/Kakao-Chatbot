// 테스트용 JS코드! 챗봇용 코드 아님!
// 아침 저녁 알람을 node-schedule로 돌려보려구 했으나, 마음같지 않네요.
// 해당 코드 창에서는 돌아가요!!
// 챗봇에 해당 라이브러리 적용하는 방법, 혹은 적용가능한 다른 라이브러리, 혹은 다른 아이디어 바랍니다!!

const schedule = require('node-schedule');

const start = schedule.scheduleJob('0 50 8 ? * 1-5', function(){
  console.log('~ 8:59까지');
  console.log('👉 입실체크');
  console.log('👉 건강설문');
});

const end = schedule.scheduleJob('0 0 18 ? * 1-5', function(){
  console.log('~ 18:30까지');
  console.log('👉 입실체크');
  console.log('👉 건강설문');
});

const test = schedule.scheduleJob('10 * * * * *', function(){
  console.log('test');
  console.log('test2');
});

// function response(room, msg, sender, isGroupChat, replier, ImageDB, packageName) {
//   const schedule = require('node-schedule');
//   const test = schedule.scheduleJob('10 * * * * *', function(){
//     replier.reply('test');
//     replier.reply('test2');
//   });
// }

// function response(room, msg, sender, isGroupChat, replier) {
//   if (msg.includes("시작시작")){
//     const schedule = require('node-schedule');
//     const test = schedule.scheduleJob('10 * * * * *', function(){
//       replier.reply('test');
//       replier.reply('test2');
//     });
//   }
// }